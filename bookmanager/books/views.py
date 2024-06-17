from django.shortcuts import render , redirect
from .models import Book
from .forms import BookForm
from django.http import JsonResponse

# Create your views here.

def book_list(request):
    books = Book.objects.all()  #this will return all books
    return JsonResponse(list(books.values()), safe=False)

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)  #to get detail of specific book 
        return JsonResponse({"title": book.title, "author": book.author ,"published_date":book.published_date})
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status= 404)
    

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return JsonResponse({"id":book.id , "title": book.title, "author": book.author , "published_date": book.published_date})
    return JsonResponse({"error":"Invalid data"}, status = 400)
