
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
function placeHeader(uname,room_id){
	var htmlString1 = "<b>Welcome "+uname+"</br>";
	var tmp=room_id.replace(/\//g,' ');
	console.log(tmp);
	if (tmp == "None")
		var htmlString2="<b>You are not checked-in in any rom</b>";
	else
		var htmlString2="<b>You are currently ckecked-in in at "+tmp+"</b>";

	var loc=document.getElementById('unametag');
	loc.insertAdjacentHTML('beforeend',htmlString1);
	loc=document.getElementById('roomtag');
	loc.insertAdjacentHTML('beforeend',htmlString2);
}

///// CHECK BUTTON /////
function ClickcheckOutStud(){
	var tmp = confirm("Would you like to Check-Out from this Room?");
	if (tmp==true)
		checkOutStud(uname_id)
}

/////////////// BODY ///////////////
///// TIMER FOR UPDATE SHOW AVAILABLE ROOMS /////
setInterval(function () {
	if (Rooms[0] != ""){
		var id="0.0";
		var elem=document.getElementById(id);
		if (elem != null)
			document.getElementById(id).click();}
	}, 5000);

///// UPADTE SHOW AVAILABLE ROOMS /////
function refreshAvabRooms(elem){
	var [index, val] = elem.value.split(".");
	console.log(index);
	index=Number(index);
	removeHtml(index+1);
	if (index==0)
		retrieveAvabRooms(val)
	else if (index==1)
		retrieveAvabRooms(Rooms[0],val)
	else if (index==2)
		retrieveAvabRooms(Rooms[0],Rooms[1],val)
	else{
		var tmp = confirm("Would you like to Check-In in this Room?")
		if (tmp == true){
			checkInStud(uname_id,Rooms[0],Rooms[1],Rooms[2],val)
			var htmlString="<div id='roomtag'>"
						  +"<b>You are currently ckecked-in in at "+Rooms[0]+Rooms[1]+Rooms[2]+val+"</b>"
						  +"</div>";
			var elem=document.getElementById('roomtag');
			if (elem!=null) {
		    	elem.parentNode.removeChild(elem);
		    	var loc=document.getElementById("header")
		    	loc.insertAdjacentHTML('beforeend',htmlString);
		    }
		}
		retrieveAvabRooms(Rooms[0],Rooms[1],Rooms[2],val)
	}
}

/////////////// AUXILIAR FUNCTIONS ///////////////
function removeHtml(index){
		var i=0;
		var index_str;
		var i_str;
		while(index<5){
			index_str=index;i_str=i;
			id=index_str.toString()+'.'+i_str.toString()+'e';
			var elem=document.getElementById(id);
			if (elem != null) {
		    	elem.parentNode.removeChild(elem);
		    	i+=1
			}
			else{
				index=index+1;i=0;
			}
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
	    	if (dataIn.Success==true)
	    		var resString="You have checked-in at "+campus+" "+building+" "+floor+" "+room+".";
	    	else
	    		var resString="You are not able to check-in at "+campus+" "+building+" "+floor+" "+room+".";
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
	    	if (dataIn.Success == true)
	    		var resString="You have checked-out";
	    	else
	    		var resString="You are not able to check-out";
	    	alert(resString);
	    	var htmlString="<div id='roomtag'>"
						  + "<b>You are not checked-in in any rom</b>"
						  +"</div>";
			var elem=document.getElementById('roomtag');
			if (elem!=null) {
		    	elem.parentNode.removeChild(elem);
		    	console.log(htmlString);
		    	var loc=document.getElementById("header")
		    	loc.insertAdjacentHTML('beforeend',htmlString);
		    }
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
	response.send(null)
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
	  			for (i=0; i<res.length; i++){
					id=index+'.'+i
					value=index+'.'+res[i];
					if (index < 4){
						buttonString="<button id='"+id+"' "
									+ "value='"+value
									+ "' onclick='refreshAvabRooms(this)'>"
									+ res[i] + "</button>";
					}
					else
						buttonString=res[i];
					htmlString += "<tr id='"+id+"e' >"
								+ "<td>"
								+ buttonString
								+ "</td> "
								+ "</tr> ";
				}
				console.log(htmlString);
				if (campus === null){
					loc=document.getElementById(int2room[0])
					loc.insertAdjacentHTML('beforeend',htmlString);
	    			retrieveAvabRooms(res[0])
	    		}
	    		else if (building === null){
					loc=document.getElementById(int2room[1])
					loc.insertAdjacentHTML('beforeend',htmlString);
	    			retrieveAvabRooms(campus,res[0])
	    		}
	    		else if (floor === null){
					loc=document.getElementById(int2room[2])
					loc.insertAdjacentHTML('beforeend',htmlString);
	    			retrieveAvabRooms(campus,building,res[0])
	    		}
	    		else if (room === null){
					loc=document.getElementById(int2room[3])
					loc.insertAdjacentHTML('beforeend',htmlString);
	    			retrieveAvabRooms(campus,building,floor,res[0])
	    		}
	    		else{
	    			loc=document.getElementById(int2room[4])
					loc.insertAdjacentHTML('beforeend',htmlString);
	    		}
	    	}
	    }
	}
}

