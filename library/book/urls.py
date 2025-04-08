from django.urls import path
from .views import index, single_book

app_name = "book"
urlpatterns = [
    path("", index, name="index"),
    path("<int:book_id>", single_book, name="single_book"),
]
