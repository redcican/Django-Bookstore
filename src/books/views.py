from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from books.form import ReviewForm
from books.models import Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

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
        context['form'] = ReviewForm()
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
    if request.user.is_authenticated:
        newReview = Review(review=review, book_id=id, user=request.user)
        form = ReviewForm(request.POST,request.FILES, instance=newReview)
        if form.is_valid():
            form.save()
        # else:
        #     print("something went wrong")
        # review = request.POST['review']
        # newReview = Review(review=review, book_id=id, user=request.user)

        # if len(request.FILES) != 0:
        #     image = request.FILES['image']
        #     fs = FileSystemStorage()
        #     image_name = fs.save(image.name, image)        
        #     image = fs.url(image_name)
        # newReview.save()
    return redirect(f'/book/{id}')
