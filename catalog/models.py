from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns

import uuid  # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower

class Review(models.Model):
    content = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.TextField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    publisher = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    reserved = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

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
