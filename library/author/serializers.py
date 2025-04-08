from rest_framework import serializers
from .models import Author
from book.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Book.objects.all(),
                                               required=False)  # It is possible not to send books, but we can send a list of IDs if it's needed

    class Meta:
        model = Author
        fields = '__all__'
