document.addEventListener('DOMContentLoaded', function() {
    function getQueryParam(name) {
        const url = new URL(window.location.href);
        return url.searchParams.get(name);
    }

    const youtuberName = getQueryParam("username");
    if (youtuberName) {
        document.getElementById("youtuberNameDisplay").textContent = "Data for: " + decodeURIComponent(youtuberName);
    }

    // The rest of your analytics related code should go below
});
