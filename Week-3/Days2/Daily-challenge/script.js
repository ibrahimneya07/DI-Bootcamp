// les differents fonction
var contenu,adjective,person,place,verb;
if(document.getElementById("noun")!=""){
     contenu=document.getElementById("noun").value;
}else{
    alert("Rcommencé en saisissant de text");
}

if(document.getElementById("adjective")!=""){
    adjective=document.getElementById("adjective").value;
}else{
    alert("Rcommencé en saisissant de text");
}

if(document.getElementById("person")!=""){
    person=document.getElementById("person").value;
}else{
    alert("Rcommencé en saisissant de text");
}
    
if(document.getElementById("place")!=""){
    place=document.getElementById("place").value;
}else{
    alert("Rcommencé en saisissant de text");
}

if(document.getElementById("verb")!=""){
    verb=document.getElementById("verb").value;
}else{
    alert("Rcommencé en saisissant de text");
}


document.getElementById("lib-button").onclick=function(){
    alert("Quand je te voie "+contenu+" je passe mon temps a experimenté tes "+adjective+ " oh toi mon "+person+ " alors que je suis "+verb+" dans mon burreau "+place);
}


