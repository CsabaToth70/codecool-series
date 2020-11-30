function init() {
    placeListeners();
}

function placeListeners() {
    const pageButtons = document.querySelectorAll('.pagination a');
    const headlines = document.querySelectorAll('.headline th a');
    for (let pageButton of pageButtons) {
        pageButton.addEventListener('click', getNewPage);
    }
    for (let headline of headlines) {
        headline.addEventListener('click', getNewOrder);
    }
}

function getDirection(directionText) {
    if (directionText === "true") {
        return true
    } else if (directionText === "false") {
        return false
    } else {
        return true
    }
}

function setUpNewOrder(actual_aspect, actual_direction, newSignal) {
    let direction = true;
    if (actual_aspect === newSignal && actual_direction) {
        direction = false;
    }
    return direction
}

function getNewOrder(event) {
    let newSignal = event.currentTarget.dataset.shortName;
    let actual_aspect = document.querySelector('.headline').dataset.aspect;
    let directionText = document.querySelector('.headline').dataset.direction;
    let actual_direction = getDirection(directionText);
    let direction = setUpNewOrder(actual_aspect, actual_direction, newSignal);
    goToSortedPage(event, newSignal, direction, 1);
}

function goToSortedPage(event, aspect, direction, newPageNumber = 1) {
    event.currentTarget.setAttribute('href', `?aspect=${aspect}&direction=${direction}&page=${newPageNumber}`);
}

function getNewPage(event) {
    let newPage = event.currentTarget.textContent;
    let currentPage = document.querySelector('.active').textContent;
    const allPage = document.querySelector('.pagination').dataset.allPage;
    let aspect = document.querySelector('.headline').dataset.aspect;
    let direction = document.querySelector('.headline').dataset.direction;
    let newPageNumber = "";
    if (newPage === '«') {
        if (currentPage !== '1') {
            newPageNumber = Number(currentPage) - 1;
        } else {
            newPageNumber = Number(currentPage)
        }
    } else if (newPage === '»') {
        if (currentPage !== allPage) {
            newPageNumber = Number(currentPage) + 1;
        } else {
            newPageNumber = Number(currentPage);
        }
    } else {
        newPageNumber = newPage;
    }
    goToNewPage(event, aspect, direction, newPageNumber);
}

function goToNewPage(event, aspect, direction, newPageNumber) {
    event.currentTarget.setAttribute('href', `?aspect=${aspect}&direction=${direction}&page=${newPageNumber}`);
}

init()
