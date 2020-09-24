from django.urls import path,include
from . import views

app_name ='myportfolio'

urlpatterns = [
    path('',views.homepage,name="homepage"),
]