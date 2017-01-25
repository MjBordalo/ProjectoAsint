$(document).ready(function(){

var added_rooms=[];
// ACESS FENIX API AND GET ALL PREVIOUS SAVED ROOMS //
var url="http://localhost:8080/roistapi/registered/rooms";
var request = new XMLHttpRequest();
request.open("GET",url);
request.send(null);
request.onreadystatechange = function()
{
	if (request.readyState == 4 && request.status == 200){
		dataIn = JSON.parse(request.responseText);
		if (dataIn.Success == true)
			added_rooms=dataIn.Rooms_names;
			list(added_rooms,"available_rooms",1);
}
}





var buildings_identifiers;
var campus_choosen;

$("#campus").change(function() {
	var parent = $(this).val();

	if(parent=="--Select--"){
		campus_choosen=null;
	}else{
		campus_choosen=parent;
		var index=$('option:selected',this).index();
		var aux_id = campus_id[index-1];
		// ACESS FENIX API AND GET CAMPUS OPTIONS //
		var url="http://localhost:8080/roistapi/fenix/buildings/"+aux_id;
		var request = new XMLHttpRequest();
		request.open("GET",url);
		request.send(null);
		request.onreadystatechange = function()
		{
			if (request.readyState == 4 && request.status == 200){
		    	dataIn = JSON.parse(request.responseText);
		    	if (dataIn.Success == true){
				}
					buildings_identifiers=dataIn.buildings_id;
		    		list(dataIn.buildings_name,"buildings");
		    	}else{
					//default child option is blank
					$("#buildings").html('');
				}
		}
	}
});


var floors_identifers;
var building_choosen;
$("#buildings").change(function() {
	var parent = $(this).val();

	if(parent=="--Select--"){
		building_choosen=null;
	}else{
		building_choosen=parent;
		var index1=$('option:selected',this).index();
		var aux_id1 = buildings_identifiers[index1-1];
		// ACESS FENIX API AND GET CAMPUS OPTIONS //
		var url="http://localhost:8080/roistapi/fenix/floors/"+aux_id1;
		var request = new XMLHttpRequest();
		request.open("GET",url);
		request.send(null)
		request.onreadystatechange = function()
	    {
	    	if (request.readyState == 4 && request.status == 200){
		    	dataIn = JSON.parse(request.responseText);
		    	if (dataIn.Success == true){
				}
					floors_identifers=dataIn.floors_id;
		    		list(dataIn.floors_name,"floors");
		    	}else{
					//default child option is blank
					$("#floors").html('');
				}
		}
	}
});
var floor_choosen;
$("#floors").change(function() {
	var parent = $(this).val();
	if(parent=="--Select--" ){
		floor_choosen=null;
	}else{
		floor_choosen=parent;
		var index=$('option:selected',this).index();
		var aux_id = floors_identifers[index-1];
		// ACESS FENIX API AND GET CAMPUS OPTIONS //
		var url="http://localhost:8080/roistapi/fenix/rooms/"+aux_id;
		var request = new XMLHttpRequest();
		request.open("GET",url);
		request.send(null)
		request.onreadystatechange = function()
		{
			if (request.readyState == 4 && request.status == 200){
		    	dataIn = JSON.parse(request.responseText);
		    	if (dataIn.Success == true){
				}
		    		list(dataIn.rooms_names,"rooms");
		    	}else{
					//default child option is blank
					$("#rooms").html('');
				}
		}
	}
});
var room_choosen;
var complete_room_name;

$("#rooms").change(function() {
	var parent = $(this).val();
	if(parent=="--Select--")
		room_choosen=null;
	else
		//CREATE ARRAY WITH COMPLETE ROOM NAME TO CHECK OCCUPANCY
		room_choosen=campus_choosen+'/'+building_choosen+'/'+floor_choosen+'/'+parent;
});

//REFRSH PAGE TO UPDATE ONLY THE OCCUPANCY OF THE SELECTED ROOM!
$("#button_refresh").click(function(){

	var parent = $("#available_rooms").val();
	if(parent=="--View--"){
		$('#occupancy').val("")
	}else{
			var url="http://localhost:8080/roistapi/uname/0/room/"+parent;
			var request = new XMLHttpRequest();
			request.open("GET",url);
			request.send(null)
			request.onreadystatechange = function()
			{
				if (request.readyState == 4 && request.status == 200){
					dataIn = JSON.parse(request.responseText);
					 $('#occupancy').val(dataIn.Students.length);

				}
			}
	}
});


//EVENT BASED (NOT REALLY NEEDED FOR HIGH ENOUGH SAMPLING FREQUENCY!)
$("#available_rooms").change(function() {

	var parent = $(this).val();
	if(parent=="--View--"){
		$('#occupancy').val("")
	}else{
			var url="http://localhost:8080/roistapi/uname/0/room/"+parent;
			var request = new XMLHttpRequest();
			request.open("GET",url);
			request.send(null)
			request.onreadystatechange = function()
			{
				if (request.readyState == 4 && request.status == 200){
					dataIn = JSON.parse(request.responseText);
					 $('#occupancy').val(dataIn.Students.length);

				}
			}
	}
});


// VERSION THAT UPDATES THE OCCUPANCY IN A GIVEN TIME PERIOD. NEEDED SINCE
// IF WE USE A DROP DOWN LSIT THE CURRENT OPTION ONLY BE UPDATED IF
// THE USER DOES CHANGES OPTIONS
/*setInterval(function () {
	var parent = $("#available_rooms").val();
	if(parent=="--View--"){
		$('#occupancy').val("")
	}else{
			var url="http://localhost:8080/roistapi/uname/0/room/"+parent;
			var request = new XMLHttpRequest();
			request.open("GET",url);
			request.send(null)
			request.onreadystatechange = function()
			{
				if (request.readyState == 4 && request.status == 200){
					dataIn = JSON.parse(request.responseText);
					 $('#occupancy').val(dataIn.Students.length);

				}
			}
		}
	}, 1000);*/









$("#button_remove").click(function() {

	var tmp = confirm("Would you like remove this Room?");
	if (tmp==true){
		var parent = $('#available_rooms').val();
		if(parent==null){
			alert("There is no room for you to delete. Sorry");
		}else{
		// ACESS FENIX API, DELECT SELECTED ROOM AND DELETE THIS ROOM
		// TO GLOBAL VARIABLE OF EXISTING ROOMS
		var url='http://localhost:8080/roistapi/uname/0/room/'+parent;
		var request = new XMLHttpRequest();
		request.open("DELETE",url);
		//request.setRequestHeader("Content-type", "application/json");
		//dataOut=JSON.stringify({});
		//request.send(dataOut);
		request.send(null)
		request.onreadystatechange = function(){
			 if (request.readyState == 4 && request.status == 200){
		    	var dataIn = JSON.parse(request.responseText);
		    	if (dataIn.Success==false){
		    	var resString="room:  "+parent+" not delete. Please check if this room exists..";
		    	alert(resString);
			}else  {
				var index_delete = added_rooms.indexOf(parent);
				added_rooms.splice(index_delete, 1);

				$("#available_rooms").val("--View--");

				list(added_rooms,"available_rooms",1);
					}

				}
			}
		}
	}

});


$("#button1").click(function() {

	var tmp = confirm("Would you like add this Room?");
	if (tmp==true){
		//CATCH A INVALID ROOM
		if (room_choosen == null || campus_choosen==null || building_choosen==null || floor_choosen==null){
			alert("Please pick a valid Campus, Building, Floor and Room.");
		}else{

			// ACESS FENIX API, CREATE SELECT ROOM AND ADDED THIS ROOM
			// TO GLOBAL VARIABLE OF EXISTING ROOMS
			var url='http://localhost:8080/roistapi/uname/'+'0/room/'+room_choosen;
			var request = new XMLHttpRequest();
			request.open("POST",url);
			request.setRequestHeader("Content-type", "application/json");
			dataOut=JSON.stringify({});
			request.send(dataOut);
			request.onreadystatechange = function(){
				 if (request.readyState == 4 && request.status == 200){
			    	var dataIn = JSON.parse(request.responseText);
			    	if (dataIn.Success==false){
			    	var resString="room:  "+room_choosen+" not added. Please check if this room is already available..";
			    	alert(resString);
				}else  {

					$("#available_rooms").val("--View--");

					added_rooms.push(room_choosen);
					list(added_rooms,"available_rooms",1);
						}

					}
				}
		}
	}
});


				function list(array_list,identifier_next="",aux=0)
				{
					if(identifier_next!="" ){
						$("#"+identifier_next).html(""); //reset child options
						if(aux==0){
							$("#"+identifier_next).append("<option>"+"--Select--"+"</option>");
						}else{
							$("#"+identifier_next).append("<option>"+"--View--"+"</option>");
							$('#occupancy').val("")
						}$(array_list).each(function (i) { //populate child options
						$("#"+identifier_next).append("<option>"+array_list[i]+"</option>");
						});
					}
				}
});
