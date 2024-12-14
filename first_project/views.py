import random

from django.shortcuts import render
import datetime
from first_project.models import ExpressionHistory


def index_page(request):
    context = {"name": "Влад Рассоха",
               "pages_count": 5}

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
