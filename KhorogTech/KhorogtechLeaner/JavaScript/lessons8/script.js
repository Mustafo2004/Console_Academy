// // Ex 1
// const balloons = [
//     { number: 1, color: "red" },
//     { number: 2, color: "black" },
//     { number: 3, color: "green" },
//     { number: 4, color: "red" },
//     { number: 5, color: "red" },
//     { number: 6, color: "black" },
//     { number: 7, color: "blue" },

// ];
// let filteredBalloons = [];

// for (let i = 0; i < balloons.length; i++) {
//     // let el = balloons[i]

//     if (balloons[i].color == "red") {
//         filteredBalloons.push(balloons[i])
//     }

// }
// console.log(filteredBalloons);

// // EX 2

// let student = [
//     {
//         name: "Ahur",
//         age: 13,
//     },
//     {
//         name: "Mustafo",
//         age: 27,
//     },
//     {
//         name: "Yasmina",
//         age: 17,
//     },
//     {
//         name: "Adolat",
//         age: 18,
//     },
//     {
//         name: "Sanoi",
//         age: 33,
//     },
//     {
//         name: "Azamat",
//         age: 22,
//     },
// ]
// let studentAge = [];

// for (let m = 0; m < student.length; m++) {

//     if (student[m].age < 18) {
//         studentAge.push(student[m])
//     }


// }
// console.log(studentAge);











// Ex 3


// let names = ["Adolat", "Mustafo", "Yasmina", "Adolat2", "Nadim"];
// let filterNames = []


// for (let i = 0; i < names.length; i++) {
//     let element = names[i];
//     if (names[i][0] == "A") {
//         filterNames.push(element[0])
//     }
// }
// console.log(filterNames);




// Ex 3 same 

// let secoundName = ["Shurat", "Afraz ", "Noziya", "Ramazon", "Nozim", "Qurbon", "Nazarkhudo"];
// let filterSecoundName = [];

// for (let i = 0; i < secoundName.length; i++) {
//     let element = secoundName[i]
//    if (element[0] == "N") {
//     filterSecoundName.push(secoundName)
//    }

// }

// console.log(filterSecoundName);

// mam bad az yakath ke


// let nums4 = [12, 24, 75, 50, 86, 97, 35, 66, 8];
// let lessThan = [];

// for (let i = 0; i < nums4.length; i++) {
//     let element = nums4[i]
//     if (element[0] <= 50) {
//         lessThan.push(nums4)
//     }

// }
// console.log(lessThan);




// Ex 4
let numbers = [5, 65, 23, 38, 87, 46, 99, 52];
let answer = [];

for (let i = 0; i < numbers.length; i++) {
    answer = answer + numbers[i];


}
console.log(answer);


