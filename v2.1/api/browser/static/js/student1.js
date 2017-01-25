// GLOBAL VARIABLES
var server = 'localhost'
var port = 8080
var tmp=window.location.href.split('/')
var uname_id=tmp[tmp.length-1];
var start=true;
var Rooms=["","","",""];
var int2room=["campus","building","floor","name","stud"]

/////////////// INITIALIZATION ///////////////
///// SHOW AVAILABLE ROOMS /////
function initAvabRooms(){
	if (start=true){
		retrieveAvabRooms();
		start=false;
	}
}

///// HEADERS /////
function initRoomString(room_id){
	var tmp=room_id.replace(/\//g,' ');
	console.log(tmp);
	if (tmp=="-1")
		var htmlString="<i><b>Status:</b> You are not Checked-In in any Room.</i>";
	else
		var htmlString="<i><b>Status:</b>  You are currently Ckecked-In in at "+tmp+"</i>";

	var loc=document.getElementById('roomtag');
	loc.insertAdjacentHTML('beforeend',htmlString);
}

///// CHECK OUT BUTTON /////
function ProcessCheckOut(){
	var tmp = confirm("Would you like to Check-Out from this Room?");
	if (tmp==true)
		checkOutStud(uname_id)
}

///// CHECK OUT BUTTON /////
function ProcessCheckIn(){
	var tmp = confirm("Would you like to Check-In at this Room?");
	if (tmp==true)
		checkInStud(uname_id,Rooms[0],Rooms[1],Rooms[2],Rooms[3])
}

///// REFRESH BUTTON /////
function ProcessRefresh(){
	removeHtml("");
	retrieveAvabRooms();
}

///////////// BODY ///////////////


///// UPADTE SHOW AVAILABLE ROOMS /////
function refreshAvabRooms(elem){
	var val=document.getElementById(elem).value;
	console.log(Rooms);
	console.log(val);
	removeHtml(elem);
	if (elem=="campus")
		retrieveAvabRooms(val)
	else if (elem=="building")
		retrieveAvabRooms(Rooms[0],val)
	else if (elem=="floor")
		retrieveAvabRooms(Rooms[0],Rooms[1],val)
	else
		retrieveAvabRooms(Rooms[0],Rooms[1],Rooms[2],val)
}

/////////////// AUXILIAR FUNCTIONS ///////////////
function removeHtml(elem){
    var i;
    if (elem==""){
    	var loc=document.getElementById("campus");
    	loc.innerHTML="";
		removeHtml("campus");
    }
    else if (elem=="campus"){
    	var loc=document.getElementById("building");
    	loc.innerHTML="";
		removeHtml("building");
    }
	else if (elem=="building"){
    	var loc=document.getElementById("floor");
    	loc.innerHTML="";
		removeHtml("floor");
	}
	else if (elem=="floor"){
    	var loc=document.getElementById("name");
    	loc.innerHTML="";
		removeHtml("name");
	}
	else if (elem=="name"){
    	var loc=document.getElementById("stud");
    	loc.innerHTML="";
    }
}

/////////////// REST API METHODS ///////////////
// Method :: POST ||  Description :: Student S Checks In from Room R ##
function checkInStud(uname_id,campus,building,floor,room){
	var URI='roistapi/uname/'+uname_id+'/room/'+campus+'/'+building+'/'+floor+'/'+room;
	var URL='http://'+server+':'+port+'/'+URI
	var request = new XMLHttpRequest();
	request.open("POST",URL);
	request.setRequestHeader("Content-type", "application/json");
	dataOut=JSON.stringify({});
	request.send(dataOut);
	request.onreadystatechange = function(){
		 if (request.readyState == 4 && request.status == 200){
	    	var dataIn = JSON.parse(request.responseText);
	    	if (dataIn.Success==true){
	    		var resString="You are successfully Checked-In";
	    		var loc = document.getElementById("roomtag");
	    		loc.innerHTML = "<i><b>Status:</b>  You are currently ckecked-in in at "
	    					 + "</br> <i>Campus:</i> " + campus
	    					 + "</br> <i>Building:</i> " + building
	    					 + "</br> <i>Floor:</i> " + floor
	    					 + "</br> <i>Room:</i> " + room;
	    	}
	    	else{
	    		var resString="You were not able Check-In";
	    	}
	    	alert(resString);
		}
	}
}

// Method :: POST ||  Description :: Student S Checks In from Room R ##
function checkOutStud(uname_id){
	var URI='roistapi/uname/'+uname_id;
	var URL='http://'+server+':'+port+'/'+URI
	var request = new XMLHttpRequest();
	request.open("DELETE",URL);
	request.send(null)
	request.onreadystatechange = function()
    {
    	if (request.readyState == 4 && request.status == 200){
	    	dataIn = JSON.parse(request.responseText);
	    	if (dataIn.Success == true){
	    		var resString="You are successfully Checked-Out";
	    		var loc = document.getElementById("roomtag");
				loc.innerHTML="<i><b>Status:</b>  You are not Checked-In in any Room</i>";
	    	}
	    	else{
	    		var resString="You were not able to Check-Out";
	    	}
	    	alert(resString);
	    }
	}
}

// Method :: GET ||  Description :: Retrieve Available Rooms
function retrieveAvabRooms(campus=null,building=null,floor=null,room=null){
	var i;
	if (campus === null){
		var URI='roistapi/uname/'+uname_id+'/room';
		var index=0;
	}
	else if (building === null){
		var URI='roistapi/uname/'+uname_id+'/room/'+campus;
		var index=1;
		Rooms[0]=campus;
	}
	else if (floor === null){
		var URI='roistapi/uname/'+uname_id+'/room/'+campus+'/'+building;
		var index=2;
		Rooms[1]=building;
	}
	else if (room === null){
		var URI='roistapi/uname/'+uname_id+'/room/'+campus+'/'+building+'/'+floor
		var index=3;
		Rooms[2]=floor;
	}
	else {
		var URI='roistapi/uname/'+uname_id+'/room/'+campus+'/'+building+'/'+floor+'/'+room
		var index=4;
		Rooms[3]=room;
	}

	var URL='http://'+server+':'+port+'/'+URI
	var response = new XMLHttpRequest();
	response.open("GET",URL);
	response.send(null);
	response.onreadystatechange = function()
    {
    	var loc;
    	var htmlString = "";
		var dataIn;
		var res;
    	if (response.readyState == 4 && response.status == 200){
	    	dataIn = JSON.parse(response.responseText);
	    	if (dataIn.Success == true){
	    		if (index < 4){
	    			res=dataIn.Rooms;
	    			if (res.length==0)
	    				return
	    		}
	    		else
	    			res=dataIn.Students;
	    		if (index == 4){
	    			loc=document.getElementById("check_in");
	    			console.log(loc);
	    			loc.innerHTML="<b>Check-In </b> at "
	    						 + "</br> <i>Campus:</i> " + Rooms[0]
	    						 + "</br> <i>Building:</i> " + Rooms[1]
	    						 + "</br> <i>Floor:</i> " + Rooms[2]
	    						 + "</br> <i>Room:</i> " + Rooms[3];
	    		}
	  			for (i=0; i<res.length; i++){
	  				loc=document.getElementById(int2room[index])
					if (index < 4){
						var opt = document.createElement('option');
    					opt.value = res[i];
    					opt.innerHTML = res[i];
    					loc.appendChild(opt);
					}
					else{
						var item = document.createElement('li');
    					item.innerHTML = res[i];
    					loc.appendChild(item);
					}
				}
				if (campus === null){
	    			retrieveAvabRooms(res[0])
	    		}
	    		else if (building === null){
	    			retrieveAvabRooms(campus,res[0])
	    		}
	    		else if (floor === null){
	    			retrieveAvabRooms(campus,building,res[0])
	    		}
	    		else if (room === null){
	    			retrieveAvabRooms(campus,building,floor,res[0])
	    		}
					// loc.insertAdjacentHTML('beforeend',htmlString);
	    	}
	    }
	}
}
