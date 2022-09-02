let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
switch(users){
    case users.length==0:
        console.log("personne n'est en ligne.");
        break;
        case users.length==1:
            console.log(users[0] + " est en ligne");
            break;
            case users.length==2:
                console.log(users[0] + " et" + users[1] + " sont en ligne");
                break;
                case users.length>2:
                    let user=users.length-2;
                    console.log(users[0] + " ," + users[1]+ " , and " + user+ "more are online");
                    break;
                    default:
                        console.log("Good wind in use");

}