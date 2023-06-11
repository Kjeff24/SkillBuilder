
const linkItem = document.querySelectorAll(".side-bar-content-row")
const iconBtn = document.querySelector(".icon-btn")
const navLinksAll = document.querySelector(".nav-links-all")
const navLinks = document.querySelectorAll(".nav-links")


iconBtn.addEventListener("click", function () {
  navLinksAll.classList.toggle("active");
  iconBtn.classList.toggle("active");
});// Handle download increment
// Get all the download links
var downloadLinks = document.querySelectorAll(".download-link");


// Iterate over each download link
downloadLinks.forEach(function (link) {
    // Add click event listener
    link.addEventListener("click", function (event) {
        

        // Get the file ID from the link's href attribute
        var fileID = link.getAttribute("data-file-id");

        // Call the increaseDownload view using AJAX
        fetch("/resource/" + fileID + "/download/")
            .then(function (response) {
                if (response.ok) {
                    // Perform any additional actions after the download is incremented
                    // ...
                } else {
                    console.error("Error: " + response.status);
                }
            })
            .catch(function (error) {
                console.error("Error: " + error);
            });
    });
});


