<<<<<<< HEAD
from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(VersionAdmin):
=======
from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(VersionAdmin):
>>>>>>> 40a0b34 (update- adding the desktop app)
    pass