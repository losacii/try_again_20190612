from django.contrib import admin
from django.urls import path
from . import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home),
    path('about/', homeViews.about),
]
