// Find the average of the array
let numbers =[15,645,8,,3,67,,128,89,11];
let filterenumbers =[];
filt1=[];

for (let i = 0; i < numbers.length; i++) {
    const element = numbers[i];
    filterenumbers =filterenumbers+element;
}
filt1=filterenumbers / numbers.length;

console.log(filteredArray);
// Problem 23: Check if all element in  an array are positive numbers.
let array = [31,-5,44,97,-17,-35,0,47,-23];
let filteredArray =[]
for (r=0; r<array.length;r++){
    if(array[r]>=0)
    filteredArray.push(array[r])
}
console.log(filteredArray);