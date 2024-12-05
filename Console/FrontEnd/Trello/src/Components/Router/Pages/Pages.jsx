import { createBrowserRouter, RouterProvider } from "react-router-dom"
import Home from "./Home"
import About from "./About"
import Services from "./Services"
import Users from "./Users"
import Person from "./Person"
import NotFound from "./NotFound"
const Customerouter = createBrowserRouter([
    {
        path: "",
        element: <Home />
    },
    {
        path: "/about",
        element: <About />
    },
    {
        path: "services",
        element: <Services />
    },
    {
        path: "user",
        element: <Users />
    },
    {
        path: "/people/:personID",
        element: <Person />
    },
    {
        path: "*",
        element: <NotFound />
    }
])
const Pages = () => {
    return (<RouterProvider router={Customerouter} />)

}

export default Pages