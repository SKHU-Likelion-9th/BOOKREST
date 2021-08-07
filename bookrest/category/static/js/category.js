//all navbar
$('#get_all').click(function() {
  $("#all").show();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").hide();
  $("#it").hide();

  //카테고리 색상
  $("#get_all").css("background-color","#2DBE61");
  $("#get_humanities").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");

})


//인문 navbar
$('#get_humanities').click(function() {
  $("#all").hide();
  $("#humanities").show();
  $("#society").hide();
  $("#media_content").hide();
  $("#it").hide();
  

  //카테고리 색상
  $("#get_humanities").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");
  
  

 
  

})



//사회 navbar
$('#get_society').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").show();
  $("#media_content").hide();
  $("#it").hide();

  //카테고리 색상
  
  $("#get_society").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");
  
})

//미컨 navbar
$('#get_media_content').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").show();
  $("#it").hide();

  //카테고리 색상
  $("#get_media_content").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_it").css("background-color","#808080");

})

//it navbar
$('#get_it').click(function() {
  $("#all").hide();
  $("#humanities").hide();
  $("#society").hide();
  $("#media_content").hide();
  $("#it").show();

  //카테고리 색상
  
  $("#get_it").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
})