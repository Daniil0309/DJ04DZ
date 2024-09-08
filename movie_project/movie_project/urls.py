from django.contrib import admin
from django.urls import path, include
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),
    path('', views.list_films, name='home'),
]
