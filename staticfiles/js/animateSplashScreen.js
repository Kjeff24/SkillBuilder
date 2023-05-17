const messages = [
    {
        title: "Welcome to our employee training program!",
        message:
            "Get ready to dive into a world of knowledge and growth as we help you level up your skills and prepare you for success.",
        image: "../assets/splash1.jpg",
    },
    {
        title: "Stay up-to-date",
        message:
            "Our training program is tailored to meet the needs of employees at all levels of the organization, from entry-level to senior management.",
        image: "../assets/splash2.jpg",
    },
    {
        title: "Learn something new",
        message:
            "Our interactive training modules are designed to be engaging and practical, allowing you to apply your learning in real-world situations.",
        image: "../assets/splash3.jpg",
    },
    {
        title: "The perfect Employee",
        message:
            "We're committed to your success and believe that investing in employee training is critical to the growth and success of our organization.",
        image: "../assets/splash4.jpg",
    },
];

const titleElement = document.querySelector(".splash-heading");
const messageElement = document.querySelector(".splash-body");
const imageElement = document.querySelector(".splash-img");

let currentMessageIndex = 0;

window.addEventListener("DOMContentLoaded", function () {
    showSplash(currentMessageIndex);
});

function showSplash(messageIndex) {
    // update the message
    titleElement.textContent = messages[messageIndex].title;
    messageElement.textContent = messages[messageIndex].message;
    imageElement.src = messages[messageIndex].image;
	
}

function addClassAnimate(){
	titleElement.classList.add("show");
	messageElement.classList.add("show");
	imageElement.classList.add("show");
}

function removeClassAnimate(){
	titleElement.classList.remove("show");
	messageElement.classList.remove("show");
	imageElement.classList.remove("show");
}

function animateDiv() {
	addClassAnimate()
	showSplash(currentMessageIndex)
	currentMessageIndex = (currentMessageIndex + 1) % messages.length;
	setTimeout(function() {
		removeClassAnimate()
	}, 1000);
  }

  setInterval(animateDiv, 8000);
