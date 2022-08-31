let i=1;
let colors=["blue", "marron", "orange", "blanc", "noir"];
for( i in colors){
    console.log("Mon choix n°"+ i +" est " + colors[i]);
}
//tableau suffixe
console.log("tableau suffixe");

for( i in colors){
    if(i==0){
        console.log("Mon #" + i +" er choix est " + colors[i]);
    }else{
        console.log("Mon #" + i +" ème choix est " + colors[i]);
    }
}
    
