document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.search-option');
    var input = document.getElementById('searchKeyword');
  
    buttons.forEach(function(button) {
      button.addEventListener('click', function() {
        // Deactivate all buttons
        buttons.forEach(function(btn) { btn.classList.remove('active'); });
        // Activate clicked button
        this.classList.add('active');
        // Change input placeholder
        input.placeholder = this.getAttribute('data-placeholder');
      });
    });
  });