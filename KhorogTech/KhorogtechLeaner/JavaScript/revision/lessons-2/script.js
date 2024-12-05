//  1.Create masiv
const users = [
    {
        image: "./image22.png",
        name: "Mustafo",
        job: "Developer"
    },
    {
        image: "./image22.png",
        name: "Mustazo",
        job: "Developer"
    },
    {
        image: "./image22.png",
        name: "Anvar",
        job: "Developer"
    },
    {
        image: "./image22.png",
        name: "Unknown",
        job: "Developer"
    },
];

// 2.Get
const creatTag = document.getElementById("root");

// 3.
users.forEach(person => {
    const divTag = document.createElement("div");
    creatTag.appendChild(divTag);

    const imgTag = document.createElement("img");   
    divTag.appendChild(imgTag);
    imgTag.src = person.image;

    const text = document.createElement("h4");
    divTag.appendChild(text);
    text.textContent = person.name;

    
});