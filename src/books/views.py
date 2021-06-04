from django.shortcuts import render
import json

bookData = open("C:/Users/chen/Desktop/DjangoExcercise/Django-Bookstore/books.json").read()
data = json.loads(bookData)

def index(request):
    context = {'books': data}
    return render(request, "books/index.html", context)

def show(request, id):
    singleBook = []
    for book in data:
        if book['id'] == id:
            singleBook = book
    context = {'book': singleBook}
    return render(request, "books/show.html", context)
