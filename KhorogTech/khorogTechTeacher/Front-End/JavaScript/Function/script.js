// Function Decloration

//* 1
function showMessage() {
  console.log("Message");
}
showMessage();
//* 2
function showMessage() {
  let message = "message"; //* mash na varthiyam peremena qiwdo berun az funkiciya  aga ya ar funkciya darun sodat chuxj ca ved
  console.log("message"); //* obyavlenie peremenuyu vnutri funkcii nazivaetsa lakalnaya funkciya
}
console.log(message);

//* 3  dizga peremenaya ta loven vneshnaya peremenaya ya aga aga berun az funkciya winchak sodat az az wam darun
let message;
function showMessage() {
  message = "message";
}
showMessage();
console.log(message);
//  masahrd lap udobne vneshme peremene sozdat chid   degat mash varviyam ca predele funkcii mam sozdat chid
