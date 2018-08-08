document.addEventListener('DOMContentLoaded', () => {

// for the two hidden boxes (more park information and all reviews), click the respective button reveals the information
// about those parks.

 $(".my_button").click(function(){
     console.log($(this).next().css("display","block"));
 });

// two seprate close functions for closing the park description and all reviews

 $(".close").click(function(){
     $(".park_description").css("display","none")
 });

 $(".close").click(function(){
     $(".park_review").css("display","none")
 });

// function for displaying and hiding friends reviews on click

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}

});