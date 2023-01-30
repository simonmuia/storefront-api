from django.urls import path 
from playground.views import say_hello


# URLConf
urlpatterns = [
    path('', say_hello)
]