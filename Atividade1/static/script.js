document.addEventListener("visibilitychange", function() {
    var video = document.getElementById("backgroundVideo");
    if (document.hidden) {
        video.pause();
    } else {
        video.play();
    }
});

let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const visibleSlides = 3; // Número de slides visíveis de uma vez

    if (index >= totalSlides / visibleSlides) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = Math.floor((totalSlides - 1) / visibleSlides);
    } else {
        currentSlide = index;
    }

    const slider = document.querySelector('.slider');
    slider.style.transform = `translateX(-${currentSlide * 100 / visibleSlides}%)`;
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}
