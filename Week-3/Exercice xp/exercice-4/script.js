let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
//le nombre d'etage du batimen
console.log("le nombre d'etage du batiment");
    console.log(building.numberOfFloors);
    //le nombre d'appartements à l'etage est 1:
    console.log("le nombre d'appartements à l'etage est 1:");
    console.log(building.numberOfAptByFloor.firstFloor);
    //le nombre d'appartements à l'etage est 3:
    console.log("le nombre d'appartements à l'etage est 3:");
    console.log(building.numberOfAptByFloor.thirdFloor);
    //le nom du deuxième locataire et le nombre de pièces qu'il possède dans son appartement.
    console.log("le nom du deuxième locataire et le nombre de pièces qu'il possède dans son appartement.");
    console.log(building.nameOfTenants[1] ,  building.numberOfRoomsAndRent.dan);
    //Operation sur le loyer de Dan
    console.log("operation sur le loyer de Dan");
    let som=building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1];
    if(som>building.numberOfRoomsAndRent.dan[1]){
        building.numberOfRoomsAndRent.dan[1]=building.numberOfRoomsAndRent.dan[1]+1200;
        console.log(building.numberOfRoomsAndRent.dan[1]);
    }
    