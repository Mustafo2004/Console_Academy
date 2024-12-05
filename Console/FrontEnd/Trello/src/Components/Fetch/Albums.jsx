import { useEffect } from "react"
import { useState } from "react"

const Albums = () => {
    const [albums, setAlbums] = useState([])
    const API_URL = "https://jsonplaceholder.typicode.com/albums"

    useEffect(() => {
        async function fetchAlbums() {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setAlbums(data)
        }
        fetchAlbums()
    }, [])
    return (
        <div>
            {
                albums.map((item) => {
                    return (
                        <div key={item.id}>
                            <p>{item.title}</p>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default Albums