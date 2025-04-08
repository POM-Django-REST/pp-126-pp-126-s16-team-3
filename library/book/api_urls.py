from django.urls import path
from .api_views import BookListCreateAPI, BookRetrieveUpdateDestroyAPI

app_name = "api_book"
urlpatterns = [
    path("", BookListCreateAPI.as_view(), name="api_book_list"),
    path("<int:pk>/", BookRetrieveUpdateDestroyAPI.as_view(), name="api_book_detail"),
]
