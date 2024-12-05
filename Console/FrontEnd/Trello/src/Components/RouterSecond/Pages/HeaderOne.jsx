import { Link } from "react-router-dom"

const HeaderOne = () => {
    return (
        <div>
            <ul>
                <Link to={"/"}>Home</Link>
                <Link to={"/about"}>About</Link>
                <Link to={"/user"}>User</Link>
            </ul>
        </div>
    )
}

export default HeaderOne
