from django.shortcuts import render
from django.http import HttpResponse
from .models import Book





def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def lab5(request):
    return render(request, 'bookmodule/lab5.html')


def search(request):
    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]






def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        
        books = __getBooksList()
        newBooks = []

        
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    
    return render(request, 'bookmodule/search.html')

def add_books(request):
    
    mybook = Book(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1)
    
    
    mybook.save()
    
    
    books = Book.objects.all()
    
    
    return render(request, 'bookmodule/bookList.html', {'books': books})


def simple_query(request):
    
    mybooks = Book.objects.filter(title__icontains='and')  

    
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='and') \
                          .filter(edition__gte=2) \
                          .exclude(price__lte=100)[:10]

    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

