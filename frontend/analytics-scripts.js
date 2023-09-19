document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const youtuberName = urlParams.get('youtuber');

    if (youtuberName) {
        const header = document.querySelector('header h1');
        header.textContent = `${youtuberName}'s Analytics`;
    }
});
