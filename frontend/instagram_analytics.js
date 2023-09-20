document.addEventListener('DOMContentLoaded', function() {
    function getQueryParam(name) {
        const url = new URL(window.location.href);
        return url.searchParams.get(name);
    }

    const instagramUsername = getQueryParam("username");
    if (instagramUsername) {
        document.getElementById("instagramUsernameDisplay").textContent = "Data for: " + decodeURIComponent(instagramUsername);
    }

    // Any other Instagram-specific analytics code should go below
});
