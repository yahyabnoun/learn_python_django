from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    # path("sports", views.sports_view),
    # path("finance", views.finance_view),
    path("<topic>", views.news_view),
    path("<int:num1>/<int:num2>", views.sum_view),

]