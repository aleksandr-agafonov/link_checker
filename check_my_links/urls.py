from django.urls import path
from . import views

urlpatterns =[
    path('', views.render_main_page, name='main_page'),
    path('result/', views.show_result, name='show_result'),
    path('clear_db/', views.clear_db, name='clear_db')
]