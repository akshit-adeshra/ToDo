from django.urls import path
from ToDoApp.views import home


urlpatterns = [
    path('', home, name='home',),
]