from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from books.models import Book, Review


class BookListView(ListView):
    # template_name = 'books/index.html' -> if not defined, 'book_list.html' is defautl used
    # context_object_name = 'books' ->  if not defined, book_list will be created for template

    def get_queryset(self):
        return Book.objects.all()
    
    
# def index(request):
#     data = Book.objects.all()
#     context = {'books': data}
#     return render(request, "books/index.html", context)


class BookDetailView(DetailView):
    model = Book
    
    # context_object_name = "BookReview" -> default is 'book' or 'object'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at') # one to many
        context['authors'] = context['book'].authors.all() # many to many
        return context

# def show(request, id):
#     singleBook = get_object_or_404(Book,pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singleBook, 'reviews': reviews}
#     return render(request, "books/show.html", context)

def author(request, author):
    books = Book.objects.filter(authors__name = author)
    context = {'book_list': books}
    return render(request,"books/book_list.html", context)


def review(request, id):
    body = request.POST['review']
    newReview = Review(body=body, book_id=id)
    newReview.save()
    return redirect("/book")
