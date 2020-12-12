function init(){
    let reportButton = document.getElementById('report');
    reportButton.addEventListener('click', displayActors);
}


async function getAge() {
    let startDate = document.getElementById('start').value;
    let endDate = document.getElementById('end').value;
    const response = await fetch(`/age?start-date=${startDate}&end-date=${endDate}`);
    return await response.json();
}

async function displayActors(event){
    let actorsData = await getAge();
    clearData()
    let tBody = document.getElementById('actor-data')
    for (let row of actorsData) {
        tBody.insertAdjacentHTML('beforeend',
            '<tr>' +
            '<td>' + row['age'] + '</td>' +
            '<td>' + row['name'] + '</td>' +
            '<td>' + row['count'] + '</td>' +
            '</tr>')
    }

}

function clearData(){
    let node = document.getElementById('actor-data');
    node.parentNode.replaceChild(node.cloneNode(false), node)
}


init()