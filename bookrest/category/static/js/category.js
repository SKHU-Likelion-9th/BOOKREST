//all navbar
$('#get_all').click(function() {
  $("#all").show();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").hide();
  $("#it").hide();
})


//인문 navbar
$('#get_humanities').click(function() {
    $("#all").hide();
    $("#humanities").show();
    $("#society").hide();
    $("#media_content").hide();
    $("#it").hide();
})

//사회 navbar
$('#get_society').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").show();
  $("#media_content").hide();
  $("#it").hide();
})

//미컨 navbar
$('#get_media_content').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").show();
  $("#it").hide();
})

//it navbar
$('#get_it').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").hide();
  $("#it").show();
})