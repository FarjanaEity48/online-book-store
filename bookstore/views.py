from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookstore/home.html',context)



def book_detail(request, pk):
    book= Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, "bookstore/book_detail.html", context)



