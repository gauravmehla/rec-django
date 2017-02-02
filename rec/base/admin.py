from django.contrib import admin
from .models import *
# Register your models here.

class TeachersView(admin.ModelAdmin):
	list_display	= ('teacher_name', 'teacher_dept')

class ClassesView(admin.ModelAdmin):
	list_display	= ('class_name', 'class_dept')

admin.site.register(Department)
admin.site.register(Teachers, TeachersView)
admin.site.register(Classes, ClassesView)
admin.site.site_header = 'R.E.C Administration'