"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from first_project.views import (index_page, time_page, calc_page,
                                 expression_page, history_page, delete_page,
                                 clear_page, new_expression, str2words, logout_view, str_history)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('time/', time_page),
    path('calc/', calc_page),
    path('expression/', expression_page),
    path('history/', history_page),
    path('delete/', delete_page),
    path('clear/', clear_page),
    path('new/', new_expression),
    path('str2words/', str2words),
    path('str_history/', str_history),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', logout_view)
]
