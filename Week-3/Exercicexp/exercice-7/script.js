let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let societesecret=names.sort();
let jonction=societesecret.join(" ");
let societe=jonction.match(/\b(\w)/g);

console.log(societe.join(""));
