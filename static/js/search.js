function init() {
    let inputButton = document.getElementById('input-button');
    inputButton.addEventListener('click', displayResults);
}

async function searchText(inputText) {
    const response = await fetch(`/search-input?input-text=${inputText}`);
    document.getElementById('findings').innerHTML = "";
    return await response.json();
}

async function displayResults() {
    let inputText = document.getElementById('searching').value;
    let resultList = await searchText(inputText)
    let uList = document.getElementById('findings');
    for (const row of resultList) {
        uList.insertAdjacentHTML('beforeend',
            '<li>' + row['name'] + ' played ' + row['character_name'] +
            ' in ' + row['title'] + '</li>'
        );
    }
}

init()