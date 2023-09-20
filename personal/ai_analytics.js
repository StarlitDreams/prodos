document.addEventListener("DOMContentLoaded", function() {
    fetch('backend/output.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        document.getElementById('chatgpt-output').textContent = data;
    })
    .catch(error => {
        console.error('There was a problem fetching the data:', error);
        document.getElementById('chatgpt-output').textContent = 'Error fetching data.';
    });
});
