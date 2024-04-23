from django.contrib import admin
from demo_app.models import AppUser, Article

# Register your models here.

admin.site.register(AppUser)
admin.site.register(Article)
