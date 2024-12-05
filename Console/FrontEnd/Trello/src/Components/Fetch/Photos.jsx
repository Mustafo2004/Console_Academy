import { useEffect } from "react"
import { useState } from "react"

const Photos = () => {
    const [photos, setPhotos] = useState([])
    const API_URL = "https://jsonplaceholder.typicode.com/photos"

    useEffect(()=>{
        async function fetchPhotos(){
            const responce = await fetch(API_URL)
           const data = await responce.json()
            setPhotos(data)
        }
        fetchPhotos()
    },[])
    return (
        <div>
            {photos.map((item) => {
                return(
                    <div key={item.id}>
                        <img src={item.url} alt={item.title} />
                        <img src={item.thumbnailUrl} alt="" />
                    </div>
                )
            })}
        </div>
    )
}

export default Photos