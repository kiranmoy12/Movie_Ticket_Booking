document.addEventListener("DOMContentLoaded", function () {
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabs = document.querySelectorAll(".tab");

    tabButtons.forEach(button => {
        button.addEventListener("click", () => {
            // Remove all active classes
            tabButtons.forEach(btn => btn.classList.remove("active"));
            tabs.forEach(tab => tab.classList.remove("active"));

            // Add active to selected tab and corresponding content
            button.classList.add("active");
            const target = button.getAttribute("data-tab");
            document.getElementById(target).classList.add("active");
        });
    });
});
