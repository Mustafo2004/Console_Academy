const posts = [
    {
        image: "./images/image.png",
        icon: "./images/Vector.png",
        type: "Podcast",
        field: "Marketing",
        data: "September 4, 2020",
        duration: "36 min",
        name: "What is traffic arbitrage and does it really make money?",
        trancription: "Pharetra, ullamcorper iaculis viverra parturient sed id sed. Convallis proin dignissim lacus, purus gravida...",
        icon1: "./images/Line (Stroke).png",
        want: "listen"
    },
    {
        image: "./images/image1.jpg",
        icon: "./images/vector1.png",
        type: "Article",
        field: "Development",
        data: "September 1, 2020",
        duration: "",
        name: "How to choose the first programming language for a beginner",
        trancription: "Turpis sed at magna laoreet gravida consequat tortor placerat. Gravida vitae aliquet enim egestas dui...",
        icon1: "./images/Line (Stroke).png",
        want: "Read"
    },
    {
        image: "./images/image2.png",
        icon: "./images/Vector2.png",
        type: "Video",
        field: "Design",
        data: "August 8, 2020",
        duration: "40 min ",
        name: "Should you choose a creative profession if you are attracted to creativity?",
        trancription: "Curabitur nisl tincidunt eros venenatis vestibulum ac placerat. Tortor, viverra sed vulputate ultrices...",
        icon1: "./images/Line (Stroke).png",
        want: "Watch"
    },
    {
        image: "./images/image3.jpg",
        icon: "./images/vector1.png",
        type: "Article",
        field: "HR & Recruting",
        data: "August 3, 2020",
        duration: " ",
        name: "HR statistics: job search,  interviews, hiring and recruiting",
        trancription: "Massa, lectus nibh consectetur aliquet nunc risus aenean. Leo hac netus bibendum diam adipiscing aenean nisl. Molestie nullam ante mattis ac sit vitae pellentesque mi etiam. Morbi commodo tempor, massa vivamus. A molestie id semper fermentum pretium...",
        icon1: "./images/Line (Stroke).png",
        want: "Read"
    },
    {
        image: "./images/image4.png",
        icon: "./images/Vector2.png",
        type: "Video",
        field: "Management",
        data: "August 2, 2020",
        duration: " 45 min",
        name: "What to do and who to talk to if you want to get feedback on the product",
        trancription: "Neque a, senectus consectetur odio in aliquet nec eu. Ultricies ac nibh urna urna sagittis faucibus. Curabitur nisl tincidunt eros venenatis...",
        icon1: "./images/Line (Stroke).png",
        want: "Watch"
    },
    {
        image: "./images/image5.png",
        icon: "./images/Vector.png",
        type: "Podcast",
        field: "Design",
        data: "July 28, 2020",
        duration: "36 min ",
        name: "What are color profiles and how they work in graphic design",
        trancription: "Aliquam vulputate hendrerit quam sollicitudin urna enim viverra gravida. Consectetur urna arcu eleifend...",
        icon1: "./images/Line (Stroke).png",
        want: "Listen"
    },
    {
        image: "./images/image6.png",
        icon: "./images/Vector2.png",
        type: "Video",
        field: "Management",
        data: "July 15, 2020",
        duration: "45 min ",
        name: "Startup: how to build a team that will live longer than a year",
        trancription: "Nisi, massa ut sit faucibus et diam. Faucibus at malesuada at justo scelerisque in nisi, urna...",
        icon1: "./images/Line (Stroke).png",
        want: "Watch"
    },
    {
        image: "./images/image7.jpg",
        icon: "./images/Vector1.png",
        type: "Article",
        field: "Marketing",
        data: "July 9, 2020",
        duration: " ",
        name: "How to get customers to love your business from the start",
        trancription: "Malesuada in augue mi feugiat morbi a aliquet enim. Elementum lacus, pellentesque etiam arcu tristique ac...",
        icon1: "./images/Line (Stroke).png",
        want: "Read"
    },


];
const elementTag = document.getElementById("all");
elementTag.className = "container1"
posts.forEach((post, index) => {

    // obesheta sen obshe 1.div  bad image 2.Div bad podcast div  vota sod 3.iga div listen 

    

    const imgDivTag = document.createElement("div");
    imgDivTag.className = "div-container div-" + (index + 1)
    elementTag.appendChild(imgDivTag);

    const iconDivTag = document.createElement("div");
    iconDivTag.className = "div-icon  div-" + (index + 1);
    imgDivTag.appendChild(iconDivTag);

      // img v imgDivTag ar obshe
      const imgTag = document.createElement("img");
      imgDivTag.appendChild(imgTag);
      imgTag.src = post.image;


    const marketingDivTag = document.createElement("div");
    marketingDivTag.className = "div-marketing";
    imgDivTag.appendChild(marketingDivTag);




    //  iconDivTag  div
    const iconTag = document.createElement("img");
    iconDivTag.appendChild(iconTag);
    iconTag.src = post.icon;

    //  iconDivTag  div
    const typeTag = document.createElement("p");
    iconDivTag.appendChild(typeTag);
    typeTag.textContent = post.type;

    const fieldTag = document.createElement("p");
    marketingDivTag.appendChild(fieldTag);
    fieldTag.textContent = post.field;

    const dataTag = document.createElement("p");
    marketingDivTag.appendChild(dataTag);
    dataTag.textContent = post.data;

    const durationTag = document.createElement("p");
    marketingDivTag.appendChild(durationTag);
    durationTag.textContent = post.duration;

    const nameTag = document.createElement("h2");
    imgDivTag.appendChild(nameTag);
    nameTag.textContent = post.name

    const trancriptionTag = document.createElement("p");
    imgDivTag.appendChild(trancriptionTag);
    trancriptionTag.textContent = post.trancription;

    // ICON-1  xu div qate

    const icon1DivTag = document.createElement("div");
    icon1DivTag.className = "div-icon1  div-" + (index + 1);
    imgDivTag.appendChild(icon1DivTag);

    const wantTag = document.createElement("p");
    icon1DivTag.appendChild(wantTag);
    wantTag.textContent = post.want;

    const icon1Div = document.createElement("img")
    icon1DivTag.appendChild(icon1Div);
    icon1Div.src = post.icon1;



});
