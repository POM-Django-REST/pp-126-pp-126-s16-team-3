from rest_framework import serializers
from .models import Book

from author.serializers import AuthorSerializer
from author.models import Author


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    authors_ids = serializers.PrimaryKeyRelatedField(many=True,
                                                     queryset=Author.objects.all(),
                                                     write_only=True,
                                                     source='authors'
                                                     )

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count', 'authors', 'authors_ids']

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        book.authors.set(authors)
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if authors is not None:
            instance.authors.set(authors)
        instance.save()
        return instance
