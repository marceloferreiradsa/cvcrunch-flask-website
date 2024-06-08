// Disable scrolling with mouse wheel and touchpad'
window.addEventListener('wheel', preventScroll, {passive: false});

function preventScroll(e) {
    e.preventDefault();
    e.stopPropagation();

    return false;
}

// Optional: Disable scrolling with keys (like arrow keys, spacebar, page up/down)
window.addEventListener('keydown', function(e) {
    // List of keys that can cause scrolling
    const keys = {ArrowLeft: 1, ArrowUp: 1, ArrowRight: 1, ArrowDown: 1, Space: 1, PageDown: 1, PageUp: 1};
    if (keys[e.key]) {
        preventScroll(e);
    }
});

/*
$(document).ready(function(){
    // Initialize Dropzone
    Dropzone.autoDiscover = false;
    var myDropzone = new Dropzone("#my-dropzone", {
        url: "/upload",
        acceptedFiles: ".txt,.pdf,.docx", // Specify accepted file types
        maxFilesize: 5, // Maximum file size in MB
        dictDefaultMessage: "Drag and drop or click here to upload your resume", // Custom message
        maxFiles: 1,
        // Other Dropzone options...
    });

    // Add event listener for invalid file type
    myDropzone.on("error", function(file, errorMessage) {
        if (errorMessage === "You can't upload files of this type.") {
            alert("Please upload only PDF or DOCX files.");
            this.removeFile(file); // Remove the invalid file from Dropzone
        }
    });
});

*/

$(document).ready(function(){
    // Initialize Dropzone
    Dropzone.autoDiscover = false;
    var csrfToken = $("meta[name='csrf-token']").attr("content"); // Get the CSRF token from the meta tag

    var myDropzone = new Dropzone("#my-dropzone", {
        url: "/upload",
        acceptedFiles: ".txt,.pdf,.docx", // Specify accepted file types
        maxFilesize: 5, // Maximum file size in MB
        dictDefaultMessage: "Drag and drop or click here to upload your resume", // Custom message
        maxFiles: 1,
        // Other Dropzone options...
        sending: function(file, xhr, formData) {
            formData.append("csrf_token", csrfToken); // Append the CSRF token to formData
        }
    });

    // Add event listener for invalid file type
    myDropzone.on("error", function(file, errorMessage) {
        if (errorMessage === "You can't upload files of this type.") {
            alert("Please upload only PDF or DOCX files.");
            this.removeFile(file); // Remove the invalid file from Dropzone
        }
    });
});

document.addEventListener('keydown', function(event) {
    // Check if the key press is 'V' and if the CTRL or Command key is pressed
    if ((event.ctrlKey || event.metaKey) && event.key === 'v') {
        // Focus the text area
        document.getElementById('textPasteArea').focus();
    }
});
   
function displayMessage(message) {
    var messageElement = document.getElementById('messageArea'); // Assume there is an HTML element with this ID where messages are displayed
    messageElement.textContent = message; // Sets the text of the message element to the provided message
    messageElement.style.display = 'block'; // Makes sure the message is visible
    // Add the blink class to the message element
messageElement.classList.add('blink');

// Remove the blink class after 3 seconds (enough time for a few blinks)
setTimeout(() => {
    messageElement.classList.remove('blink');
}, 500);
}; 

document.addEventListener('DOMContentLoaded', function() {
    var step1Btn = document.getElementById('step1-btn');
    if (step1Btn) {
        step1Btn.addEventListener('click', function() {
            scrollToSection('step2');
        });
    }
});
document.getElementById('forw-step3-btn').addEventListener('click', async function() { // Note the async keyword
    var textArea = document.getElementById('textPasteArea');
    var text = textArea.value;

    // Show loading message or spinner
    displayMessage('Processing... Please wait.');

    try {
        // First, process the text
        let textResponse = await fetch('/textPaste', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({text: text}),
        });
        let textData = await textResponse.json();
        displayMessage('Text successfully processed');

        // Now call the API
        let apiResponse = await fetch('/apiCall', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({text: 'API Called!'}),
        });
        let apiData = await apiResponse.json();
        displayMessage('API call successfully processed');

        // Fetch and display results from the final API call
        let finalResponse = await fetch('/report'); // Make sure this should be an await if you are expecting to wait for the result
        let finalData = await finalResponse.json();  // Convert the response to JSON
        console.log(finalData);  // For example, log the data
        displayContent(finalData);
        // // If you want to display this data in HTML, you can insert it into the DOM
        // document.getElementById('yourElementId').innerHTML = JSON.stringify(finalData, null, 2).replace(/\n/g, '<br>');
        // // Inserting the fetched data into the placeholders
        // document.getElementById('content').innerHTML = finalData.content; // Assumes 'finalData.content' contains HTML-ready content
        // document.getElementById('role').textContent = finalData.role;
        // // Change the section heading to reflect the new status
        // document.querySelector('#step4 h2').textContent = 'Analysis Results';

    } catch (error) {
        console.error('Error:', error);
        displayMessage('Error processing request');
    }
});

function displayContent(data) {
    // Here we parse the 'content' to make it more readable and split into sections
    const contentSections = data.content.split('\n').filter(section => section.trim() !== '');
    let formattedContent = '';

    contentSections.forEach((section, index) => {
        if (section.includes('/100')) {
            // This is a section header
            formattedContent += `<h3>${section}</h3>`;
        } else {
            // This is a section body
            formattedContent += `<p>${section}</p>`;
        }
    });

    document.getElementById('content').innerHTML = formattedContent;
    document.getElementById('role').textContent = data.role;
}

document.getElementById('forw-step2-btn').addEventListener('click', function() {
    scrollToSection('step3');
});

document.getElementById('back-step2-btn').addEventListener('click', function() {
    scrollToSection('step1');
});

function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' })
};
    
document.getElementById('forw-step3-btn').addEventListener('click', function() {
    scrollToSection('step4');
});

document.getElementById('back-step3-btn').addEventListener('click', function() {
    scrollToSection('step2');
});

document.getElementById('back-step4-btn').addEventListener('click', function() {
    scrollToSection('step3');
});

function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' })
};

// Function to check if there are any files in the Dropzone area
function hasFilesInDropzone() {
    return myDropzone.getQueuedFiles().length > 0;
}
/*
document.getElementById('login').addEventListener('click', function() {
    window.location.href = this.getAttribute('data-url');
});

document.getElementById('signup').addEventListener('click', function() {
    window.location.href = this.getAttribute('data-url');
});
*/
document.addEventListener('DOMContentLoaded', function() {
    var loginButton = document.getElementById('login');
    if (loginButton) {
        loginButton.addEventListener('click', function() {
            window.location.href = this.getAttribute('data-url');
        });
    }

    var signupButton = document.getElementById('signup');
    if (signupButton) {
        signupButton.addEventListener('click', function() {
            window.location.href = this.getAttribute('data-url');
        });
    }

    var signupEmail = document.getElementById('alert-box-email');
    if (signupEmail) {
        signupEmail.addEventListener('input'), function(){
            console.log('input event triggered');
            let alertBox = document.getElementById('alert-box-email');
            if (alertBox) {
                alertBox.style.display = 'none';
            }
        }}
});

