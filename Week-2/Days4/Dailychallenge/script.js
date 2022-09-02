let tab=prompt("saisissez plusieurs mots en les séparant par des virgules");
let tableau=tab.split(",");
for(let i in tableau){
    console.log(tableau[i]);
}
