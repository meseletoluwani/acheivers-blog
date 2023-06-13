let clicked = 1
let clicked2 = 1
$("#toggle-password").click(function() {
    
    if (clicked % 2 == 0){
        $("#password").attr("type", "password");
        clicked++ 
    }
    else{
        $("#password").attr("type", "text");
        clicked++
    }
  } );

  $("#toggle-password2").click(function() {
    
    if (clicked2 % 2 == 0){
        $("#password2").attr("type", "password");
        clicked2++ 
    }
    else{
        $("#password2").attr("type", "text");
        clicked2++
    }
  } );

$(".delete").click(function(){
    let to_select = ".pop-up" + String(this.id)
    $(to_select).removeClass("none")
    $(to_select).addClass("display-popup")
})

$(".kill-popup").click(function(){
    let to_select = ".pop-up" + String(this.id)
    $(to_select).addClass("none")
    $(to_select).removeClass("display-popup")
})