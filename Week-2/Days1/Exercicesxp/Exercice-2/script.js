let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength=myWatchedSeries.length;
let myWatchedSeriesSentence="black mirror, money heist, and the big bang theory";
console.log("I watched "+ myWatchedSeriesLength + " series " + ": " + myWatchedSeriesSentence);
myWatchedSeries.splice(2,1,"friends");
myWatchedSeries.push("the resident");
myWatchedSeries.unshift("Startup");
myWatchedSeries.splice(1,1);
let ibra=myWatchedSeries.toString();
console.log(ibra.substring(10,11));
console.log(myWatchedSeries);