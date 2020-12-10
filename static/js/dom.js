function init(){
    getBackground();
}

function getBackground (){
    let episodeValues = document.querySelectorAll(".episodes");
    for (let episodeValue of episodeValues){
        console.log(episodeValue.textContent);
        if (Number(episodeValue.textContent) % 2 === 0){
            episodeValue.parentElement.classList.add('even')
        } else {
            episodeValue.parentElement.classList.add('odd')
        }
    }
}

init()