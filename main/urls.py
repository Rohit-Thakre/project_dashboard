from django.urls import path
from main import views
urlpatterns = [
    path('',views.home, name='home'),
    path('read_json/', views.read_json, name='read_json')
]