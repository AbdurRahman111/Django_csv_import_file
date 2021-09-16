
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('save_the_csv_file', views.save_the_csv_file, name='save_the_csv_file'),
]
