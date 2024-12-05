import { useEffect, useState } from "react";
import HeaderOne from "./HeaderOne";
import { Link } from "react-router-dom";

const Users = () => {
    const [UserPost, setUserPost] = useState([])
    const API_URL = "https://66a7afc153c13f22a3d0b785.mockapi.io/api/media/Social"
    console.log(API_URL);


    async function GetUserPosts() {
        try {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setUserPost(data)
        } catch (error) {
            console.log(error);
        }

    }
    useEffect(() => {
        GetUserPosts()
    }, [])

    return (
        <div>
            <HeaderOne />
            <div className="flex items-center justify-center">

                {
                    UserPost.map((item) => {
                        return (
                            <div key={item.id} className="grid grid-cols-4">
                                <Link to={`/user/${item.id}`}>
                                    <h1>{item.surname}</h1>

                                </Link>

                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Users
