from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('register/', views.register, name='register')
]