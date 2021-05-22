from django.urls import path
from sales_manager import views


urlpatterns = [
    path("book_detail/<int:book_id>/", views.book_detail, name="book-detail"),
    path("book_like/<int:book_id>/", views.book_like, name="book-like"),
    path("", views.main_page, name="main_page"),
]
