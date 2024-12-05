// function namee() {

//     for (let i = 0; i < i < 50; i++) {
//        console.log("hello world");
//     }
// }

// namee();


// function createUser(teacher, number) {

//     console.log(teacher);
//     console.log(number);

//     const person = {
//         name: teacher,
//         phone: number
//     }

//     console.log(person);
// }
// createUser("Jasur", "99999999");






function findSpecificUsers(masiv) {


    for (let i = 0; i < masiv.length; i++) {
        const element = masiv[i]

        if (element == "Mustafo") {
            console.log(masiv[i]);
        };
    }
}

findSpecificUsers(["Adolat", "Yasmina", "Sanoi", "Mustafo", "Noziya"]);


function countNegativNumbers(array) {

    for (let i = 0; i < array.length; i++) {
        const element = array[i];

        if (element < 1) {
            console.log(element);
        }
        
    }

}

countNegativNumbers([-1, 2, -3, 4, -5, 6, 7, -8, -9, 10])