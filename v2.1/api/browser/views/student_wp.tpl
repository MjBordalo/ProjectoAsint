
<html>
<head>
	<title> Your Page - ROISTAPI </title>
</head>
<h1>Student {{Username}} homepage.. </h1>
<p>
<!-- <link rel="stylesheet" type="text/css" href="../static/css/student.css" />
<style>

.exttb{
	table-layout: fixed;
    border: 1px solid black;
	width:100px;
	height:300px;
	display:inline-block;
}

.inttb{
	width:100%;
	height:100%;
	white-space: nowrap;
}

tr,td {
    border: 1px solid black;
    width: 100px;
    height: 50px;
    overflow: hidden;
    white-space: nowrap;
} -->
<!--
/*button
{
   display: inline-block;
   width: 100%;
   height: 100%;
}*/

.btnckeckout{
	width: 100px;
	height: 50px;
	float: right;
} -->

</style>
<script type="text/javascript" src="../static/js/student1.js"></script>
<body>

<div id="roomtag"> </div>

<script> var room_id="{{Room}}"; initRoomString(room_id); </script>

</br>
<input onclick="ProcessRefresh()" type="button" id="button_refresh" href="#" class="myButton" value="Refresh Page"></input>

<style type="text/css">
body {
background-color: lightblue;
}
.myButton {
	-moz-box-shadow:inset -1px 0px 0px -50px #bee2f9;
	-webkit-box-shadow:inset -1px 0px 0px -50px #bee2f9;
	box-shadow:inset -1px 0px 0px -50px #bee2f9;
	background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #63b8ee), color-stop(1, #468ccf));
	background:-moz-linear-gradient(top, #63b8ee 5%, #468ccf 100%);
	background:-webkit-linear-gradient(top, #63b8ee 5%, #468ccf 100%);
	background:-o-linear-gradient(top, #63b8ee 5%, #468ccf 100%);
	background:-ms-linear-gradient(top, #63b8ee 5%, #468ccf 100%);
	background:linear-gradient(to bottom, #63b8ee 5%, #468ccf 100%);
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#63b8ee', endColorstr='#468ccf',GradientType=0);
	background-color:#63b8ee;
	-moz-border-radius:42px;
	-webkit-border-radius:42px;
	border-radius:42px;
	border:7px solid #3866a3;
	display:inline-block;
	cursor:pointer;
	color:#14396a;
	font-family:Times New Roman;
	font-size:24px;
	font-weight:bold;
	padding:11px 17px;
	text-decoration:none;
	text-shadow:0px -1px 50px #7cacde;
}
.myButton:hover {
	background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #468ccf), color-stop(1, #63b8ee));
	background:-moz-linear-gradient(top, #468ccf 5%, #63b8ee 100%);
	background:-webkit-linear-gradient(top, #468ccf 5%, #63b8ee 100%);
	background:-o-linear-gradient(top, #468ccf 5%, #63b8ee 100%);
	background:-ms-linear-gradient(top, #468ccf 5%, #63b8ee 100%);
	background:linear-gradient(to bottom, #468ccf 5%, #63b8ee 100%);
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#468ccf', endColorstr='#63b8ee',GradientType=0);
	background-color:#468ccf;
}
.myButton:active {
	position:relative;
	top:1px;
}

 </style>
</p>

<h2> Check-In / Check Out </h2>

<button id="check_in" onclick="ProcessCheckIn()">  </button>
<button id="check_out" onclick="ProcessCheckOut()"> <b> Check Out</b> </br> </br> </br> </br> </br> </button>

<h2> List of Available Rooms </h2>

Campus: <select id="campus" onchange="refreshAvabRooms('campus')" >
</select> </br>

Building: <select id="building" onchange="refreshAvabRooms('building')">
</select> </br>

Floor: <select id="floor" onchange="refreshAvabRooms('floor')">
</select> </br>

Rooms: <select id="name" onchange="refreshAvabRooms('name')">
</select> </br>

<h2> List of Students in the Room </h2>
<ol id="stud">
</ol>

<script> initAvabRooms() </script>



<!-- <div id="header" class="header">
	<div id="unametag"> </div>
	<div id="roomtag"> </div>
	<button class="btnckeckout" onclick="ClickcheckOutStud()"> Check-Out </button>
	<script> var uname="{{Username}}"; var room_id="{{Room}}"; initUser(uname,room_id); </script>
</div> -->
<!-- <center>
<script> initAvabRooms() </script>
<table class="exttb">
	<tr>
		<td>
			Campus
		</td>
		<td>
			Building
		</td>
		<td>
			Floor
		</td>
		<td>
			Room
		</td>
		<td>
			Students
		</td>
	</tr>
	<tr>
		<td>
			<table class="inttb" id="campus"> </table>
		</td>
		<td>
			<table class="inttb" id="building"></table>
		</td>
		<td>
			<table class="inttb" id="floor"> </table>
		</td>
		<td>
			<table class="inttb" id="name"> </table>
		</td>
		<td>
			<table class="inttb" id="stud"> </table>
		</td>
	</tr>
</table>
</center> -->
</body>
</html>
