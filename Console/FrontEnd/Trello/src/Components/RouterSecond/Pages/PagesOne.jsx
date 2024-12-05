import { createBrowserRouter, RouterProvider } from "react-router-dom"
import Home from "./Home"
import About from "./About"
import Users from "./Users"
import Odam from "./Odam"

const CustomerRouter = createBrowserRouter([
    {
        path: "",
        element: <Home />
    },
    {
        path: "/about",
        element: <About />
    },
    {
        path: "/user",
        element: <Users />
    },
    {
        path: "/odam/:personID",
        element: <Odam />
    }

])
const PagesOne = () => {
    return (<RouterProvider router={CustomerRouter} />)
}

export default PagesOne
