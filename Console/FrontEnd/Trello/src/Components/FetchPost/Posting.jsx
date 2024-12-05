import { useEffect, useState } from "react"
import SignIn from "../SignIn/SignIn"

const Posting = () => {
    const [users, setUsers] = useState([])
    const [name, setName] = useState("")
    const [deadline, setDeadline] = useState("")
    const [person, setPerson] = useState("")
    // const [done, setDone] = useState(false)
    const API_URL = "127.0.0.1:2442/course/get/all?age_status=adults&"
    // const API_URL_Post = "127.0.0.1:2442/course/add"

    async function GetUsers() {
        try {
            const responce = await fetch(API_URL)
            const data = await responce.json()
            setUsers(data)
        } catch (error) {
            console.log(error);
        }
    }
    useEffect(() => {
        GetUsers()
    }, []);


    const handleSubmit = async () => {
        // e.preventDefault()
        // const newTodo = {
        //     name,
        //     deadline,
        //     person,
        //     // done: false
        // }
        // const responce = await fetch(API_URL_Post, {
        //     method: "POST",
        //     body: JSON.stringify(newTodo),
        //     headers: {
        //         "Content-Type": "application/json",
        //     }
        // })
        // const data = await responce.json()
        // console.log(data);
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const raw = JSON.stringify({
            "Image": "1",
            "Age_Status": "kids",
            "General_Description_En": {
                "Name": "frontend",
                "Description": "development",
                "Level": "level 1",
                "Start_Date": "1.09.2024",
                "Course_Price": "$700",
                "Course_Duration": "from 1.09.2024 to 1.12.2024"
            },
            "General_Description_Ru": {
                "Name": "back-end",
                "Description": "development",
                "Level": "level 1",
                "Start_Date": "1.09.2024",
                "Course_Price": "$700",
                "Course_Duration": "from 1.09.2024 to 1.12.2024"
            },
            "Overal_Description_En": {
                "About_Course_Title": "development",
                "About_Course_Image": "1",
                "Course_Advantages": [
                    "Good"
                ],
                "Title": "for everyone",
                "Description": "asds",
                "Image": "1",
                "Teachers": [
                    "masrur"
                ],
                "Syllabus_Title": "sintaksis",
                "Syllabus_Description": "asdas",
                "Duration": {
                    "Topics": "12",
                    "Projects": "2",
                    "Hours": "221"
                },
                "Module": {
                    "Title": "GOlang",
                    "Description": "hello world"
                },
                "Question": [
                    {
                        "key": "name",
                        "Required": false,
                        "Type": "line"
                    },
                    {
                        "key": "info",
                        "Required": false,
                        "Type": "line"
                    }
                ],
                "People_Thoughts": [
                    "link"
                ]
            },
            "Overal_Description_Ru": {
                "About_Course_Title": "development",
                "About_Course_Image": "1",
                "Course_Advantages": [
                    "Good"
                ],
                "Title": "for everyone",
                "Description": "asds",
                "Image": "1",
                "Teachers": [
                    "id"
                ],
                "Syllabus_Title": "sintaksis",
                "Syllabus_Description": "asdas",
                "Duration": {
                    "Topics": "12",
                    "Projects": "2",
                    "Hours": "221"
                },
                "Module": {
                    "Title": "GOlang",
                    "Description": "hello world"
                },
                "Question": [
                    {
                        "key": "name",
                        "Required": false,
                        "Type": "line"
                    },
                    {
                        "key": "info",
                        "Required": false,
                        "Type": "line"
                    }
                ],
                "People_Thoughts": [
                    "wd",
                    "wesd"
                ]
            }
        });

        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };

        fetch("127.0.0.1:2442/course/add", requestOptions)
            .then((response) => response.text())
            .then((result) => console.log(result))
            .catch((error) => console.error(error));
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="name" value={name} onChange={(e) => { setName(e.target.value) }} />
                <input type="text" placeholder="deadline" value={deadline} onChange={(e) => setDeadline(e.target.value)} />
                <input type="text" placeholder="person" value={person} onChange={(e) => { setPerson(e.target.value) }} />
                <button>Submit</button>
            </form>


            {
                users.map(user => (
                    <div key={user._id}>
                        <h2>{user.name}</h2>
                        <p>{user.deadline}</p>
                        <p>{user.done}</p>
                    </div>
                ))
            }
        </div>
    )
}

export default Posting