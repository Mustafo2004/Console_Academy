import { useEffect, useState } from "react"

const Comments = () => {
    const [comments, setCommnets] = useState([])
    const API_URL = "https://jsonplaceholder.typicode.com/comments"
    useEffect(() => {
        async function GetComments() {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setCommnets(data)
            console.log(data);

        }
        GetComments()
    }, [])
    return (
        <div>
            {comments.map((item) => {
                return(
                    <div key={item.id}>
                        <h2>{item.name}</h2>
                        <p>{item.body}</p>
                        <p>User ID: {item.userId}</p>
                        <hr />
                    </div>
                )
            })}
        </div>
    )
}

export default Comments