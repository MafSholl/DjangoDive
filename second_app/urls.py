from django.urls import path
from . import views

app_name = 'second_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.redirect),
    path('redirect/', views.redirect),
    path('about/', views.about, name='about'),
    # path('book-list/', views.book_list),
    # path('book-detail/<int:pk>/', views.book_details),

    # path('books/', views.book_list, name='book-list'),
    path('books/', views.BookList.as_view(), name='book-list'),
    # path('books/<int:pk>/', views.book_details, name='book-details'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-details'),
    # path('publishers/', views.publisher_list, name="publisher-list"),
    # path('publishers/<int:pk>', views.publisher_detail, name="publisher-detail")

]
