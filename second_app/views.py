from _testcapi import raise_exception

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

import serializers
from .models import Book
from serializers import BookSerializer, PublisherSerializer, BookCreateSerializer

# Create your views here.
from second_app.models import Book, Publisher


def index(request):
    context = [8, 4, 1]
    return render(request, 'second_app/index.html', context={"obj": context, "name": "Shola", 'is_major': True})


def redirect(request):
    return HttpResponseRedirect(reverse('second_app:index'))


def about(request):
    return render(request, 'second_app/about.html')


# def book_list(request):
#     books = Book.objects.all()
# books = Book.objects.filter(genre='TRAGEDY')
# books = Book.objects.filter(price__gt=50.00)
# books = Book.objects.filter(publisher_id__in=(1, 7, 3)).order_by('-title', 'price').reverse()
# # values and only does same job. However values return a dictionary
# books = Book.objects.filter(publisher_id__in=(1, 7, 3)).values('-title', 'price')
# #While only returns the object itself
# books = Book.objects.filter(publisher_id__in=(1, 7, 3)).only('-title', 'price')
# # You do not want to do a query of another fetch-by e.g genre on this method in our FE (i.e say book.genre)
# books = Book.objects.filter(publisher_id__in=(1, 7, 3)).only('-title', 'price')
# # Since publisher is a foreign key in book object, we can force the query to select related (attribute) object i.e eagerly resolve
# books = Book.objects.select_related().all('publisher')
# books = Book.objects.raw("Select * from second_app_book")

# #if you want to use the d-base itself and not the manager object, see below
# cursor = connection.cursor()
# result = cursor.execute("select * from second_app_book")
# books = result.fetchall()
# cursor.close()

# return render(request, 'second_app/book-list.html', {'books': books})


# def book_details(request, pk):
# try:
#     book = Book.objects.get(pk=pk)
#     return render(request, 'second_app/book-detail.html', {'book': book})
# except Book.DoesNotExist:
#     return HttpResponse("E no dey")
# book = get_object_or_404(Book, pk=pk)
# return render(request, 'second_app/book-detail.html', {'book': book})


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_details(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book, context={'request': request})
#         return Response(serializer)
#     elif request.method in ('PUT', 'PATCH'):
#         serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
#         serializer.is_valid(raise_exception == True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Publisher.objects.all()
#         serializer = PublisherSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def publisher_detail(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == 'GET':
#         serializer = PublisherSerializer(publisher, context={'request': request})
#         return Response(serializer)
#     elif request.method in ('PUT', 'PATCH'):
#         serializer = BookSerializer(publisher, data=request.data, partial=True, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request': self.request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status.HTTP_201_CREATED)
#
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, context={'request': request})
#         return Response(serializer)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
#         serializer.is_valid(raise_exception == True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
class BookList(ListCreateAPIView):
    queryset = Book.objects.all()

    # what if I want to tweak my serializer up to return a particular serializer, though i inherited it from django
    # ListCreateApi
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        else:
            return BookCreateSerializer

    serializer_class = BookSerializer()

    #
    def get_serializer_context(self):
        return {'request': self.request}


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This next one will create all the HttpMethods for us
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.get.all()
#     serializer_class = BookSerializer
