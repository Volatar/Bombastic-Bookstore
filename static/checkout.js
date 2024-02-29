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
      passOrFailElement.style.color =
        data.passOrFail === "Pass" ? "green" : "red";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function submitAddress() {
  // Get form data
  var formData = new FormData(document.getElementById("address-form"));

  // Send form data asynchronously
  fetch("/process_address", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      // Update pass or fail message
      var passOrFailElement = document.getElementById("addressPassOrFail");
      passOrFailElement.textContent = data.passOrFail;
      passOrFailElement.style.color =
        data.passOrFail === "Pass" ? "green" : "red";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
