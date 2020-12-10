function init() {
    const ageButton = document.getElementById("get-years");
    ageButton.addEventListener('click', displayActors);
}

async function getAge() {
    const start_date = document.getElementById('start-field').value;
    const end_date = document.getElementById('end-field').value;
    const response = await fetch(`/age?start-date=${start_date}&end-date=${end_date}`);
    return await response.json();
}

async function displayActors() {
    const actor_data = await getAge();
    const tBody = document.getElementById("table-body");
    for (let row of actor_data) {
        tBody.insertAdjacentHTML('beforeend',
            '<tr>' +
            '<td>' + row['name'] + '</td>' +
            '<td>' + row['age'] + '</td>' +
            '<td>' + row['count'] + '</td>' +
            '</tr>')
    }
}

init()