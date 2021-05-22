from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sales_manager.models import Book


def main_page(request):
    query_set = Book.objects.all()
    context = {"books": query_set}
    return render(request, "sales_manager/index.html", context=context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {"book": book}
    return render(request, "sales_manager/book_detail.html", context=context)


@login_required()
def book_like(request, book_id):
    book = Book.objects.get(id=book_id)
    book.likes.add(request.user)
    return redirect("main_page")
