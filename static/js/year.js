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
                '<tr ' + 'class=\"trow\" ' +
                'data-actor-age-released=\"' + row['age_actor_at_release'] +
                '\" ' + 'data-show-age=\"' + row['age_of_show'] + '\"' + '>' +
                '<td>' + row['name'] + '</td>' +
                '<td class="older">' + row['actor_age'] + '</td>' +
                '</tr>')
            } else {
            tableBody.insertAdjacentHTML('beforeend',
                '<tr ' + 'class=\"trow\" ' +
                'data-actor-age-released=\"' + row['age_actor_at_release'] +
                '\" ' + 'data-show-age=\"' + row['age_of_show'] + '\"' + '>' +
                '<td>' + row['name'] + '</td>' +
                '<td>' + row['actor_age'] + '</td>' +
                '</tr>')
        }
    }
    let rowSigns = document.querySelectorAll('.trow');
    for (let rowSign of rowSigns) {
        rowSign.addEventListener('click', popUpInfo);
    }
}

function popUpInfo(event) {
    let actorAgeAtShow = event.currentTarget.dataset.actorAgeReleased;
    let ageOfShow = event.currentTarget.dataset.showAge;
    let infoToAlert = 'Actor age at show released: ' + actorAgeAtShow + ' years' + '\n' +
        'Age of the show: ' + ageOfShow + ' years';
    alert(infoToAlert);
}

init()