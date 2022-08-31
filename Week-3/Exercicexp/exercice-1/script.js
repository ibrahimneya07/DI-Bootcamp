//Partie I - Examen Des Tableaux

let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people.splice(2,1,"Jason");
people.push("Neya");
console.log(people.indexOf("Mary"));
console.log(people.slice(1));
console.log(people.indexOf("Foo"));//sa renvoie -1 car "Foo"  n' est pas dans le tableau
let last=people[3];
console.log(last);//l'indice du dernier elements du tableau est sa posistion dans le tableau
                    //alors que la longueur du tableau est le nombre d'elements dans le tableau


 //Partie II - Boucles
 console.log("affichage de tout les elements du tableau.");
 for(let i in people){
    console.log(people[i]);
 }

 console.log("affichage de tout les elements du tableau sauf Neya.");
 for(let i in people){
    if(i==3){
        break;
    }
    console.log(people[i]);
 }