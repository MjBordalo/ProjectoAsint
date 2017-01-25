
$(document).ready(function() {
	alert("jijijij")
  $("#numbers").hide();

  $("#numbers").change(function() {
    var el = $(this) ;
    if(el.val() === "1" ) {
    $("#status").append("<option>1000000</option>");
    }
      else if(el.val() === "MANUAL" ) {
        $("#status option:last-child").remove() ; }
  });

});
