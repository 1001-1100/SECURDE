from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('books', views.books , name='books'),
    path('addbook', views.addBook , name='addBook'),
    path('borrowBook', views.borrowBook, name='borrowBook'),
    path('addBookReview', views.addBookReview, name='addBookReview'),
    path('editBook', views.editBook, name='editBook'),
    path('deleteBook', views.deleteBook, name='deleteBook'),
    path('createManager', views.createManager, name='createManager'),
    path('logs', views.logs, name='logs'),
]