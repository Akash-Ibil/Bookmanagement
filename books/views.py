# books/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def homepage(request):
    return render(request, 'books/homepage.html') 

# List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

# Add new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list')
    else:
        form = BookForm()
    return render(request, 'books/form.html', {'form': form, 'action': 'Add'})
