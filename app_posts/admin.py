from django.contrib import admin
from . import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_tags", "category", "description", "created_date", "category_post")

    def get_tags(self, obj):
        tags = obj.tags.all()
        return "\n".join([t.title for t in tags])


admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.CategoryPost)
