from django.contrib import admin
from .models import Post, Category, Tag, Comment


class CategoryPostInline(admin.TabularInline):
	model = Post
	extra = 1


class AdminCategory(admin.ModelAdmin):
	list_filter = ('date_created',)
	list_display = ('title', 'date_created')
	date_hierarchy = ('date_created',)
	search_fields = ('title',)
	inlines = [CategoryPostInline]


admin.site.register(Category, AdminCategory)


class AdminPost(admin.ModelAdmin):
	search_fields = ('title',)
	date_hierarchy = ('date_created',)
	filter_horizontal = ('tags',)
	list_filter = ('title', 'category', 'date_created',)
	list_display_links = ['title', 'category', 'date_created']
	list_display = ('title', 'category', 'date_created')


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
	search_fields = ['post__title', 'title']
	raw_id_fields = ('post',)
	list_display = ['title', 'email', 'content', 'status', 'post']
	list_filter = ['status', 'post',]


admin.site.register(Comment, AdminComment)


class AdminTag(admin.ModelAdmin):
	search_fields = ['title']
	raw_id_fields = ('post',)
	list_display = ['title', 'date_created']
	list_filter = ['date_created',]


admin.site.register(Tag, AdminTag)
