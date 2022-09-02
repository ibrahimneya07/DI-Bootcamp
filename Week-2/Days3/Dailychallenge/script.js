console.log("avec une boucle");
for(let i=1;i<=6;i++){
    let n="*";
    console.log(n.repeat(i));
}

console.log("avec deux boucles");
for(let i=1;i<=6;i++){
    for(let j=1;j<=i;j++){
    let n="*";
    console.log(n.repeat(i));
    }
    
}
