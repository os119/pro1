from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('lab5/', views.lab5, name="lab5"),
    path('search_books/', views.search_books, name="search_books"),
    path('add_books/', views.add_books, name='add_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('p', views.test_create, name='p'),
    path('lab8/task1/', views.t1, name='t1'),
    path('lab8/task2/', views.t2, name='t2'),
    path('lab8/task3/', views.t3, name='t3'),
    path('lab8/task4/', views.t4, name='t4'),
    path('lab8/task5/', views.t5, name='t5'),
    path('lab9', views.lab9, name='lab9'),
    path('lab10one/<int:bid>/', views.oneBook, name='lab10one'),
    path('lab10books/', views.books, name='lab10books'),
    path('update/<int:bid>/', views.updateBook, name='update'),
    path('delete/<int:bid>/', views.deleteBook, name='deleteBook'),
    path('add/', views.addBook, name='addBook'),
    path('addf/', views.addBookf, name='addBookf'),
    path('updatef/<int:bid>/', views.updateBookf, name='updateBookf'),
    path('qm/', views.qm, name='qm'),
    path('add_user/', views.a, name='u'),
    path('j/', views.j, name='j'),

    


   
   
    
]

