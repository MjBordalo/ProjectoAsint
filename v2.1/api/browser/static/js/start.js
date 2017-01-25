function SubmitForm(){
	var x=document.getElementById("form");
	var server = 'localhost'
	var port = 8080
	var URI='roistapi/start'
	var URL='http://'+server+':'+port+'/'+URI
	var request = new XMLHttpRequest();
	request.open("POST",URL);
	request.setRequestHeader("Content-type", "application/json");
	dataOut=JSON.stringify({"uname":x.elements[0].value});
	request.send(dataOut);
	x.reset();
	request.onreadystatechange = function()
    {
    	var elem = document.getElementById("error");
    	if (elem != null)
    		elem.parentNode.removeChild(elem);
	    if (request.readyState == 4 && request.status == 200){
	    		var dataIn = JSON.parse(request.responseText);
	    		/*if (dataIn.Success == true)
	    			var result="Valid Username";
	    		else
	    			var result="Invalid Username";
	    		//var htmlString="<span id='error' class='error'>"+result+"</span>";
				//uname.insertAdjacentHTML('afterend',htmlString);*/
				if(dataIn.Success == true){
					var New_URL='http:'+'//localhost:8080/roistapi/uname/'+ dataIn.Identifier;
					window.location=New_URL
					var New_URL='http:'+'//localhost:8080/roistapi/uname/'+ dataIn.Identifier;
					window.location=New_URL
				}else{
					var result="Invalid Username";
					var htmlString="<span id='error' class='error'>"+result+"</span>";
					uname.insertAdjacentHTML('afterend',htmlString);
				}



	    }
    };
}
