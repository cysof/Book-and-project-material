from webbrowser import register

from books.models import Book, Review
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    
    
    
class ReviewInline(admin.TabularInline):
    model = Review
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Review)