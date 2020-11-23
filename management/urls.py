from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books', views.books, name="books"),
    path('book_author/<str:author_name>', views.book_author, name="book_author"),
    path('authors', views.authors, name="authors"),
    path('book/<int:book_id>', views.display_book, name="book"),
    path('profile/', views.profile, name="profile"),
    path('developers', views.developers, name="developers"),
    path('mentors', views.mentors , name="mentors"),
    path('login', views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
