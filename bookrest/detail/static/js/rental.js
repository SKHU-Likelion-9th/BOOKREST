$("#modal-open").click(function(){
    if(confirm("대여신청 하시겠습니까?") == true){
        alert("대여신청 되었습니다");
        document.getElementById("img").src = "/static/img/star_onclick.png";
    }
    else{
        return ;
    }
});