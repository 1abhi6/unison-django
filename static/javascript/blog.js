// Responsive search Icon Popup 

let search_icon = document.querySelector('.search_icon');
let popup_bg = document.querySelector('.popup_bg');
let popup_close = document.querySelector('.popup_close');

search_icon.addEventListener('click', function () {
    popup_bg.classList.add('bg_active');
});
popup_close.addEventListener('click', function () {
    popup_bg.classList.remove('bg_active');
});


// JavaScript code for the search bar
function search_Blog() {
    let input = document.getElementById('searchbar').value
    input = input.toLowerCase();
    let x = document.getElementsByClassName('home_article');

    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display = "none";
        }
        else {
            x[i].style.display = "flex";

        }
    }
}

