console.log("Script loaded successfully");

document.addEventListener("DOMContentLoaded", function() {
    var imageElement = document.getElementById("demo");
    if (!imageElement) return;

    var images = [];
    try {
        images = JSON.parse(imageElement.getAttribute("data-images"));
    } catch (e) {
        console.error("Could not parse image list", e);
        return;
    }
    var currentImageIndex = 0;
    var intervalStarted = false;
    var intervalId = null;

    imageElement.addEventListener("click", function() {
        if (intervalStarted) return; // Prevent multiple intervals
        intervalStarted = true;
        intervalId = setInterval(function() {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            imageElement.src = images[currentImageIndex];
            console.log("image changed");
        }, 2000);
        imageElement.src = images[currentImageIndex];
    });
});
