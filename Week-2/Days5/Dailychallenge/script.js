let x=prompt("saisir un nombre");
if(Number(x)){
    while(x!=0){
        x=x-1;
        alert("we have now "+x+" bottles");
    }
}else{
    alert("nombre incorrecte");
}