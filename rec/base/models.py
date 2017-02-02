from django.db import models

# Create your models here.


class Department(models.Model):
	department_id	= models.AutoField(primary_key=True)
	department_name	= models.CharField(max_length=100)

	class Meta:
		verbose_name_plural	= "Department List"

	def __unicode__(self):
		return self.department_name


class Teachers(models.Model):
	teacher_id		= models.AutoField(primary_key=True)
	teacher_name 	= models.CharField(max_length=255)
	teacher_dept 	= models.ForeignKey(Department)

	class Meta:
		verbose_name_plural	= "Teachers List"

	def __unicode__(self):
		return self.teacher_name

class Classes(models.Model):
	class_name		= models.CharField(max_length=100)
	class_dept		= models.ForeignKey(Department)

	class Meta:
		verbose_name_plural	= "Classes List"

	def __unicode__(self):
		return self.class_name