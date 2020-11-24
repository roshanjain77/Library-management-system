from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    summary = models.TextField(max_length=1000)
    genre = models.ManyToManyField(Genre, related_name="books")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='media/')

    def __str__(self):
        return f'{self.id} {self.title}'


class Student(models.Model):
    roll_no = models.CharField(max_length=8, unique=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="data")
    pic = models.ImageField(blank=True, null=True, upload_to='media/')
    branch = models.CharField(max_length=32)
    contact_no = models.CharField(max_length=10)
    total_books_due = models.IntegerField(default=0)
    tot_fine = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.roll_no} {self.name}"


class Borrower(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    fine = models.IntegerField(default=0)

    def __str__(self):
        return self.student.first_name + " borrowed " + self.book.title
    
class request_book(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student} has requested {self.book}"

# class Reviews(models.Model):
#     review=models.CharField(max_length=100,default="none")
#     book=models.ForeignKey('Book',on_delete=models.CASCADE)
#     student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
#     CHOICES = (
#         ('0', '0'),
#         ('.5', '.5'),
#         ('1', '1'),
#         ('1.5', '1.5'),
#         ('2', '2'),
#         ('2.5', '2.5'),
#         ('3', '3'),
#         ('3.5', '3.5'),
#         ('4', '4'),
#         ('4.5', '4.5'),
#         ('5', '5'),
#     )

#     rating=models.CharField(max_length=3, choices=CHOICES, default='2')
