
Numbers:
	<select id="numbers">
		%for value in numbers:
		<option> {{value}}</option>
		%end
 	</select>

Letters:
	<select id="letters">
		%for value in letters:
		<option class="opt"> {{value}}</option>
		%end
	</select>
<script type="text/javascript" src="jquery-3.1.1.js"></script>
<script type="text/javascript" src="test_j.js"></script>
