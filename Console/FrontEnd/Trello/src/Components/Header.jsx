import { Link, } from "react-router-dom"

const Header = () => {
    return (
        <div>
            <ul>
                <Link to={"/"}  >Home</Link>
                <Link to={"/about"}>About</Link>
                <Link to={"/services"}>Services</Link>
                <Link to={"/user"}>User</Link>
            </ul>
        </div>
    )
}

export default Header