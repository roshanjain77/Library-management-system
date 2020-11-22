from django.http.response import HttpResponse
from django.shortcuts import render
import datetime

from .models import *

# Create your views here.

Fineperday = 5

def update_data(user):
    data = user.data
    borrows = user.borrowed.all()

    tot = 0
    cur_date = datetime.date.today()
    for borrow in borrows:
        if borrow.return_date < cur_date:
            fine = (cur_date - borrow.return_date).days * Fineperday
            borrow.fine = fine
            borrow.save()
            tot += fine
    
    data.tot_fine = tot
    data.total_books_due = len(borrows)
    data.save()
    return
            




def index(request):

    book = Book.objects.order_by('-id').first()
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)


def display_book(request, book_id):

    book = Book.objects.get(pk=book_id)
    context = {"book": book, "genre": book.genre.all()}
    return render(request, 'management/book.html', context=context)


def profile(request):

    user = User.objects.get(username=request.user.username)

    update_data(user)

    data = user.data
    context = {"user": user, "data": data, "borrows": user.borrowed.all()}

    return render(request, 'management/profile.html', context=context)