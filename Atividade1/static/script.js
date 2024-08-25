document.addEventListener("visibilitychange", function() {
    var video = document.getElementById("backgroundVideo");
    if (document.hidden) {
        video.pause();
    } else {
        video.play();
    }
});
