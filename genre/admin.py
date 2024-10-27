from django.contrib import admin
from .models import Collection,Piece,UserProfile

# Register your models here.

admin.site.register(Collection)
admin.site.register(Piece)
admin.site.register(UserProfile)