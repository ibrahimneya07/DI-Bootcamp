    let stock={
        "banana":6,
        "apple":0,
        "pear":12,
        "orange":32,
        "blueberry":1
    }
    let prices={
        "banana":4,
        "apple":2,
        "pear":1,
        "orange":1.5,
        "blueberry":10
    }
    
    let shoppingList=["banana", "orange", "apple"];
    
function myBill(shoppingList,prices,stock){
    let i,j,k;
    let sum=0;
    for(i in shoppingList){
       for(j in stock){
        if(shoppingList[i]==j && stock[j]!=0){
            for(k in prices){
                if(j==k){
                    sum=sum+prices[k];
                    stock[j]=stock[j]-1;
                }
            }
        }
       }
    }
    console.log(sum);

    console.log("voici le nombre restant de chaque element après achat:")
    for(j in stock){
        console.log(stock[j]);
    }

    //la partie bonus

}
myBill(shoppingList,prices,stock);