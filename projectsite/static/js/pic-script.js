const upload_form = document.querySelector("#upload_form");
const image_input = document.querySelector("#image_input");
const save_button = document.querySelector("#save_button");
const remove_button = document.querySelector("#remove_button");
const display_image = document.querySelector("#display_image");
const loading = document.querySelector("#loading");

// Check if profile picture exists in localStorage
if (localStorage.getItem("profile_picture")) {
    display_image.style.backgroundImage = localStorage.getItem("profile_picture");
}

image_input.addEventListener("change", function() {
    const file = image_input.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.addEventListener("load", function() {
        display_image.style.backgroundImage = `url(${reader.result})`;
    });
});

save_button.addEventListener("click", function() {
    if (display_image.style.backgroundImage !== "") {
        localStorage.setItem("profile_picture", display_image.style.backgroundImage);
        alert("Changes saved successfully!");
    } else {
        alert("Please select an image to save.");
    }
});

remove_button.addEventListener("click", function() {
    localStorage.removeItem("profile_picture");
    display_image.style.backgroundImage = "";
    image_input.value = "";
});
