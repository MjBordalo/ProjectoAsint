
<h1>Administrator homepage.. </h1>
<p>
<input  type="button" id="button_refresh" href="#" class="myButton" value="Refresh Page"></input>

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
<table>
	<tr>
		<h2> Current rooms </h2>
		<td>
			<select id="available_rooms">
			</select>
		</td>
		<td>
			Occupancy:
	 	<input id="occupancy" class="field left" readonly>

	 	</td>
	</tr>
</table>

<p>
<input type="button" id="button_remove" value="Delete room"/>
</p>

<table class="maintable">
				<h2> Please select the available rooms  </h2>
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
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"> </script>
				<script> var campus_id={{campus_id}};</script>
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
<input type="button" id="button1" value="Add room"/>
</p>
