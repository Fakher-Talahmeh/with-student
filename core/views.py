from django.shortcuts import render,redirect
from .models import *
from .forms import BookForm,AuthorForm
# Create your views here.
def index(request):
    books =book.objects.all()
    authors = Author.objects.all()
    book_form = BookForm()
    author_form = AuthorForm()
    return render(
        request,
        'index.html',
        context={'books':books,
                 'authors':authors,
                 'book_form':book_form,
                 'author_form':author_form
                 })

def append_book(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')

def append_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')

def update_book(request,pk):
    update_book = book.objects.get(id=pk)
    form = BookForm(request.POST,instance=update_book)
    if form.is_valid():
        form.save()
    return redirect('home')

def delete_book(request,pk):
    book.objects.get(id=pk).delete()
    return redirect('home')

def details_book(request,pk):
    view_book = book.objects.get(id=pk)
    book_form = BookForm()
    return render(request,'book_details.html',{'book':view_book,'book_form':book_form})