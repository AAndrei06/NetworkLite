var swiper = new Swiper(".mySwiper", {
      loop: true,
      spaceBetween: 1,
      slidesPerView: 4,
      freeMode: true,
      watchSlidesProgress: true,
    });
    var swiper2 = new Swiper(".mySwiper2", {
      loop: true,
      spaceBetween: 0,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      thumbs: {
        swiper: swiper,
      },
    });


let linkMenuItems = document.querySelectorAll(".link-item-menu");

linkMenuItems[linkMenuItems.length-1].style.borderBottomLeftRadius = "16px";
linkMenuItems[0].style.borderTopLeftRadius = "10px";

let menuArea = document.querySelector("#show-menu-info");

function menuSlideShow(){
  menuArea.classList.toggle("class-appear-menu");
}
