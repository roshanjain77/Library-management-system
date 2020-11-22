from django.http.response import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):

    book = Book.objects.order_by('-id').first()
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)


def display_book(request, book_id):

    book = Book.objects.get(pk=book_id)
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)