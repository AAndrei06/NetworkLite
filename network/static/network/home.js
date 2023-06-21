let linkItems = document.querySelectorAll(".link-item");

linkItems[0].style.borderTopLeftRadius = "5px";
linkItems[0].style.borderTopRightRadius = "5px";
linkItems[linkItems.length-1].style.borderBottomLeftRadius = "5px";
linkItems[linkItems.length-1].style.borderBottomRightRadius = "5px";



for (let i = 0;i < linkItems.length;i++)
{
	linkItems[i].addEventListener('click',() =>{

		for (let j = 0;j < linkItems.length;j++)
		{
			linkItems[j].style.borderLeftStyle = "none";
			linkItems[j].style.width = "100%";
			linkItems[j].style.color = "black";
			linkItems[i].style.width = "99%";
			linkItems[i].style.color = "#1d8bf9";
			linkItems[i].style.borderLeftStyle = "solid";
			linkItems[i].style.borderLeftColor = "#1d8bf9";
		}

	});
}

let newsItems = document.querySelectorAll(".news-item");

newsItems[newsItems.length-1].style.borderBottomLeftRadius = "5px";
newsItems[newsItems.length-1].style.borderBottomRightRadius = "5px";
newsItems[0].style.borderTop = "none";

let linkMenuItems = document.querySelectorAll(".link-item-menu");

linkMenuItems[linkMenuItems.length-1].style.borderBottomLeftRadius = "16px";
linkMenuItems[0].style.borderTopLeftRadius = "10px";

let menuArea = document.querySelector("#show-menu-info");

function menuSlideShow(){
	menuArea.classList.toggle("class-appear-menu");
}



 var swiper = new Swiper(".mySwiper", {
      slidesPerView: 3,
      spaceBetween: 10,
      mousewheel: {
  			releaseOnEdges: true,
			},
      loop: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
		   	120: {
		      slidesPerView: 1,
		      spaceBetween: 10
		    },
		    340: {
		      slidesPerView: 2,
		      spaceBetween: 10
		    },
		    400: {
		      slidesPerView: 2,
		      spaceBetween: 10
		    },
		    470: {
		      slidesPerView: 2,
		      spaceBetween: 10
		    },
		    580: {
		      slidesPerView: 3,
		      spaceBetween: 10
		    },

  	}
    });
