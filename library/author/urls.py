from django.urls import path
from .views import index, single_author, delete_author

app_name = 'author'

urlpatterns = [
    path('', index, name='index'),
    path('<int:author_id>/', single_author, name='single_author'),
    path('delete/<int:author_id>/', delete_author, name='delete_author'),
]
