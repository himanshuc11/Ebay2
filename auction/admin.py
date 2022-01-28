from django.contrib import admin
from .models import Category, Items, Comment, Bid

# Register your models here.
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Comment)
admin.site.register(Bid)
