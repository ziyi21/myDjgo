from django.contrib import admin
from .models import Articles, Comments, BlogType


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Articles)
class AticleAdmin(admin.ModelAdmin):
    # 显示所有内容的列表，不需要点击详情页进行查找
    list_display = ('id', 'title', 'author', 'create_time', 'last_update_time')
    # 倒序排列
    # ordering = ("-id",)
    ordering = ("id",)


# admin.site.register(Articles, AticleAdmin)
# admin.site.register(Comments)
