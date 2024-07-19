// Function to prevent scrolling
function preventScroll(e) {
    e.preventDefault();
    e.stopPropagation();
    return false;
}

// Function to disable scrolling
function disableScroll() {
    window.addEventListener('wheel', preventScroll, { passive: false });
    window.addEventListener('touchmove', preventScroll, { passive: false });
    window.addEventListener('keydown', preventScrollKeys, { passive: false });
}

// Function to enable scrolling
function enableScroll() {
    window.removeEventListener('wheel', preventScroll, { passive: false });
    window.removeEventListener('touchmove', preventScroll, { passive: false });
    window.removeEventListener('keydown', preventScrollKeys, { passive: false });
}

// Function to prevent scrolling with keys
function preventScrollKeys(e) {
    const keys = { ArrowLeft: 1, ArrowUp: 1, ArrowRight: 1, ArrowDown: 1, Space: 1, PageDown: 1, PageUp: 1 };
    if (keys[e.key]) {
        preventScroll(e);
    }
}

// Disable scrolling on pages with the 'no-scroll' class
document.addEventListener('DOMContentLoaded', function() {
    if (document.body.classList.contains('no-scroll')) {
        disableScroll();
    } else {
        enableScroll();
    }
});

// Existing code for Dropzone and other functionalities...

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
        init: function() {
            this.on("sending", function(file, xhr, formData) {
                formData.append("csrf_token", csrfToken); // Append the CSRF token to formData
            });
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
}

document.addEventListener('DOMContentLoaded', function() {
    var step1Btn = document.getElementById('step1-btn');
    if (step1Btn) {
        step1Btn.addEventListener('click', function() {
            scrollToSection('step2');
        });
    }
});

/*
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
            body: JSON.stringify({ text: text }),
        });
        let textData = await textResponse.json();
        displayMessage('Text successfully processed');

        // Now call the API
        let apiResponse = await fetch('/apiCall', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: 'API Called!' }),
        });
        let apiData = await apiResponse.json();
        displayMessage('API call successfully processed');

        // Fetch and display results from the final API call
        let finalResponse = await fetch('/report'); // Make sure this should be an await if you are expecting to wait for the result
        let finalData = await finalResponse.json(); // Convert the response to JSON
        console.log(finalData); // For example, log the data
        displayContent(finalData);

    } catch (error) {
        console.error('Error:', error);
        displayMessage('Error processing request');
    }
});
*/

document.getElementById('forw-step3-btn').addEventListener('click', async function() { // Note the async keyword
    var textArea = document.getElementById('textPasteArea');
    var text = textArea.value;
    var csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content'); // Get the CSRF token from the meta tag

    // Show loading message or spinner
    displayMessage('Processing... Please wait.');

    try {
        // First, process the text
        let textResponse = await fetch('/textPaste', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include the CSRF token in the headers
            },
            body: JSON.stringify({ text: text }),
        });
        let textData = await textResponse.json();
        displayMessage('Text successfully processed');

        // Now call the API
        let apiResponse = await fetch('/apiCall', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include the CSRF token in the headers
            },
            body: JSON.stringify({ text: 'API Called!' }),
        });
        let apiData = await apiResponse.json();
        displayMessage('API call successfully processed');

        // Fetch and display results from the final API call
        let finalResponse = await fetch('/report'); // Make sure this should be an await if you are expecting to wait for the result
        let finalData = await finalResponse.json(); // Convert the response to JSON
        console.log(finalData); // For example, log the data
        displayContent(finalData);

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
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('forw-step3-btn').addEventListener('click', function() {
    scrollToSection('step4');
});

document.getElementById('back-step3-btn').addEventListener('click', function() {
    scrollToSection('step2');
});

document.getElementById('back-step4-btn').addEventListener('click', function() {
    scrollToSection('step3');
});

// Function to check if there are any files in the Dropzone area
function hasFilesInDropzone() {
    return myDropzone.getQueuedFiles().length > 0;
}

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
        signupEmail.addEventListener('input', function(){
            console.log('input event triggered');
            let alertBox = document.getElementById('alert-box-email');
            if (alertBox) {
                alertBox.style.display = 'none';
            }
        });
    }
});
