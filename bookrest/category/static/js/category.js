





//인문 navbar
$('#get_humanities').click(function() {
  
  //카테고리 색상
  $("#get_humanities").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");
  

  var url = window.location.search;
  if(url == "major=인문&search="){
  $("#get_humanities").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");
}
})



//사회 navbar
$('#get_society').click(function() {

  //카테고리 색상
  $("#get_society").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  $("#get_it").css("background-color","#808080");
  
})

//미컨 navbar
$('#get_media_content').click(function() {

  //카테고리 색상
  $("#get_media_content").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_it").css("background-color","#808080");

})

//it navbar
$('#get_it').click(function() {
  //카테고리 색상
  
  $("#get_it").css("background-color","#2DBE61");
  $("#get_all").css("background-color","#808080");
  $("#get_humanities").css("background-color","#808080");
  $("#get_society").css("background-color","#808080");
  $("#get_media_content").css("background-color","#808080");  
  
})