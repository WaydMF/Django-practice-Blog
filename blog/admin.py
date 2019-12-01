from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('body', )


admin.site.register(Post, PostAdmin)
