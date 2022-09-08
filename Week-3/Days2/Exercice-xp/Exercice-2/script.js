let formulaire=document.forms[0];
console.log(formulaire);
//recuperation des entrées
document.getElementById("submit").onclick=function(){
    let firstinput=document.getElementById("fname").value;
    let secondinput=document.getElementById("lname").value;
    console.log(firstinput);
    console.log(secondinput);
}
    //recupérer des entrées grace au attribut des elements
    let fname=document.getElementById("fname").value;
    let lname=document.getElementById("lname").value;
document.getElementById("submit").onclick=function(){
    console.log(fname);
    console.log(lname);
}    

//dernière partie
let envoi=document.getElementById("submit");
envoi.addEventListener("onclick",test ());
function test(){
    if(fname=="" || lname==""){
        alert("Remplir tout les champs");
    }else{
        const liste1=document.createElement("li");
    const liste2=document.createElement("li");
    const c=document.body.firstElementChild.nextElementSibling;
    c.appendChild(liste1);
c.appendChild(liste2);
const text=document.createTextNode(fname);
liste1.appendChild(text);
const textt=document.createTextNode(lname);
liste2.appendChild(textt);

    }
}




