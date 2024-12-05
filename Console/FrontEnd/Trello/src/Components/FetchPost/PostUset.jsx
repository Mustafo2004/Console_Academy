import { useEffect, useState } from "react";

const PostUser = () => {
    const [userArray, setUserArray] = useState([]);
    const [name, setName] = useState("");
    const [surname, setSurname] = useState("");
    const [user_name, setUser_name] = useState("");
    const [address, setAddress] = useState("");
    const [phone_number, setPhone_number] = useState("");
    const [loading, setLoading] = useState(false);

    const API_URL = "https://66a7afc153c13f22a3d0b785.mockapi.io/api/media/Social";



    async function GetUser() {
        try {
            setLoading(true);
            const response = await fetch(API_URL);
            const data = await response.json();
            setUserArray(data);
        } catch (error) {
            console.log(error);
        }
        setLoading(false);
    }

    useEffect(() => {
        GetUser();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newUser = {
        
            name,
            surname,
            user_name,
            address,
            phone_number,
        };
        try {
            const response = await fetch(API_URL, {
                method: "POST",
                body: JSON.stringify(newUser),
                headers: {
                    "Content-Type": "application/json",
                },
            });
            const data = await response.json();
            setUserArray([...userArray, data]);
            setName("");
            setSurname("");
            setUser_name("");
            setAddress("");
            setPhone_number("");
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="name" value={name} onChange={(e) => setName(e.target.value)} />
                <input type="text" placeholder="surname" value={surname} onChange={(e) => setSurname(e.target.value)} />
                <input type="text" placeholder="user_name" value={user_name} onChange={(e) => setUser_name(e.target.value)} />
                <input type="text" placeholder="address" value={address} onChange={(e) => setAddress(e.target.value)} />
                <input type="text" placeholder="phone_number" value={phone_number} onChange={(e) => setPhone_number(e.target.value)} />
                <button type="submit">Submit</button>
            </form>
            <div>
                {loading ? <p>Loading</p> : null}
                {userArray.length === 0 && !loading ? <p>Cannot find</p> : null}
                {userArray.map((item) => (
                    <div key={item.id}>
                        <h2>{item.name}</h2>
                        <p>{item.surname}</p>
                        <p>{item.user_name}</p>
                        <p>{item.address}</p>
                        <p>{item.phone_number}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default PostUser;
