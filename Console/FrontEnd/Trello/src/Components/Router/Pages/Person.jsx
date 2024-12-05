import { UserArray } from "./Data"
import { useParams } from "react-router-dom"

const Person = () => {
    const item = UserArray.find(each => each.id == personId)
    console.log(item.id);


    const { personId } = useParams()
    return (
        <div >
            <h1>Hello</h1>
            <h2>{item.name}</h2>
            <p>{item.email}</p>
            <p>{item.phone}</p>
        </div>
    )
}

export default Person