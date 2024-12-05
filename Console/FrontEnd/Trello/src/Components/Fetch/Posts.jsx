import { useEffect, useState } from "react"

const Posts = () => {
    const [dataJson, setDataJson] = useState([])
    const API_URL = "https://jsonplaceholder.typicode.com/posts"

    useEffect(() => {
        async function GetPosts() {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setDataJson(data)
            console.log(data);
        }
        GetPosts()
    }, [])
    return (
        <div className="border border-red-900 p-[20px] flex flex-wrap justify-between items-center gap-3">
            {dataJson.map((post) => {
                return (
                    <div key={post.id} className="border border-black w-[200px] h-[500px] p-[20px]">
                        <h1>{post.title}</h1>
                        <p>{post.body}</p>
                    </div>
                )
            })}
        </div>
    )
}

export default Posts