document.addEventListener("DOMContentLoaded", function () {
    // Select all external links
    const externalLinks = document.querySelectorAll('a[href^="http"]');

    externalLinks.forEach(link => {
        link.setAttribute('target', '_blank');
    });
});
