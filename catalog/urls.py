from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books , name='books'),
    path('profile', views.profile, name='profile'),
    path('addbook', views.addBook , name='addBook'),
    path('modifybook', views.modifyBook, name='modifyBook'),
    path('borrowbook', views.borrowBook, name='borrowBook'),
    path('addbookreview', views.addBookReview, name='addBookReview'),
    path('reviews', views.reviews, name='reviews'),
    path('editbook', views.editBook, name='editBook'),
    path('deletebook', views.deleteBook, name='deleteBook'),
    path('addinstance', views.addInstance, name='deleteBook'),
    path('removeinstance', views.removeInstance, name='deleteBook'),
    path('createmanager', views.createManager, name='createManager'),
    path('logs', views.logs, name='logs'),
]