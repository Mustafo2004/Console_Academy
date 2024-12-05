import { useEffect, useState } from "react"

const Posts = () => {
    const [users, setUsers] = useState([])
    const [name, setName] = useState("")
    const [phone, setPhone] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const API_URL = "http://192.168.0.102:3000/api/get/contact"
    const API_URLPost = "http://192.168.0.102:3000/api/post/contact"

    async function GetUsers() {
        try {
            setIsLoading(true)
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setUsers(data)
        } catch (error) {
            console.log(error);
        }
        setIsLoading(false)
    }
    useEffect(() => {
        GetUsers()
    }, []);



    // ! Post 
    const handleSubmit = async (event) => {
        event.preventDefault()
        console.log("salom");
        const newContact = {
            name,
            phone,
        }
        const responce = await fetch(API_URLPost, {
            method: "POST",
            body: JSON.stringify(newContact),
            headers: {
                "Content-Type": "application/json",
                // "Accept": "application/json"
            }
        })

        const data = await responce.json()
        console.log(data);
    }
    return (
        <>
            <div>
                {
                    isLoading == true ? <p>Loading</p> : null
                }
                {
                    users.length > 1 && isLoading == false ? (
                        <p>Cannot find</p>
                    ) : users.map(user => (
                        <div key={user._id}>
                            <h2>{user.name}</h2>
                            <p>{user.email}</p>
                            <p>{user.phone}</p>
                        </div>
                    ))

                }
            </div>
            <div>
                <h1>Form</h1>
                <form onSubmit={handleSubmit}>
                    <input type="text" placeholder="Name" onChange={(e) => { setName(e.target.value) }} value={name} />
                    <input type="tel" placeholder="EmaPhone" onChange={(e) => { setPhone(e.target.value) }} value={phone} />
                    <button className="border text-black" >Subit</button>
                </form>



            </div >
        </>
    )
}

export default Posts