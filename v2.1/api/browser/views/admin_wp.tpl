<html>

<head>
	<title> admin - ROISTAPI </title>
</head>

<link rel="stylesheet" type="text/css" href="../static/css/base.css" />
<!-- Override some styles -->
<link rel="stylesheet" type="text/css" href="../static/css/admin.css" />

<body>

	<form id="form">



		<div class="imgcontainer">
			<img src="../static/figs/logotipo-tecnico-c.svg" alt="entry" class="avatar">
		</div>

		<div>
			<img style="float: left" src="../static/figs/admin.png" alt="entry" class="user">
			<div>
				<div>
					<h2>Hello admin!</h2>

					<!-- TODO:  ProcessRefresh esta errado! -->
					<input onclick="ProcessRefresh()" type="button" id="button_refresh" href="#" class="button small" value="Refresh Status" ></input>
				</div>
			</div>
		</div>

		<div style="clear: left">

		</div>

		<!-- <input type="button" id="button_refresh" href="#" class="myButton" value="Refresh Page"></input> -->

		<h3> Current rooms </h3>
		<select id="available_rooms"></select>
		Occupancy:
		<!-- TODO:  Melhorar o design disto que tipo de var é esta? -->
		<input id="occupancy" class="field left" readonly>


		<input type="button" class="button small" id="button_remove" value="Delete room" />


		<table class="maintable">
			<h3> Please select the available rooms  </h3>
			<tr style="line-height:50px;">
				<td>Campus</td>
				<td>:</td>
				<td>
					<select id="campus">
                            <option values="">--Select--</option>
							%for item in campus_names:
							<option>{{item}}</option>
							 %end

                        </select>
				</td>
			</tr>
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js">
			</script>

			<script>
				var campus_id = [];
				var i = 0; %
				for item in campus_id:
					campus_id[i] = {
						{
							item
						}
					};
				i = i + 1; %
				end
			</script>

			<script type="text/javascript" src="../static/js/admin_domingos.js"></script>

			<tr style="line-height:20px;">
				<td>Building</td>
				<td>:</td>
				<td>
					<select style="float:left;" id="buildings">
                        </select>
				</td>
			</tr>
			<tr style="line-height:20px;">
				<td>Floor</td>
				<td>:</td>
				<td>
					<select style="float:left;" id="floors">
                        </select>
				</td>
			</tr>

			<tr style="line-height:20px;">
				<td>Room</td>
				<td>:</td>
				<td>
					<select style="float:left;" id="rooms">
                        </select>
				</td>
			</tr>
		</table>
		<p>
			<input type="button" class="button small" id="button1" value="Add room" />
		</p>

	</form>
</body>

</html>
