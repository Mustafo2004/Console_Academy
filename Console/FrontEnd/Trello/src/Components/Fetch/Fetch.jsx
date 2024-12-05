import { useEffect, useState } from "react";


const Fetch = () => {
    const [dataJson, setDataJson] = useState([]);

    const API_URL = "https://jsonplaceholder.typicode.com/users";

    // ! Get  ?
    useEffect(() => {
        async function GetUsers() {
            const response = await fetch(API_URL);
            const data = await response.json();
            setDataJson(data);
            console.log(data);
        }

        GetUsers();
    }, []);

    return (
        <div>
            {dataJson.map((item) => {
                return (
                    <div key={item.id}>
                        <h2>{item.name}</h2>
                        <p>{item.email}</p>
                        <p>{item.website}</p>
                    </div>
                )
            })}
            <h1>Fetch</h1>
        </div>
    )
}

export default Fetch;
