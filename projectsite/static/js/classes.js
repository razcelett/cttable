// Get the select menu element
var selectMenu = document.getElementById("select-menu");

// Add an event listener for when the selected value changes
selectMenu.addEventListener("change", function() {
  // Get the selected value
  var selectedValue = selectMenu.value;
  // If a page is selected, navigate to that page
  if (selectedValue !== "") {
    window.location.href = selectedValue;
  }
});
