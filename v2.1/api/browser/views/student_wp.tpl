<html>

<head>
	<title> {{Username}} - ROISTAPI </title>
</head>
<link rel="stylesheet" type="text/css" href="../static/css/base.css" />
<link rel="stylesheet" type="text/css" href="../static/css/student.css" />

<script type="text/javascript" src="../static/js/student1.js"></script>

<body>

	<form id="form">

		<div class="imgcontainer">
			<img src="../static/figs/logotipo-tecnico-c.svg" alt="entry" class="avatar">
		</div>

		<div>
			<img style="float: left" src="../static/figs/user.png" alt="entry" class="user">
			<div>
				<h2>Hello {{Username}}!</h2>
				<div id="roomtag"> </div>
				<script>
					var room_id = "{{Room}}";
					initRoomString(room_id);
				</script>
				<input onclick="ProcessRefresh()" type="button" id="button_refresh" href="#" class="button small" value="Refresh Status" ></input>

			</div>
		</div>
		<div style="clear: left">

		</div>

		<!-- <input onclick="ProcessRefresh()" type="button" id="button_refresh" href="#" class="myButton" value="Refresh Page"></input> -->


		<h3> Check-In / Check Out </h3>

		<button id="check_in" class="button" onclick="ProcessCheckIn()"> cenas </button>
		<button id="check_out" class="button" onclick="ProcessCheckOut()"> <b> Check Out</b>  </button>

		<!-- <input id="check_out" onclick="ProcessCheckOut()" type="button" class="button" value="check_in"> -->

		<h3> List of Available Rooms </h3> Campus: <select id="campus" onchange="refreshAvabRooms('campus')"></select>
		<br> Building: <select id="building" onchange="refreshAvabRooms('building')"></select>
		<br> Floor: <select id="floor" onchange="refreshAvabRooms('floor')"></select>
		<br> Rooms: <select id="name" onchange="refreshAvabRooms('name')"></select>
		<br>

		<h3> List of Students in the Room </h3>
		<ol id="stud"> </ol>
		<script>
			initAvabRooms()
		</script>

	</form>
</body>

</html>


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
