$(document).ready(function(){

	$('.allPresnt').hide();

	$('#class-select').change(function(){
		var class_value 	= $('#class-select option:selected').val();
		var sem_value		= $('#semester-select option:selected').val();
		if (class_value != '' && sem_value != ''){
			return selectClass(class_value, sem_value);
		}
		else{
			if (class_value == ''){
				alert('Please Select a Class.');
				$('#result').empty();
				$('#attendence-wrapper').empty();
			}
		}
	});

	$('#semester-select').change(function(){
		var class_value 	= $('#class-select option:selected').val();
		var sem_value		= $('#semester-select option:selected').val();
		return selectClass(class_value, sem_value);
	});

	function selectClass (class_value, sem_value){
		$.ajax({
			type	: 'POST',
			url		: '/attendence/getdata/',
			data	: {
						'selectedClass'	: class_value,
						'selectedSem'	: sem_value,
					 },
			success : function(result){
				$('#result').html(result);
				$('#attendence-wrapper').empty();
			},
			headers	: {
				'X-CSRFtoken'	: csrftoken
			}
		});
		return false;
	}


	function getCookie(name){
		var cookieValue = null;
		if(document.cookie && document.cookie != ''){
			var cookies = document.cookie.split(';');
			for(var i=0; i< cookies.length; i++){
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')){
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken')

});

function saveAttendence(){
	var checkedValues = $('input:radio:checked').map(function() { 	return this.value;	}).get();
	var class_value 	= $('#class-select option:selected').val();
	var sem_value		= $('#semester-select option:selected').val();
	var subject_value	= $('#subject-select option:selected').val();
	var index 			= $('#index').val();
	var group_value		= $('#group-select option:selected').val();
	$.ajax({
			type	: 'POST',
			url		: '/attendence/saveattendence/',
			data	: {
						'selectedClass'		: class_value,
						'selectedSem'		: sem_value,
						'selectedSubject'	: subject_value,
						'checkedValues'		: checkedValues,
						'index' 			: index,
						'selectedGroup'		: group_value,
					 },
			success : function(result){
				$('#attendence-wrapper').html(result);
			},
			headers	: {
				'X-CSRFtoken'	: csrftoken
			}
		});
		return false;
}

function getAttendence() {
		var class_value 	= $('#class-select option:selected').val();
		var sem_value		= $('#semester-select option:selected').val();
		var subject_value	= $('#subject-select option:selected').val();
		var group_value		= $('#group-select option:selected').val();
		$.ajax({
			type	: 'POST',
			url		: '/attendence/getattendence/',
			data	: {
						'selectedClass'		: class_value,
						'selectedSem'		: sem_value,
						'selectedSubject'	: subject_value,
						'selectedGroup'		: group_value,
					 },
			success : function(result){
				$('#attendence-wrapper').html(result);
			},
			headers	: {
				'X-CSRFtoken'	: csrftoken
			}
		});
		return false;
	}

function getCookie(name){
		var cookieValue = null;
		if(document.cookie && document.cookie != ''){
			var cookies = document.cookie.split(';');
			for(var i=0; i< cookies.length; i++){
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')){
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

var csrftoken = getCookie('csrftoken')


function Absent(){
	$(':input[class="present"]').each(function(){
		$('.absent').prop('checked',true);
	});
}

function Present(){
	$(':input[class="absent"]').each(function(){
		$('.present').prop('checked',true);
	});
}
