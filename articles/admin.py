from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(VersionAdmin):
    pass