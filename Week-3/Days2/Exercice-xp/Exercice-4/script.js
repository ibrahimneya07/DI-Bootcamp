document.getElementById("submit").onclick=function(){
    let radius=document.getElementById("radius").value;
    document.getElementById("volume").value=(Math.pow(radius,3)*(4/3)*3.14);
}
