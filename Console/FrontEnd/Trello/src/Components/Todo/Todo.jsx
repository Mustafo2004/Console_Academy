import { useEffect, useState } from "react";

const Todo = () => {
    const [tasks, setTasks] = useState("");
    const [calendar, setCalendar] = useState("");
    const [owner, setOwner] = useState("");
    const [message, setMessage] = useState("");
    const [backlogArray, setBacklogArray] = useState([]);
    const [ToDoArray, setTodoArray] = useState([]);
    const [testingArray, setTestingArray] = useState([]);
    const [doneArray, setDoneArray] = useState([]);
    const handleButton = () => {
        if (tasks.trim() === "" || calendar.trim() === "" || owner.trim() === "" || message.trim() === "") return;
        const newTask = {
            id: Date.now(),
            tasks: tasks,
            calendar: calendar,
            owner: owner,
            message: message
        };
        setBacklogArray([...backlogArray, newTask]);
        setTasks("");
        setCalendar("");
        setOwner("");
        setMessage("");
    };
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/tasks.json'); 
                const data = await response.json();
                setBacklogArray(data.backlog || []);
                setTodoArray(data.todo || []);
                setTestingArray(data.testing || []);
                setDoneArray(data.done || []);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);


    const moveTask = (task, fromArray, setFromArray, toArray, setToArray) => {
        setFromArray(fromArray.filter(item => item.id !== task.id));
        setToArray([...toArray, task]);
    };
    const handleDelete = (id) => {
        const update = setDoneArray(doneArray.filter(item => item.id !== id))
        setDoneArray(update)
    }


    return (
        <>
            <div className="flex items-center justify-center flex-col">
                <h1 className="font-bold text-[30px] m-[20px]">Task Management</h1>
                <div>
                    <input
                        value={tasks}
                        onChange={(e) => setTasks(e.target.value)}
                        type="text"
                        placeholder="Add new task"
                        className="border w-[520px] h-[50px] p-[20px] rounded-xl"
                    />
                    <div className="flex items-center justify-center gap-5">
                        <input
                            value={calendar}
                            onChange={(e) => setCalendar(e.target.value)}
                            type="datetime-local"
                            className="border w-[250px] h-[50px] p-[20px] my-[20px]"
                        />
                        <select
                            value={owner}
                            onChange={(e) => setOwner(e.target.value)}
                            className="border w-[250px] h-[50px] my-[20px]"
                        >
                            <option value="">Select Owner</option>
                            <option value="Mustafo">Mustafo</option>
                            <option value="Jahongir">Jahongir</option>
                            <option value="Sayod">Sayod</option>
                            <option value="Amina">Amina</option>
                            <option value="Hasan">Hasan</option>
                        </select>
                    </div>
                    {/* <input
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        className="border w-[520px] h-[240px] text-red-700"
                        placeholder="Task Description"
                    /> */}
                    <textarea className="border resize-none w-[520px] h-[240px] text-red-700" onChange={(e) => setMessage(e.target.value)} value={message} name="message" id="1" placeholder="task description">

                    </textarea>
                </div>
                <button onClick={handleButton} className="border w-[520px] mt-5 rounded-xl bg-black text-white h-[60px] mb-7">Add new Task</button>
            </div>
            <div className="flex items-start justify-between">
                <div className="border-[5px] border-black rounded-xl min-w-[400px] min-h-[300px] p-[20px] flex-col flex items-center gap-2 justify-center">
                    <h1 className="ml-5 font-semibold text-[20px]">Backlog</h1>
                    {backlogArray.map((item) => (
                        <div key={item.id} className="border w-[350px] h-[250px] p-[20px] bg-blue-400 rounded-2xl">
                            <p className="m-[10px]">{item.tasks}</p>
                            <p>{item.message}</p>
                            <button onClick={() => moveTask(item, backlogArray, setBacklogArray, ToDoArray, setTodoArray)} className="border p-[10px] bg-black text-white rounded-xl">Move to To Do</button>
                            <div>
                                <p>Deadline: {item.calendar}</p>
                                <p>Person: {item.owner}</p>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="border-[5px] border-black rounded-xl w-[400px] h-[300px] flex flex-col items-center justify-center">
                    <h1 className="ml-5 font-semibold text-[20px]">To Do</h1>
                    {ToDoArray.map((item) => (
                        <div key={item.id} className="border w-[350px] h-[250px] p-[20px] bg-blue-400 rounded-2xl">
                            <p className="m-[10px]">{item.tasks}</p>
                            <p>{item.message}</p>
                            <button onClick={() => moveTask(item, ToDoArray, setTodoArray, testingArray, setTestingArray)} className="border p-[10px] bg-black text-white rounded-xl">Move to Testing</button>
                            <div>
                                <p>Deadline: {item.calendar}</p>
                                <p>Person: {item.owner}</p>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="border-[5px] border-black rounded-xl w-[400px] h-[300px] flex flex-col items-center justify-center">
                    <h1 className="ml-5 font-semibold text-[20px]">Testing</h1>
                    {testingArray.map((item) => (
                        <div key={item.id} className="border w-[350px] h-[250px] p-[20px] bg-blue-400 rounded-2xl">
                            <p className="m-[10px]">{item.tasks}</p>
                            <p>{item.message}</p>
                            <button onClick={() => moveTask(item, testingArray, setTestingArray, doneArray, setDoneArray)} className="border p-[10px] bg-black text-white rounded-xl">Move to Done</button>
                            <div>
                                <p>Deadline: {item.calendar}</p>
                                <p>Person: {item.owner}</p>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="border-[5px] border-black rounded-xl min-w-[400px] min-h-[300px] flex flex-col items-center justify-center">
                    <h1 className="ml-5 font-semibold text-[20px]">Done</h1>
                    {doneArray.map((item) => (
                        <div key={item.id} className="border w-[350px] h-[250px] p-[20px] bg-blue-400 rounded-2xl">
                            <p className="m-[10px]">{item.tasks}</p>
                            <p>{item.message}</p>
                            <button onClick={() => handleDelete(item.id)}>Delete</button>
                            <div>
                                <p>Deadline: {item.calendar}</p>
                                <p>Person: {item.owner}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
};

export default Todo;
