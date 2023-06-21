
let linkMenuItems = document.querySelectorAll(".link-item-menu");

linkMenuItems[linkMenuItems.length-1].style.borderBottomLeftRadius = "16px";
linkMenuItems[0].style.borderTopLeftRadius = "10px";

let menuArea = document.querySelector("#show-menu-info");

function menuSlideShow(){
	menuArea.classList.toggle("class-appear-menu");
}