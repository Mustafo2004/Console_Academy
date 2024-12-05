async function GetPosts() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const data = await response.json();
    console.log(data);
    RenderUsers(data);
  } catch (error) {
    console.log(error);
  }
}
GetPosts();

async function GetComment() {
  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/comments"
    );
    const comment = await response.json();
    console.log(comment);
    RenderUsers(comment);
  } catch (error) {
    console.log(error);
  }
}
GetComment();

async function GetAlbums() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/albums");
    const Album = await response.json();
    console.log(Album);
    RenderUsers(Album);
  } catch (error) {
    console.log(error);
  }
}

GetAlbums();

async function GetPhotos() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/photos");
    const Photos = await response.json();
    console.log(Photos);
    RenderUsers(Photos);
  } catch (error) {
    console.log(error);
  }
}

GetPhotos()

async function Todos() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/photos");
    const Todo = await response.json();
    console.log(Todo);
    RenderUsers(Todo);
  } catch (error) {
    console.log(error);
  }
}

Todos()
