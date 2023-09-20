document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const inputValue = document.getElementById('searchInput').value;
    // Append the input value as a query parameter and reload the page
    window.location.href = window.location.origin + window.location.pathname + '?youtuber=' + encodeURIComponent(inputValue);
});
