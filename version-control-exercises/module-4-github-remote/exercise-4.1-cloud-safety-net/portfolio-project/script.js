/**
 * Portfolio — Simple interactive behaviors.
 */

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        var targetId = this.getAttribute("href");
        var target = document.querySelector(targetId);
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});

// Add animation class when sections scroll into view
function revealOnScroll() {
    var sections = document.querySelectorAll("section");
    var windowHeight = window.innerHeight;

    sections.forEach(function (section) {
        var sectionTop = section.getBoundingClientRect().top;
        if (sectionTop < windowHeight - 100) {
            section.classList.add("visible");
        }
    });
}

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

// Log page load (for development)
console.log("Portfolio loaded successfully.");
console.log("Built with vanilla HTML, CSS, and JavaScript.");
