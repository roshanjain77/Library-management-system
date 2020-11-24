from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .models import *

# Create your views here.

Fineperday = 5

# used to update user data before they try to access 
# the profile page
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
            

def update_book_data(book_id):
    
    book = Book.objects.get(pk=book_id)
    in_use = len(Borrower.objects.filter(book=book))
    book.available_copies = book.total_copies - in_use
    book.save()
    return


def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"management/login.html")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        
        else:
            return render(request,"management/login.html")


def logout_view(request):
    logout(request)
    return render(request,"management/login.html")


def index(request):
    
    book = Book.objects.all().last()
    update_book_data(book.id)
    book = Book.objects.all().last()
    books = Book.objects.all()
    context = {"book": book, "genre": book.genre.all(), "book_list": books}
    return render(request, 'management/book.html', context=context)


def display_book(request, book_id):
    if request.method=="POST":
        if request.user.is_authenticated:
            book = Book.objects.get(pk=book_id)
            user = User.objects.get(username=request.user)
            book_request = request_book.objects.create(student=user, book=book)
            book_request.save()
            
    update_book_data(book_id)
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


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
        
    
    user = User.objects.get(username=request.user.username)

    update_data(user)

    data = user.data
    context = {"user": user, "data": data, "borrows": user.borrowed.all()}

    return render(request, 'management/profile.html', context=context)


def developers(request):
    return render(request, "management/developers.html", {"page_name":"Developers"})


def mentors(request):
    return render(request, "management/mentors.html", {"page_name":"Mentors"})
