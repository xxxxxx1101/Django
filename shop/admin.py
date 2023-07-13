from django.contrib import admin
from .models import Author, Book, CategoryMovie, Movie, User


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'date_birthday', 'date_of_death', 'description', )
    search_fields = ('first_name','last_name',)
    list_display_links = ('id','first_name')

    

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','author','publication_date','in_stock',)
    list_filter = ('in_stock','publication_date','author',)
    search_fields = ('id','name',)
    list_display_links = ('id','author',)
    list_editable = ('in_stock','name',)
    # autocomplete_fields = ('author',)


class CategoryMovieAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    search_fields = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'year_release', 'company', 'time', 'budget', 'description','image', )
    list_filter = ('category','company',)
    search_fields=('name',)
    list_display_links = ('id','name',)
    autocomplete_fields = ('category',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'login', 'email', 'create', )

# admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(CategoryMovie,CategoryMovieAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(User,UserAdmin)


