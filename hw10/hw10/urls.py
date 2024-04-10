from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    #під'єднуємо урли цитат
    path("", include("quotes.urls")),
    path("authors/", include("authors.urls")),    
    path("users/", include("users.urls"))   
]
