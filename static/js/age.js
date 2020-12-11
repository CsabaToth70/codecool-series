function init(){
    let dateButton = document.getElementById('report');
    dateButton.addEventListener('click', display_actors)
}

async function get_actors_ages(startDate, endDate) {
    const response = await fetch(`/age?start-date=${startDate}&end-date=${endDate}`);
    return await response.json();
}

async function display_actors(event){
    let startDate = document.getElementById('start-date').value;
    let endDate = document.getElementById('end-date').value;
    let dataSheet = await get_actors_ages(startDate, endDate)
    const tableActors = document.getElementById('actor-table')
    for (let row of dataSheet){
        tableActors.insertAdjacentHTML('beforeend',
        '<tr>' +
        '<td>' + row['name'] + '</td>' +
        '<td>' + row['age'] + '</td>' +
        '<td>' + row['count'] + '</td>' +
        '</tr>')
    }
}

init()