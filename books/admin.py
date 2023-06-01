from django.contrib import admin
from . import models
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "raiting", "year", "publisher", "genre", "get_tags")

    def get_tags(self, obj):
        tags = obj.tags.all()
        return "\n".join([t.title for t in tags])


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Movie)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Publisher)
