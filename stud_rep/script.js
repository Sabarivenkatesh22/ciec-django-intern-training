document.getElementById("apiForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {
        first_name: formData.get("firstName"),
        last_name: formData.get("lastName"),
        email_id: formData.get("email")
    };

    fetch("http:localhost:8000/create_student", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
