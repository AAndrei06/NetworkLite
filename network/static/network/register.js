try{

let error_field = document.querySelector(".register-errors");

function deleteObject(){

	error_field.innerText = "";
	error_field.style.display = "none";

}

if (error_field.innerText == "")
	error_field.style.display = "none";
else{
	error_field.style.display = "inline-block";

	setTimeout(deleteObject,6000);
}

}
catch
{
	console.log("error")

}
