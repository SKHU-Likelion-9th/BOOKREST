const menuAll = document.querySelector(".js-menuAll");
const menu1 = document.querySelector(".js-menu1");
const menu2 = document.querySelector(".js-menu2");
const menu3 = document.querySelector(".js-menu3");
const menu4 = document.querySelector(".js-menu4");



const mainBookListInit = () => {
    itemList.forEach(function(item) {
        item.addEventListener("click", handleClick);
    });
}



mainBookListInit();