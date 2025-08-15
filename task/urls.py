from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('task/<task_id>/',views.detail_page),
]