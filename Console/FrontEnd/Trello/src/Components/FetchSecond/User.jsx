import { useEffect, useState } from "react"

const User = () => {
    const [userArray, setUserArray] = useState([])

    // const [userName, setUserName] = useState("")
    // const [userPhone, setUserPhone] = useState("")
    // const [userSurname, setUserSurname] = useState("")

    const [loading, setLoading] = useState(false)
    const API_URL = "https://66a727f953c13f22a3ce9f60.mockapi.io/fetch/post/Contact"

    async function GetUsers() {
        try {
            setLoading(true)
            const response = await fetch(API_URL)
            const data = await response.json()
            setUserArray(data)
        } catch (error) {
            console.log(error);
        }
        setLoading(false)
    }
    useEffect(() => {
        GetUsers()
    }, [])
    // const hanldeSubmit = async (e) => {
    //     e.preventDefault()
    //     const newUser = {
    //         name,
    //         phone,
    //         surname
    //     }

    // }

    return (
        <div>
            {/* <h2>Form</h2>
            <form>
                <input type="text" onChange={(e) => { setUserName(e.target.value) }} value={userName} />
                <input type="text" onChange={(e) => { setUserPhone(e.target.value) }} value={userPhone} />
                <input type="text" onChange={(e) => { setUserSurname(e.target.value) }} value={userSurname} />
            </form> */}
            <div>
                {
                    loading == true ? <p>Loading</p> : null
                }
                {
                    userArray.length > 1 && loading == false ? (<p>Cannot find</p>) : userArray.map((item) => {
                        return (
                            <div key={item.id}>
                                <p>
                                    
                                </p>
                                <p>{item.phone}</p>
                                <p>{item.surname}</p>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default User