from django.contrib import admin
from .models import Course, Avaliable

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'url', 'created', 'updated', 'active')

@admin.register(Avaliable)

class AvaliableAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'avaliable', 'created', 'updated', 'active')
