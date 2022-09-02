isDivisible();
function isDivisible(){
    let sum=0;
    for(let i=0;i<=500;i++){
        if(i%23==0){
            console.log(i);
            sum=sum+i;
        }
    }
    console.log("la somme de tous les nombres divisibles par 23 est:");
    console.log(sum);
}

//partie Bonus
/*console.log("la partie bonus");
function isDivisible(divisor){
    let divisor=parseInt(prompt("saisir un diviseur"));
    let sum=0;
    for(let i=0;i<=500;i++){
        if(i%divisor==0){
            console.log(i);
            sum=sum+i;
        }
    }
    console.log("la somme de tous les nombres divisibles par "+divisor+ " est:");
    console.log(sum);
}*/