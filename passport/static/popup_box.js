document.addEventListener('DOMContentLoaded', () => {

 $(".my_button").click(function(){
     console.log($(this).next().css("display","block"));
 });

 $(".close").click(function(){
     $(".park_description").css("display","none")
 });


 $(".my_button").click(function(){
     console.log($(this).next().css("display","block"));
 });

 $(".close").click(function(){
     $(".park_review").css("display","none")
 });

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