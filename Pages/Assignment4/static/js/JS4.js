
const userID = () => {
    console.log('check');
    const formInput = document.getElementById("frontend").user_id.value;
    fetch(` https://reqres.in/api/users/${formInput}`)
        .then((response) => response.json())
        .then((object) => {
            const data = object?.data;
            document.getElementById("Response").innerHTML =
                `
                    <br>
                    <h3>${data?.first_name} ${data?.lastname}</h3>
                    <h4>${data?.email}</h4>
                    <img src="${data?.avatar}" alt="Profile Picture"/>
                `
        })
        .catch((err) => console.log(err));
}