from django.shortcuts import render
import datetime

def my_page(request):
    context = {"name": "Vlad",
               "city": "Domodedovo"
               }

    return render(request, "my_page.html", context)


def index_page(request):
    context = {"name": "Влад Рассоха",
               "pages_count": 2}

    return render(request, "index_page.html", context)


def time_page(request):
    context = {"date": datetime.date.today().strftime("%d.%m.%Y"),
               "time": datetime.datetime.now().strftime("%H:%M:%S")}

    return render(request, "time_page.html", context)

def calc_page(request):
    return render(request, "calc_page.html")
