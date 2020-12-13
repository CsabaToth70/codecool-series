function init (){
    const inputButton = document.getElementById('add-year');
    inputButton.addEventListener('click', display_actors);
}

async function getYears(year) {
    const response = await fetch(`/year?year-input=${year}`);
    document.getElementById('actors-data').innerHTML = "";
    return await response.json();
}

async function display_actors(){
    let year = document.getElementById('year-input').value;
    let actorData = await getYears(year);
    let titleOfPage = document.getElementById('page-title');
    titleOfPage.textContent = "Actors of shows released in " + String(year).split('-')[0];
    let tableBody = document.getElementById('actors-data');
    for (let row of actorData) {
        if (row['is_older_actor']){
            tableBody.insertAdjacentHTML('beforeend',
                '<tr>' +
                '<td>' + row['name'] + '</td>' +
                '<td class="older">' + row['actor_age'] + '</td>' +
                '</tr>')
            } else {
            tableBody.insertAdjacentHTML('beforeend',
                '<tr>' +
                '<td>' + row['name'] + '</td>' +
                '<td>' + row['actor_age'] + '</td>' +
                '</tr>')
        }
    }
    // let olderButton = document.getElementById('older');
    // olderButton.addEventListener('click', displayOlder);
}

// async function displayOlder(event){
//
// }

init()