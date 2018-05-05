function toggleSideBar() {
    var sideBar = document.getElementById("mySidenav");
    if (sideBar.style.display === "none") {
        sideBar.style.display = "block";
    } else {
        sideBar.style.display = "none";
    }
}

$(document).keyup(function(e) {
     if (e.keyCode == 27) { 
     	var sideBar = document.getElementById("mySidenav");
     	if (sideBar.style.display === 'block'){
     		sideBar.style.display = "none";
     	}
    }
});
