from django.shortcuts import render
from .models import Book


def index(request):
    # The sorting by name and ASC by default
    sort_by = request.GET.get('sort', 'name')  # get a sorting parameter, 'name' by default
    order_by = request.GET.get('order', 'asc')

    ordering = '-' + sort_by if order_by == 'desc' else sort_by

    books = Book.objects.all().order_by(ordering)
    context = {
        'books': books,
        'current_sort': sort_by,
        'current_order': order_by
    }
    return render(request, 'book/index.html', context)


def single_book(request, book_id):
    book = Book.get_by_id(book_id)
    if book is None:
        return render(request, 'book/404.html', context={'book_id': book_id})
    return render(request, 'book/single_book.html', {'book': book})
