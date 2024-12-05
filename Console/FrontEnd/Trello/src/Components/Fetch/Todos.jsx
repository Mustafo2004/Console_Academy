import { useEffect } from "react"
import { useState } from "react"

const Todos = () => {
    const [Todos, setTodos] = useState([])
    const API_URL = "https://jsonplaceholder.typicode.com/todos"
    useEffect(() => {
        async function Todos() {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setTodos(data)
        }
        Todos()
    }, [])
    return (
        <div>
            {Todos.map((item) => {
                return(
                    <div key={item.id}>
                        <h1>{item.title}</h1>

                    </div>
                )
            })}
        </div>
    )
}

export default Todos