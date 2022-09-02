function calculateTip(){
    let montant;
    let pourboire;
    let facture=parseInt(prompt("saisir le montant de la facture"));
    if(facture<50){
        pourboire=(facture*20)/100;
     montant=facture+(20/100);
    }else if(50<facture<100){
        pourboire=(facture*15)/100;
     montant=facture+(15/100);
    }else if(facture>200){
        pourboire=(facture*10)/100;
      montant=facture+(10/100);
    }
    console.log("le pourboire est "+ pourboire +" la facture final est "+montant);
}
calculateTip();