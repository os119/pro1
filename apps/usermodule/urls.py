from django.urls import path
from . import views
urlpatterns = [
    
    path('register/', views.register_1, name="users.register"),
    path('login/', views.login_1, name="users.login"),
    path('logout/', views.logout_1, name="users.logout"),
    path('profile/', views.profile, name="pro"),


]
