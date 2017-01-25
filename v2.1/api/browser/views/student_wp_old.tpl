<html>
<head>
	<title> Your Page - ROISTAPI </title>
</head>
<link rel="stylesheet" type="text/css" href="../static/css/student.css" />
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
}

button
{
   display: inline-block;
   width: 100%;
   height: 100%;
}

.btnckeckout{
	width: 100px;
	height: 50px;
	float: right;
}

</style>
<script type="text/javascript" src="../static/js/student.js"></script>
<body>
<div id="header" class="header">
	<div id="unametag"> </div>
	<div id="roomtag"> </div>
	<button class="btnckeckout" onclick="ClickcheckOutStud()"> Check-Out </button>
	<script> var uname="{{Username}}"; var room_id="{{Room}}"; placeHeader(uname,room_id); </script>
</div>
<center>
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
</center>
</body>
</html>
