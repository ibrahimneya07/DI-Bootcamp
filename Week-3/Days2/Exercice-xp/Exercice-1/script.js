let ib=document.getElementsByTagName("h1")[0];
console.log(ib);
document.getElementsByTagName("p")[3].remove();
document.getElementsByTagName("h2")[0].onclick=function(){
    document.getElementsByTagName("h2")[0].style.backgroundColor="red";
}
document.getElementsByTagName("h3")[0].onclick=function(){
    document.getElementsByTagName("h3")[0].style.display="none";
}
document.getElementsByTagName("button")[0].onclick=function(){
    for(let i=0;i<4;i++){
        document.getElementsByTagName("p")[i].style.fontWeight="bold";
    }
}
document.getElementsByTagName("h1")[0].onmouseover=function(){
    document.getElementsByTagName("h1")[0].style.fontSize="50px";
}