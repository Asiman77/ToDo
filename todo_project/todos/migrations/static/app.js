const apiUrl = "http://localhost:8000/todos/";

document.addEventListener("DOMContentLoaded", fetchTodos);

document.getElementById("todo-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: title, description: description }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Todo added:", data);
        fetchTodos();
    })
    .catch(error => console.error("Error:", error));
});

function fetchTodos() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const todoList = document.getElementById("todo-list");
            todoList.innerHTML = "";
            data.forEach(todo => {
                const li = document.createElement("li");
                li.textContent = `${todo.title}: ${todo.description}`;
                todoList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching todos:", error));
}
