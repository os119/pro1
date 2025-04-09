from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Publisher
from django.db.models import Count, Min, Max, Sum, Avg
from django.db.models import Q


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

def ap(request):
    a= Publisher(name="ahmed",location="riyadh")
    a.save()
    all_publishers = Publisher.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': all_publishers})

def test_create(request):
    pub = Publisher.objects.filter(name="ahmed").first()
    book = Book(title="Django For Beginners", author="William S.", edition=1, publisher=pub)
    book.save()
    b=Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': b})

def t1(request):
    a=Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': a})

def t2(request):
    a=Book.objects.filter(Q(edition__gt=3)&(Q(title__icontains="co")|Q(author__icontains="co")))
    return render(request, 'bookmodule/bookList.html', {'books': a})

def t3(request):
    a=Book.objects.filter(~Q(edition__gt=3)&(~Q(title__icontains="co")&~Q(author__icontains="co")))
    return render(request, 'bookmodule/bookList.html', {'books': a})

def t4(request):
    a=Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': a})

def t5(request):
    a1=Count('id')
    a2=Sum('price')
    a3=Avg('price')
    a4=Max('price')
    a5=Min('price')
    q=Book.objects.aggregate(count=a1,sum=a2,avg=a3,max=a4,min=a5)
    return render(request,'bookmodule/lab8.html',{'stats':q})
    