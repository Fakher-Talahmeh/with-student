from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    books =book.objects.all()
    authors = Author.objects.all()
    return render(request,'index.html',context={'books':books,'authors':authors})

def append_book(request):
    author =Author.objects.get(
            name=request.POST.get('author-name')
        )
    new_book = book.objects.create(
        name=request.POST.get('name'),
        author=author
    )
    new_book.save()
    return redirect('home')

def append_author(request):
    new_author = Author.objects.create(
        name=request.POST.get('name')
    )
    new_author.save()
    return redirect('home')

def update_book(request,pk):
    update_book = book.objects.get(id=pk)
    update_book.name = request.POST.get('name')
    update_book.save()
    return redirect('home')

def delete_book(request,pk):
    book.objects.get(id=pk).delete()
    return redirect('home')

def details_book(request,pk):
    view_book = book.objects.get(id=pk)
    return render(request,'book_details.html',{'book':view_book})