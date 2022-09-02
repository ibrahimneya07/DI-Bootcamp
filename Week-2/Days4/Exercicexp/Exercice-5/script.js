function changeEnough(itemsPrice,amountofChange=[]){
    let sum=0;
    for(let i in amountofChange){
        let quarters=0.25;
        let dimes=0.10;
        let nickel=0.05;
        let penny=0.01;
        if(i==0){
            sum=amountofChange[i]*quarters+sum;
        }else if(i==1){
            sum=amountofChange[i]*dimes+sum;
        }
        else if(i==2){
            sum=amountofChange[i]*nickel+sum;
        }
        else if(i==3){
            sum=amountofChange[i]*penny+sum;
        }
    }
    if(sum>=itemsPrice){
       console.log("true");
    }else{
        console.log("false");
    }
}
changeEnough(14.11, [2,100,0,0]);