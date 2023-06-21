let linkMenuItems = document.querySelectorAll(".link-item-menu");

linkMenuItems[linkMenuItems.length-1].style.borderBottomLeftRadius = "10px";
linkMenuItems[0].style.borderTopLeftRadius = "10px";

let menuArea = document.querySelector("#show-menu-info");

function menuSlideShow(){
	menuArea.classList.toggle("class-appear-menu");
}

function validateEmail(email){
  return String(email)
    .toLowerCase()
    .match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};

const firstText = document.querySelector(".first-text");
const firstTextContainer = document.querySelector(".text-first");
const btn = document.querySelector("#btnButton");
const btnText = document.querySelector("#btnText");
const btnButton = document.querySelector("#btnButton");
btn.onclick = () => {

    var params = {
		name:document.getElementById("user-input-id").value,
		email:document.getElementById("email-input-id").value,
		message:document.getElementById("msg-input-id").value
	}

	if (document.getElementById("user-input-id").value.length == 0){
		firstText.innerText = "Numele este prea scurt";
		firstText.style.color = "#e64b40";
	}
	else if (!validateEmail(document.getElementById('email-input-id').value))
	{
		firstText.innerText = "Email Invalid";
		firstText.style.color = "#e64b40";
	}
	else if(document.getElementById("msg-input-id").value.length == 0)
	{
		firstText.innerText = "Mesajul este prea scurt";
		firstText.style.color = "#e64b40";
	}
	else{
		const serviceId = "service_qguzivd"
		const templateId = "template_6b3m28v"
		emailjs.send(serviceId,templateId,params)
		firstText.innerText = "Email trimis cu succes";
		firstText.style.color = "#3b4a59";
		btnText.innerHTML = "&nbspTRIMIS";
    btnText.marginLeft = "20px";
    btn.classList.add("active");
   	btnButton.color = "white";
		document.getElementById("user-input-id").value = '';
		document.getElementById("email-input-id").value = '';
		document.getElementById("msg-input-id").value = '';
	}
	
};