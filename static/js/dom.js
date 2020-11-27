function init() {
    getPagination();
}


function getPagination() {
    const pageButtons = document.querySelectorAll('.pagination a');
    for (let pageButton of pageButtons) {
        pageButton.addEventListener('click', getNewPage)
    }

}

function getNewPage(event) {
    let newPage = event.currentTarget.textContent;
    let currentPage = document.querySelector('.active').textContent;
    const allPage = document.querySelector('.pagination').dataset.allPage;
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
            newPageNumber = Number(currentPage)
        }
    } else {
        newPageNumber = newPage;
    }
    goToNewPage(event, newPageNumber)
}


function goToNewPage(event, newPageNumber) {
    event.currentTarget.setAttribute('href', `?page=${newPageNumber}`);
}

init()

