import Home from "./Home"
import { UserArray } from "./Data"
import { Link } from "react-router-dom"
const Users = () => {
    return (
        <div>
            <Home />
            {
                UserArray.map((user) => {
                    return (
                        <div key={user.id}>
                            <Link to={`/people/${user.id}`}>
                                <h2>{user.name}</h2>
                            </Link>
                            <p>{user.email}</p>
                            <p>{user.phone}</p>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default Users