from django.db import models
import MySQLdb
import os
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
	class_name		= models.CharField(max_length=100, unique=True)
	class_dept		= models.ForeignKey(Department)

	class Meta:
		verbose_name_plural	= "Classes List"

	def __unicode__(self):
		return self.class_name

	def save(self, *args, **kwargs):
		# Create Tables into Database
		db 		= MySQLdb.connect("localhost","root","root","rec_db")
		cursor	= db.cursor()
		try:
			sql 	= 'CREATE TABLE base_' + self.class_name +'_attendence (id integer AUTO_INCREMENT NOT NULL PRIMARY KEY, stud_roll integer NOT NULL, stud_name varchar(100) NOT NULL, sem varchar(30), subjects varchar(100) , attendence varchar(100), total varchar(100) ,  email_id varchar(100) NOT NULL, phone_no varchar(100) NOT NULL, group_name_id varchar(30))'
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
		db.close

		#Create Modules in the Models.py
		BASE_DIR 		= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		BASE_MODELS_FILE= BASE_DIR + '/base/models.py'
		write_module	= open(BASE_MODELS_FILE, 'a+')
		write_module.writelines(['\n#'+self.class_name+'_START', '\n'])
		write_module.writelines(['\nclass ' + self.class_name + '_attendence(models.Model):\n', '\tstud_roll = models.IntegerField(unique=True)\n','\tstud_name = models.CharField(max_length=100)\n','\tgroup_name = models.ForeignKey(Groups)\n\n','\tsem_choices=(("First_Sem","1st"),("Second_Sem","2nd"),("Third_Sem","3rd"),("Fourth_Sem","4th"),("Fifth_Sem","5th"),("Sixth_Sem","6th"),("Seventh_Sem","7th"),("Eighth_Sem","8th"))\n','\tsem = models.CharField(max_length=30, choices=sem_choices, blank=True)\n\n','\tsubjects = models.CharField(max_length=100, blank=True)\n\n','\tattendence = models.CharField(max_length=100, blank=True, default="0|0|0|0|0|0")\n\n','\ttotal = models.CharField(max_length=100, blank=True, default="0|0|0|0|0|0")\n\n','\temail_id = models.CharField(max_length=100, blank=True)\n','\tphone_no = models.CharField(max_length=100, blank=True)\n\n','\tdef __unicode__(self):\n','\t\treturn self.stud_name\n\n','\tclass Meta:\n','\t\tverbose_name_plural = "' + self.class_name.upper() + '_attendence"\n'])
		write_module.writelines(['\n\tdef save(self, *args, **kwargs):\n','\t\tdb 		= MySQLdb.connect("localhost","root","root","rec_db")\n','\t\tcursor	= db.cursor()\n'])
		
		# For 1st Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'First_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 2nd Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Second_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 3rd Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Third_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 4th Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Fourth_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 5th Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Fifth_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 6th Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Sixth_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 7th Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Seventh_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])
		
		# For 8th Sem
		write_module.writelines(['\t\tsql = "INSERT INTO `base_'+self.class_name+'_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES (\'" + str(self.stud_roll) + "\',\'" + self.stud_name + "\', \'Eighth_Sem\',\'" + self.attendence +"\',\'" + self.total +"\',\'" + self.email_id + "\',\'"+ self.phone_no +"\',\'" + str(self.group_name.id) + "\')"','\n'])
		write_module.writelines(['\t\tcursor.execute(sql)\n','\t\tdb.commit()\n'])

		write_module.writelines(['\n#'+self.class_name+'_END', '\n']) 
		write_module.close()
		
		super(Classes, self).save(*args, **kwargs)

class AllSubjects(models.Model):
	sem = (
			('First_Sem'   , '1st'),
			('Second_Sem'  , '2nd'),
			('Third_Sem'	, '3rd'),
			('Fourth_Sem'  , '4th'),
			('Fifth_Sem'   , '5th'),
			('Sixth_Sem' 	, '6th'),
			('Seventh_Sem' , '7th'),
			('Eighth_Sem'  , '8th'),
		)
	class_for	= models.ForeignKey(Classes)
	semester	= models.CharField(max_length=100, choices=sem)
	subject_1 	= models.CharField(max_length=100, blank=True)
	subject_2 	= models.CharField(max_length=100, blank=True)
	subject_3 	= models.CharField(max_length=100, blank=True)
	subject_4 	= models.CharField(max_length=100, blank=True)
	subject_5 	= models.CharField(max_length=100, blank=True)
	subject_6 	= models.CharField(max_length=100, blank=True)

	class Meta:
		verbose_name_plural	= "All Subjects List"

	def __unicode__(self):
		return self.semester

class Groups(models.Model):
	group_name		= models.CharField(max_length=30)
	group_dept		= models.ForeignKey(Department)

	class Meta:
		verbose_name_plural	= "Groups List"

	def __unicode__(self):
		return self.group_name



#############################################
#											#
#	A U T O   G E N E R A T I N G  C O D E	#
#											#
#############################################


#CSE2016_START

class CSE2016_attendence(models.Model):
	stud_roll = models.IntegerField(unique=True)
	stud_name = models.CharField(max_length=100)
	group_name = models.ForeignKey(Groups)

	sem_choices=(("First_Sem","1st"),("Second_Sem","2nd"),("Third_Sem","3rd"),("Fourth_Sem","4th"),("Fifth_Sem","5th"),("Sixth_Sem","6th"),("Seventh_Sem","7th"),("Eighth_Sem","8th"))
	sem = models.CharField(max_length=30, choices=sem_choices, blank=True)

	subjects = models.CharField(max_length=100, blank=True)

	attendence = models.CharField(max_length=100, blank=True, default="0|0|0|0|0|0")

	total = models.CharField(max_length=100, blank=True, default="0|0|0|0|0|0")

	email_id = models.CharField(max_length=100, blank=True)
	phone_no = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.stud_name

	class Meta:
		verbose_name_plural = "CSE2016_attendence"

	def save(self, *args, **kwargs):
		db 		= MySQLdb.connect("localhost","root","root","rec_db")
		cursor	= db.cursor()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'First_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Second_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Third_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Fourth_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Fifth_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Sixth_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Seventh_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()
		sql = "INSERT INTO `base_CSE2016_attendence` (`stud_roll`,`stud_name`,`sem`,`attendence`,`total`,`email_id`,`phone_no`,`group_name_id`) VALUES ('" + str(self.stud_roll) + "','" + self.stud_name + "', 'Eighth_Sem','" + self.attendence +"','" + self.total +"','" + self.email_id + "','"+ self.phone_no +"','" + str(self.group_name.id) + "')"
		cursor.execute(sql)
		db.commit()

#CSE2016_END
