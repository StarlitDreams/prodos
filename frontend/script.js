// Function to simulate fetching data and redirecting to the analytics page
function fetchData() {
    console.log('Fetching data...');
    const youtuberNameInput = document.querySelector('.search-container input');
    const youtuberName = youtuberNameInput.value;

    if (!youtuberName.trim()) { // Check if input is empty or just whitespace
        youtuberNameInput.value = "Error: Please type a name!";
        youtuberNameInput.style.color = "red"; // Change text color to red for the error message
        document.querySelector('.loading-scene').style.display = 'none'; // Hide loading screen
        return;
    }

    console.log(`Fetching data for: ${youtuberName}`);
    
    // Simulate a delay for fetching data
    setTimeout(function() {
        // Redirect to the analytics page after the delay with the YouTuber's name as a query parameter
        window.location.href = `analytics.html?youtuber=${encodeURIComponent(youtuberName)}`; 
    }, 3000); // 3 seconds delay for demonstration. Adjust as needed.
}

// Function to handle the search button click
function handleSearchClick(event) {
    event.preventDefault(); // Prevent any default action

    // Display the loading scene
    document.querySelector('.loading-scene').style.display = 'flex';

    // Fetch data (simulated) and then redirect
    fetchData();
}

// Event listener for the search button
document.querySelector('.search-container button').addEventListener('click', handleSearchClick);

// Function to hide the logo animation after a delay
function hideLogoAnimation() {
    setTimeout(function() {
        const logoAnim = document.querySelector('.logo-animation');
        logoAnim.style.display = 'none';
    }, 3000); // 3 seconds delay to match the CSS fadeOut animation
}

// Call the function to hide the logo animation on document load
document.addEventListener("DOMContentLoaded", hideLogoAnimation);

