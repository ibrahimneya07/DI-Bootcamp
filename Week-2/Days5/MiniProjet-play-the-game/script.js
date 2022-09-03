
//première partie

function playTheGame(){
   let dialogue=confirm("voulez-vous jouer au jeu");
    if(dialogue==false){
        alert("Pas de problème, au revoir");
    }else{
      let  numero=prompt("saisir un numéro entre 0 et 10");
        if(!Number(numero)){
            alert("Désolé, pas un numéro, au revoir");
        }else if(0>numero || numero>10){
            alert("Désolé, ce n'est pas un bon chiffre, au revoir ");
        }else{
           let computerNumbe=Math.floor(Math.random()  *10);
            alert("le nombre aleatoire selectionner est: "+computerNumbe);
        }
    }
}

//deuxième parties

function compareNumbers(userNumber,compareNumbers){
    playTheGame();
    userNumber=Number(prompt("saisir un nombre"));
    let numberTentative=0;
    if(userNumber=compareNumbers){
        alert("userNumber et compareNumbers sont egaux: FIN DU GAME");
    }else if(userNumber>compareNumbers && numberTentative<3){
        userNumber=Number(prompt("Votre numéro est plus grand que celui de l'ordinateur,devinez a nouveau:"));
        numberTentative=numberTentative+1;
    }else if(userNumber<compareNumbers && numberTentative<3){
        userNumber=Number(prompt("Votre numéro est plus pétit que celui de l'ordinateur,devinez a nouveau:"));
        numberTentative=numberTentative+1;
    }
}
compareNumbers();