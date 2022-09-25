function hidediv(){
    var div1 = document.getElementById("most-love-1");
    var div2 = document.getElementById("most-love-2");
    var div3 = document.getElementById("most-love-3");
    div1.style.display = "none"
    div2.style.display = "none"
    div3.style.display = "none"
}

function showdiv(score){
    var div1 = document.getElementById("most-love-1");
    var div2 = document.getElementById("most-love-2");
    var div3 = document.getElementById("most-love-3");
    // var rads = document.querySelectorAll('input[name="rating_sat"]');

    if (score === "1" || score === "2") {
        div1.style.display = "block"
        div2.style.display = "None"
        div3.style.display = "None"
    } else if (score === "3") {
        div1.style.display = "None"
        div2.style.display = "block"
        div3.style.display = "None"
    } else if (score === "4" || score === "5") {
        div1.style.display = "None"
        div2.style.display = "None"
        div3.style.display = "Block"
    } else {
        div1.style.display = "none"
        div2.style.display = "none"
        div3.style.display = "none"
    }
}



