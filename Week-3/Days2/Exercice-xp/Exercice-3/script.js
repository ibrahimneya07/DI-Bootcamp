var allBoldItems;
function getBold_items(){
    for(let i=0;i<6;i++){
       allBoldItems= document.getElementsByTagName("strong")[i].innerHTML;
       console.log(allBoldItems);
    }
    
}
function highlight(){
    for(let i=0;i<6;i++){
        document.getElementsByTagName("strong")[i].style.color="blue";
    }
}


function return_normal(){
    for(let i=0;i<6;i++){
        document.getElementsByTagName("strong")[i].style.color="black";
    }
}

//appelle des fonction

   allBoldItems= document.getElementsByTagName("p")[0];
   allBoldItems.addEventListener("mouseover",highlight);

   allBoldItems= document.getElementsByTagName("p")[0];
   allBoldItems.addEventListener("mouseout",return_normal);