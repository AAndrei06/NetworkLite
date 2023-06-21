let userResults = document.querySelectorAll(".user-result");
let noResult = document.querySelector(".no-results");

if (userResults.length == 0)
{
	noResult.style.display = "inline-block";
}
else
{
	noResult.style.display = "none";
}

