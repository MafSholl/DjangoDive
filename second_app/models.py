from django.db import models

# Create your models here.

class Book(models.Model):
    GENRE_CHOICES = (
        ('COMEDY', 'Comedy'),
        ('TRAGEDY', 'Tragedy'),
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-Fiction'),
        ('ROMANCE', 'Romance'),
    )
    title = models.CharField(max_length=255, verbose_name="Book title")
    description = models.TextField(verbose_name="Description", default="Any Text")
    date_published = models.DateField(auto_now_add=True) #"auto_now=True"- keeps track of time each time the objext changes state
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    #For field we want optional in the database write field as - "null = True"
    #For field we want optional in the front-end write field as - "blank = True"

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    books = models.ManyToManyField(Book, related_name='authors', through='BookAuthor')

class BookAuthor(models.Model):
    ROLES = (
        ('AUTHOR', 'Author'),
        ('CO_AUTHOR', 'Co-Author'),
        ('EDITOR', 'Editor')
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=ROLES)

class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default='Lagos')
    country = models.CharField(max_length=255, default='Nigeria')
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)