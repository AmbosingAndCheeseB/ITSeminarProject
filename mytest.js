$(document).ready(function(){
	"use strict";
  $(".content").slice(0, 4).show();
  $("#loadMore").on("click", function(e){
    e.preventDefault();
    $(".content:hidden").slice(0, 4).slideDown();
    if($(".content:hidden").length === 0) {
      $("#loadMore").text("No Content").addClass("noContent");
    }
  });
  
});