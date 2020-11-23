from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "posts_count")

    exclude = ("posts",)

    def posts_count(self, obj):
        return str(obj.posts.count()) + " posts"


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author")
    inlines = [
        CategoryInLine,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
