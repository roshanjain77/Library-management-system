from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/<int:book_id>', views.display_book, name="book"),
    path('profile/', views.profile, name="profile")
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
