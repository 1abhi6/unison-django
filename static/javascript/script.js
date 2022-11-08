
// // Initialize Swiper 
// var swiper = new Swiper(".mySwiper", {
//     // spaceBetween: 30,
//     centeredSlides: true,
//     autoplay: {
//         delay: 3500,
//         disableOnInteraction: false
//     }
// });



// Search Bar 

// const searchBlog = () => {
//     // debugger;
//     let filter = document.getElementById('searchInput').value.toUpperCase();
//     let main_articles_div = document.getElementById('main_articles_div');
//     let a = main_articles_div.getElementsByTagName('a');
//     let child_article_div = a.getElementById('child_article_div');

//     for (var i = 0; i < child_article_div.length; i++) {
//         let h3 = child_article_div[i].getElementsByTagName('h3')[0];

//         let textValue = h3.textContent || a.innerHTML;

//         if (textValue.toUpperCase().indexOf(filter) >= -1) {
//             child_article_div[i].style.color = "blue";
//             // console.log("Success");

//         }
//         else {
//             child_article_div[i].style.display = "none";
//             // console.log("Failure");

//         }
//     }
// }

// let search=document.getElementById('search');
// search.addEventListener('click', searchBlog);
// searchBlog();
// onkeyup="searchBlog"



