from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns

import uuid  # Required for unique book instances
from datetime import date

# from django.contrib.auth.models import User  # Required to assign User as a borrower
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from activity_log.models import UserMixin

class Book(models.Model):
    title = models.CharField(max_length=200,default='Untitled')
    author = models.CharField(max_length=200,default='Unknown')
    publisher = models.CharField(max_length=200,default='Unknown')
    publication_year = models.IntegerField(default=0)
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>', default=0)
    instances = models.IntegerField(default=1)
    borrowed = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.title



from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, email, password=None):
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         is_staff=True,
    #     )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password
        )
        user.is_administrator = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin, UserMixin):
    username = models.CharField(max_length=100,unique=True) 
    email = models.EmailField()
    idnum = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)
    is_manager = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['firstname', 'lastname', 'email', 'idnum']

    class Meta:
        # ordering = ['id_num','last_name']
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):              
        return self.username

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# class Author(models.Model):
#     """Model representing an author."""
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('died', null=True, blank=True)

#     class Meta:
#         ordering = ['last_name', 'first_name']

#     def get_absolute_url(self):
#         """Returns the url to access a particular author instance."""
#         return reverse('author-detail', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the Model object."""
#         return '{0}, {1}'.format(self.last_name, self.first_name)
