from django.urls import path
from .api_views import AuthorListCreateAPI, AuthorRetrieveUpdateDestroyAPI

app_name = "api_author"
urlpatterns = [
    path('', AuthorListCreateAPI.as_view(), name='api_author_list'),
    path('<int:pk>/', AuthorRetrieveUpdateDestroyAPI.as_view(), name='api_author_detail'),
]
