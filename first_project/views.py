import random
from datetime import datetime
from typing import Any

import datetime
from first_project.models import ExpressionHistory, StrHistory
from first_project.forms import StrForm


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from django.contrib.auth import authenticate


def index_page(request):
    context = {"name": "Влад Рассоха",
               "pages_count": 8}

    return render(request, "index_page.html", context)


def time_page(request):
    context = {"date": datetime.date.today().strftime("%d.%m.%Y"),
               "time": datetime.datetime.now().strftime("%H:%M:%S")}

    return render(request, "time_page.html", context)


def calc_page(request):
    return render(request, "calc_page.html")


def expression_page(request):
    n = random.randint(2, 4)
    operations = list(random.choice(["-", "+"]) for i in range(0, n - 1))
    nums = list(random.randint(10, 100) for i in range(0, n))
    operation = ""
    for i in range(0, n):
        operation += str(nums[i])
        try:
            operation += operations[i]
        except IndexError:
            pass
    answer = eval(operation)

    context = {
        "operation": operation,
        "answer": answer
    }

    expression_history = ExpressionHistory(
        expression=operation,
        answer=answer
    )
    expression_history.save()

    return render(request, "expression_page.html", context)


def history_page(request):
    expression_history = ExpressionHistory.objects.all()
    context = {
        "expression_history": expression_history
    }
    return render(request, "history_page.html", context)


def delete_page(request):
    expression_last = ExpressionHistory.objects.last()
    expression_last.delete()
    return render(request, "delete_page.html")


def clear_page(request):
    expression_history = ExpressionHistory.objects.all()
    expression_history.delete()
    return render(request, "clear_page.html")


def new_expression(request):
    if "operation" in request.GET:
        operation = request.GET["operation"]
        operation = str(operation)
        operation = operation.replace('plus', '+')
        operation = operation.replace('minus', '-')
        if operation == "":
            operation = "Нет выражения"

        print(operation)

        try:
            answer = eval(operation)

        except SyntaxError:
            context = {
                "operation": operation
            }
            return render(request, "new_wrong.html", context)

        context = {
            "operation": operation,
            "answer": answer
        }

        expression_history = ExpressionHistory(
            expression=operation,
            answer=answer
        )
        expression_history.save()
        return render(request, "new_page.html", context)

    else:
        context = {
            "operation": 'Нет выражения'
        }
        return render(request, "new_wrong.html", context)


@login_required
def str2words(request):
    if request.method == "POST":
        str_form = StrForm(request.POST)
        if str_form.is_valid():
            text = str_form.cleaned_data["text"]
            words = text.split()
            words_count = len(words)
            nums = []
            for word in words:
                if word.isdigit():
                    nums.append(word)
            nums_count = len(nums)

            #сохраняем в бд

            str_history = StrHistory(
                str=text,
                words_count=words_count,
                nums_count=nums_count,
                time=datetime.datetime.now().strftime("%H:%M:%S"),
                date=datetime.date.today().strftime("%d/%m/%Y"),
                author=request.user
            )
            str_history.save()
            print(datetime.datetime.now().strftime("%H:%M"), datetime.date.today().strftime("%d/%m/%Y"))

        else:
            str_form = StrForm(request.POST)
            words = []
            words_count = 0
            nums = []
            nums_count = 0

    else:
        str_form = StrForm(request.POST)
        words = []
        words_count = 0
        nums = []
        nums_count = 0

    context = {
        "words": words,
        "words_count": words_count,
        "nums": nums,
        "nums_count": nums_count,
        "str_form": str_form
    }
    return render(request, "str2words.html", context)


@login_required
def str_history(request):
    str_history = StrHistory.objects.filter(author_id=request.user.id)
    context = {
        "username": request.user.username,
        "user_id": request.user.id,
        "str_history": str_history
    }
    return render(request, "str_history_page.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
