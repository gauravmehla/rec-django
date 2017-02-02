from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from base.models import *	# Importing all Models of `base` Class
import MySQLdb
# Create your views here.

def home(request):
	context = {
		'Message' : 'Welcome',
		'all_classes' : Classes.objects.all(),
	}
	return render(request, 'attendence_home.html', context)


def getdata(request):		
	db 		= MySQLdb.connect("localhost","root","root","rec_db")
	cursor	= db.cursor()
	try:
		selectedSem		= request.POST['selectedSem']
		selectedClass	= request.POST['selectedClass']
		sql 	= "SELECT * FROM base_allsubjects WHERE `semester` = '" + selectedSem + "' AND `class_for_id` = '" + selectedClass + "'"
		cursor.execute(sql)
		data = cursor.fetchall()
		db.commit()
	except:
		db.rollback()
	db.close

	all_groups = Groups.objects.all()
#	print all_groups
	return render_to_response('result.html', {'result' : data , 'groups' : all_groups})


def getattendence(request):		# Function to fetch the data from DB
	db 		= MySQLdb.connect("localhost","root","root","rec_db")
	cursor	= db.cursor()
	try:
		selectedSem		= request.POST['selectedSem']
		selectedClass	= request.POST['selectedClass']
		selectedSubject	= request.POST['selectedSubject']
		selectedGroup	= request.POST['selectedGroup']
		thisclass 		= Classes.objects.get(id=selectedClass)
		thisGroup		= Groups.objects.get(group_name=selectedGroup)
		# DB
#		print selectedSem
		sql 	= "SELECT * FROM `base_"+ thisclass.class_name + "_attendence` WHERE `group_name_id` = '"+ str(thisGroup.id) +"' AND `sem`='" + selectedSem +"'"
		cursor.execute(sql)
		data = cursor.fetchall()
		if data == None:
			print 'abc'
		db.commit()
	except:
		db.rollback()
	db.close
	list_subject = AllSubjects.objects.get(semester=selectedSem, class_for_id=selectedClass)
	subject_array = [ 
					  list_subject.subject_1,
					  list_subject.subject_2,
					  list_subject.subject_3,
					  list_subject.subject_4,
					  list_subject.subject_5,
					  list_subject.subject_6,
					]
	index 					= subject_array.index(selectedSubject)
	attendence_list 		= []
	total_attendence_list 	= []



#----------------------------------------------------------------------------
	#### C A U T I O N 														#
	for each in data:														#
		attendence = each[5].split('|')										#
		for index_att, att in enumerate(attendence):						#
			if index_att==index:											#
				attendence_list.append(attendence[index_att])				#
																			#
																			#
																			#
		total_attendence = each[6].split('|')								#
		for index_att, att in enumerate(total_attendence):					#
			if index_att==index:											#
				total_attendence_list.append(total_attendence[index_att])	#
	#### C A U T I O N 														#
#----------------------------------------------------------------------------



	all_list = zip(data, attendence_list, total_attendence_list)
	return render_to_response('attendence_table_view.html', {'selectedClass': selectedClass,
															 'selectedSem'	: selectedSem,
															 'selectedSubject' : selectedSubject,
															 'index'		:	index,
															 'all_list'		: all_list,
															}, context_instance=RequestContext(request))

def saveattendence(request):
	selectedClass	= request.POST['selectedClass']
	selectedSubject	= request.POST['selectedSubject']
	selectedSem		= request.POST['selectedSem']
	index 			= request.POST['index']
	checkedValues	= request.POST.getlist('checkedValues[]')
	thisGroup		= Groups.objects.get(group_name=request.POST['selectedGroup'])
#	print thisGroup
	classSelected 	= Classes.objects.get(id=selectedClass)

	list_subject = AllSubjects.objects.get(semester=selectedSem, class_for_id=selectedClass)
	subject_array = [ 
					  list_subject.subject_1,
					  list_subject.subject_2,
					  list_subject.subject_3,
					  list_subject.subject_4,
					  list_subject.subject_5,
					  list_subject.subject_6,
					]
	subjects 				= '|'.join(subject_array)
#	print subjects

	try:
		# DB
		db 		= MySQLdb.connect("localhost","root","root","rec_db")
		cursor	= db.cursor()
		sql 	= "SELECT * FROM `base_"+ classSelected.class_name + "_attendence` WHERE `group_name_id` = '"+ str(thisGroup.id) +"' AND `sem`='" + selectedSem + "'"
		cursor.execute(sql)
		data = cursor.fetchall()
		db.commit()
	except:
		db.rollback()

	global total

#------------------------------------------------------------------------------------------------------------
	# C A U T I O N 																						#
																											#
	for student, checked in zip(data, checkedValues):														#
		student = list(student)																				#
#		print student 																						#
		if checked[0]=='P':																					#
																											#
			present_Student	= student[1]																	#
#			print present_Student																			#
																											#
			student_total_attendence = student[6].split('|')			# Increment in Total Attendence		#
			incremented = int(student_total_attendence[int(index)]) + 1										#
			student_total_attendence[int(index)] = str(incremented)											#
			student[6] 	=  '|'.join(student_total_attendence)												#
			total = student[6]																				#
																											#
			student_attendence 	= student[5].split('|')					# Increment in Present Attendence	#
			incremented = int(student_attendence[int(index)]) + 1											#
			student_attendence[int(index)] 	= str(incremented)												#
			student[5] 	= '|'.join(student_attendence)														#
																											#
			sql = "UPDATE base_"+ str(classSelected.class_name) + "_attendence SET attendence = '"\
					 + str(student[5]) + "' , subjects = '"+ subjects +"' WHERE stud_roll = '" + \
					 str(present_Student) + "' AND `sem`='" + selectedSem + "'"								#
			cursor.execute(sql)																				#
			db.commit()																						#
																											#
		else:																								#
			student_total_attendence = student[6].split('|')												#
			incremented = int(student_total_attendence[int(index)]) + 1										#
			student_total_attendence[int(index)] = str(incremented)											#
			student[6] 	=  '|'.join(student_total_attendence)												#
			total = student[6]																				#
																											#
	sql = "UPDATE base_"+ str(classSelected.class_name) + "_attendence SET total = '"\
				+ str(total) + "' WHERE `group_name_id` = '"+ str(thisGroup.id) \
				+"'AND `sem`='" + selectedSem + "'" 														#
	cursor.execute(sql)																						#
	db.commit()																								#
	db.close()																								#
																											#
	# C A U T I O N 																						#
#------------------------------------------------------------------------------------------------------------
 	return getattendence(request)
	

