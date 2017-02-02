from django.contrib import admin
from .models import *
from django.apps import apps
import MySQLdb
# Register your models here.

class TeachersView(admin.ModelAdmin):
	list_display	= ('teacher_name', 'teacher_dept')

class ClassesView(admin.ModelAdmin):
	list_display	= ('class_name', 'class_dept')

	def __init__(self, *args, **kwargs):
		super(ClassesView, self).__init__(*args, **kwargs)
		self.list_display_links = (None,)

class AttendenceView(admin.ModelAdmin):
    list_display    = ('stud_roll', 'stud_name','group_name_id','sem', 'subjects', 'attendence', 'total')

class SubjectView(admin.ModelAdmin):
    list_display    = ('class_for_id', 'semester','subject_1', 'subject_2', 'subject_3', 'subject_4', 'subject_5', 'subject_6')

app = apps.get_app_config('base')

for model_name, model in app.models.items():
    if model_name == 'classes':
    	admin.site.register(model, ClassesView)
    elif model_name == 'teachers':
    	admin.site.register(model, TeachersView)
    elif model_name == 'allsubjects':
        admin.site.register(model, SubjectView)
    elif 'attendence' in model_name:
    	admin.site.register(model, AttendenceView)
    else:
        admin.site.register(model)
