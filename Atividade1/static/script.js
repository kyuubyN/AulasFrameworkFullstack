document.addEventListener("visibilitychange", function () {
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
    const visibleSlides = 2;

    let translateValue = window.innerWidth >= 300 && window.innerWidth <= 600 ? 210 : 50;

    if (index >= totalSlides / visibleSlides) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = Math.floor((totalSlides - 1) / visibleSlides);
    } else {
        currentSlide = index;
    }

    const slider = document.querySelector('.slider');
    slider.style.transform = `translateX(-${currentSlide * translateValue / visibleSlides}%)`;
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}
window.addEventListener('resize', () => {
    showSlide(currentSlide);
});



let currentSlide2 = 0;

function showSlide2(index) {
    const slides2 = document.querySelectorAll('.slide2');
    const totalSlides2 = slides2.length;
    const visibleSlides2 = 3;

    if (index >= totalSlides2 / visibleSlides2) {
        currentSlide2 = 0;
    } else if (index < 0) {
        currentSlide2 = Math.floor((totalSlides2 - 1) / visibleSlides2);
    } else {
        currentSlide2 = index;
    }

    const slider2 = document.querySelector('.slider2');
    slider2.style.transform = `translateX(-${currentSlide2 * 100 / visibleSlides2}%)`;
}

function nextSlide2() {
    showSlide2(currentSlide2 + 1);
}

function prevSlide2() {
    showSlide2(currentSlide2 - 1);
}

$('[name="estado"]').click(function () {

    $('[name="cidades"] option').css('display', 'none');

    $('[name="cidades"] .' + $(this).val()).css('display', '');

});