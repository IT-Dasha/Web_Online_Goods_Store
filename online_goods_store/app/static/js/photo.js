document.addEventListener('DOMContentLoaded', function() {
    var classButtons = document.getElementsByClassName('button_add_update_product');

    // Loop through all buttons and add click event listeners
    for (var i = 0; i < classButtons.length; i++) {
        classButtons[i].addEventListener('click', function() {
            this.style.top = '-993px'; // Change the position of the clicked button
        });
    }
    var dt = new DataTransfer();

    // Select the file input element
    var fileInput = document.querySelector('.input-file input[type=file]');
    var filesList = document.createElement('div'); // Create a container for the file list
    fileInput.parentNode.appendChild(filesList); // Append the file list container next to the input

    fileInput.addEventListener('change', function() {
        filesList.innerHTML = ''; // Clear the existing list

        for (var i = 0; i < this.files.length; i++) {
            let file = this.files.item(i);
            dt.items.add(file); // Add file to DataTransfer

            let reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = function() {
                let newFileInput = document.createElement('div');
                newFileInput.classList.add('input-file-list-item');
                
                newFileInput.innerHTML = `
                    <img class="input-file-list-img" src="${reader.result}">
                    <a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>
                `;
                
                filesList.appendChild(newFileInput); // Append the new file item
            }
        }

        this.files = dt.files; // Update the input's files
    });
});

// Function to remove files
function removeFilesItem(target) {
    let name = target.previousElementSibling.textContent; // Get the file name
    let input = target.closest('.input-file-row').querySelector('input[type=file]'); // Find the input

    target.closest('.input-file-list-item').remove(); // Remove the file item

    for (let i = 0; i < dt.items.length; i++) {
        if (name === dt.items[i].getAsFile().name) {
            dt.items.remove(i); // Remove the file from DataTransfer
        }
    }

    input.files = dt.files; // Update the input's files
}
