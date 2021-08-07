  $(".star_img").click(function(){
    if(confirm("관심 리스트에 추가하시겠습니까?") == true){
        alert("추가되었습니다");
        document.getElementById("img").src = "/static/img/star_onclick.png";
    }
    else{
        return ;
    }
});