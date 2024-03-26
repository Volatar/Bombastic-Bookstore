<!-- Add this form to allow users to enter filtering criteria -->
<form id="filterForm">
    <input type="text" name="title" placeholder="Title">
    <input type="text" name="author" placeholder="Author">
    <!-- Add more input fields for other filtering criteria as needed -->

    <button type="submit">Filter</button>
</form>

<script>
    // Function to handle form submission
    document.getElementById("filterForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Get form data
        var formData = new FormData(this);

        // Convert form data to JSON object
        var jsonData = {};
        formData.forEach(function(value, key) {
            jsonData[key] = value;
        });

        // Send AJAX request to Flask backend
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/filter_inventory");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Update HTML with filtered inventory data
                var filteredInventory = JSON.parse(xhr.responseText);
                // Code to update HTML with filtered inventory data goes here
            } else {
                console.error("Error:", xhr.statusText);
            }
        };
        xhr.onerror = function() {
            console.error("Network Error");
        };
        xhr.send(JSON.stringify(jsonData));
    });
</script>
