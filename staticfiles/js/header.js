
const linkItem = document.querySelectorAll("a");
const iconBtn = document.querySelector(".icon-btn")
const navLinksAll = document.querySelector(".nav-links-all")

linkItem.forEach(link =>{
    link.addEventListener('click', function() {
        linkItem.forEach(activelink => activelink.classList.remove("active"))
        this.classList.add('active')
    })
})


iconBtn.addEventListener("click", function () {
  navLinksAll.classList.toggle("active");
  iconBtn.classList.toggle("active");
});


// window.addEventListener("scroll", () => {
//   const scrollY = window.pageYOffset;
//   container.forEach((current) => {
//     const containerHeight = current.offsetHeight;
//     const containerTop = current.offsetTop - 200;
//     const containerId = current.getAttribute("id");

//     if (scrollY > containerTop && scrollY < containerTop + containerHeight) {
//         document.querySelector('li a[href*="' + containerId+'"]').classList.add('active')
//     } else {
//         document.querySelector('li a[href*="' + containerId+'"]').classList.remove('active')
//     }
//   });
// });

