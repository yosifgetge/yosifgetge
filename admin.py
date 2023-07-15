from django.contrib import admin
from .models import Login
class LoginsAdmin(admin.ModelAdmin):
     list_display = ['username','password','Active']
     list_display_links = ['password']
     list_editable = ['username','Active']
     search_fields = ['username']
     list_filter = ['Active']
admin.site.register(Login,LoginsAdmin)