from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm


def index(request):
    # If the form was sent, work with it
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()  # if the form is valid, we save the form, it means that the form creates a new Author object

            # After saving new form do redirect to the same page
            return redirect('author:index')
    else:  # if it was a GET-request, just create new form
        form = AuthorForm()

    sort_by = request.GET.get('sort', 'surname')
    order_by = request.GET.get('order', 'asc')
    ordering = '-' + sort_by if order_by == 'desc' else sort_by

    authors = Author.objects.all().order_by(ordering)
    context = {
        'authors': authors,
        'current_sort': sort_by,
        'current_order': order_by,
        'form': form
    }
    return render(request, 'author/index.html', context)


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('author:index')


def single_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return render(request, 'author/404.html', {'author_id': author_id})
    return render(request, 'author/single_author.html', {'author': author})
