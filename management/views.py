from django.http.response import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):

    #book = Book.objects.order_by('-id').first()
    book = Book.objects.first()
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)


def display_book(request, book_id):

    book = Book.objects.get(pk=book_id)
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)

def books (request):
    book_list = Book.objects.all()
    return render(request,"management/books.html", context={"book_list":book_list})


def authors (request):
    author_list = Author.objects.all()
    return render(request,"management/authors.html", context={"author_list":author_list})


def book_author (request, author_name):
    book_list = Book.objects.filter(author= author_name)
    cur_author = Author.objects.get(pk=author_name)
    return render(request,"management/book_author.html", context={"book_list":book_list, "author":cur_author})

