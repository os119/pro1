from django.urls import path
from . import views
path('<int:bookId>', views.viewbook)
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('lab5/', views.lab5, name="lab5"),
]

