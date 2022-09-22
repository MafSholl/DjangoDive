from rest_framework import serializers

from second_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):  # noqa
    # title = serializers.charField(max_length = 255) etc.
    book_genre = serializers.CharField(max_length=255, source='title')
    # publisher = PublisherSerializer()
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='second_app:publisher-detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'price', 'book_genre', 'publisher']
        # exclude = ['price']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
