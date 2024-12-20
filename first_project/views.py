import random

from django.shortcuts import render
import datetime
from first_project.models import ExpressionHistory


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
