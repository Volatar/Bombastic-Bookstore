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

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/filter_inventory");
            xhr.setRequestHeader("Content-Type", "application/json"); // Set the Content-Type header
            xhr.onload = function() {
    if (xhr.status === 200) {
        // Handle successful response
    } else {
        // Handle error
    }
};
xhr.send(JSON.stringify(jsonData));
</script>
