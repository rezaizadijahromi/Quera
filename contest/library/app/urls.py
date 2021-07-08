from django.urls import path

app_name = 'app'

from . import views

urlpatterns = [
    path('get_book_users/<int:book_id>/', views.Library, name='home')
]
