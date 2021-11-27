function getUsers() {
    // fetch the server API info
    fetch("http://localhost:5000/api/users")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let userTable = document.querySelector("#users")
        userTable.innerHTML = "";

        for (const user of data.users) {
            let row = document.createElement("tr");
            let name = document.createElement("td");

            name.innerHTML = user.username;
            row.appendChild(name);

            let email = document.createElement("td");
            email.innerHTML = user.email;
            row.appendChild(email);

            userTable.appendChild(row);
        }
    })
}

getUsers()

let username = "";
let email = "";

function setUsername(ele) {
    username = ele.value;
}

function setEmail(ele) {
    email = ele.value;
}

function handleSubmit() {
    // handel the submit request as POST
    const options = {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            username: username,
            email: email
        })
    }

    fetch("http://localhost:5000/api/users/create", options)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // to echo the user list as default after submit request sent
            getUsers();
            // reset default to empty after submit
            // username = "";
            // email = "";
            document.querySelector("#username").value = "";
            document.querySelector("#email").value = "";
        })
}