from django.contrib import admin
from .models import Post,Exp

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status', 'created_on')
	list_filter = ("status",)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class ExpAdmin(admin.ModelAdmin):
	list_display = ('company', 'slug', 'status', 'created_on')
	list_filter = ("status",)
	search_fields = ['company', 'content']
	prepopulated_fields = {'slug': ('company',)}

admin.site.register(Exp, ExpAdmin)

# Register your models here.
