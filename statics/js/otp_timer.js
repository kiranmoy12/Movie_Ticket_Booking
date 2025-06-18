document.addEventListener("DOMContentLoaded", function () {
    const countdownElem = document.getElementById("countdown");
    const resendBtn = document.getElementById("resendBtn");
    let secondsLeft = parseInt(countdownElem.getAttribute("data-time"));

    function updateCountdown() {
        const minutes = Math.floor(secondsLeft / 60);
        const seconds = secondsLeft % 60;
        countdownElem.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        if (secondsLeft <= 0) {
            clearInterval(timer);
            countdownElem.textContent = "00:00";
            resendBtn.style.pointerEvents = "auto";
            resendBtn.style.color = "#007BFF";  // make it look active
        }

        secondsLeft--;
    }

    updateCountdown(); // initial display
    const timer = setInterval(updateCountdown, 1000);
});
