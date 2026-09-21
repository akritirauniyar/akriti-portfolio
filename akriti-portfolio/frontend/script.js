/* =========================
   TYPING ANIMATION
========================= */

const words = [
    "Data Scientist",
    "Machine Learning Enthusiast",
    "Data Analyst",
    "Python Developer"
];

let wordIndex = 0;
let charIndex = 0;
let deleting = false;

const typing = document.getElementById("typing");

function typeEffect() {

    const word = words[wordIndex];

    if (!deleting) {

        typing.textContent = word.substring(0, charIndex + 1);
        charIndex++;

        if (charIndex === word.length) {
            deleting = true;
            setTimeout(typeEffect, 1500);
            return;
        }

    } else {

        typing.textContent = word.substring(0, charIndex - 1);
        charIndex--;

        if (charIndex === 0) {
            deleting = false;
            wordIndex++;

            if (wordIndex === words.length) {
                wordIndex = 0;
            }
        }
    }

    setTimeout(typeEffect, deleting ? 50 : 100);
}

typeEffect();


/* =========================
   SCROLL REVEAL
========================= */

const reveals = document.querySelectorAll(".reveal");

function revealOnScroll() {

    reveals.forEach(element => {

        const windowHeight = window.innerHeight;

        const elementTop =
            element.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {
            element.classList.add("active");
        }

    });

}

window.addEventListener("scroll", revealOnScroll);

revealOnScroll();


/* =========================
   PARTICLE BACKGROUND
========================= */

const canvas = document.getElementById("particles");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

for (let i = 0; i < 80; i++) {

    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2,
        speedX: (Math.random() - .5) * .4,
        speedY: (Math.random() - .5) * .4
    });

}


function animateParticles() {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    particles.forEach(p => {

        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0 || p.x > canvas.width)
            p.speedX *= -1;

        if (p.y < 0 || p.y > canvas.height)
            p.speedY *= -1;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = "rgba(0,255,157,.5)";

        ctx.fill();

    });


    /* connect nearby particles */

    for (let i = 0; i < particles.length; i++) {

        for (let j = i + 1; j < particles.length; j++) {

            const dx =
                particles[i].x - particles[j].x;

            const dy =
                particles[i].y - particles[j].y;

            const distance =
                Math.sqrt(dx * dx + dy * dy);

            if (distance < 120) {

                ctx.beginPath();

                ctx.moveTo(
                    particles[i].x,
                    particles[i].y
                );

                ctx.lineTo(
                    particles[j].x,
                    particles[j].y
                );

                ctx.strokeStyle =
                    "rgba(0,255,157,.08)";

                ctx.stroke();
            }
        }
    }

    requestAnimationFrame(animateParticles);
}

animateParticles();

/* =========================
   CONTACT POPUP
========================= */

function openContact() {

    document.getElementById("contactModal").style.display = "flex";

}

function closeContact() {

    document.getElementById("contactModal").style.display = "none";

}


/* Close popup when clicking outside */

window.addEventListener("click", function(event) {

    const modal = document.getElementById("contactModal");

    if (event.target === modal) {

        closeContact();

    }

});


/* Resize */

window.addEventListener("resize", () => {

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

});