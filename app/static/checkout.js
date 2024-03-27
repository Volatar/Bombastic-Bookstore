document.getElementById("orderNowButton").addEventListener("click", function() {
  window.location.href = "receipt.html"; // Redirect to receipt.html 
});

function submitForm() {
  // Get form data
  var formData = new FormData(document.getElementById("payment-form"));

  // Send form data asynchronously
  fetch("/process_payment", {
      method: "POST",
      body: formData,
  })
  .then((response) => response.json())
  .then((data) => {
      // Update pass or fail message
      var passOrFailElement = document.getElementById("passOrFail");
      passOrFailElement.textContent = data.passOrFail;
      passOrFailElement.style.color = data.passOrFail === "Pass" ? "green" : "red";

      // Show or hide the "Order Now" button based on the result
      var orderNowButton = document.getElementById("orderNowButton");
      if (data.passOrFail === "Pass") {
          orderNowButton.style.display = "block"; // Show the button
      } else {
          orderNowButton.style.display = "none"; // Hide the button
      }
  })
  .catch((error) => {
      console.error("Error:", error);
  });
}
