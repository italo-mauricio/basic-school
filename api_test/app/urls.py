from django.urls import path
from app.views import todo_list

urlpatterns = [
    path('', todo_list),
]