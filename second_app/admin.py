from django.contrib import admin
from second_app.models import Book, Publisher
# Register your models here.

# admin.site.register(Book)
admin.site.register(Publisher)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']
    # fields = ['title', 'isbn']
    # fieldsets =



