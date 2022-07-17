from django.contrib import admin

from .models import Diary

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'body')


admin.site.register(Diary,DiaryAdmin)