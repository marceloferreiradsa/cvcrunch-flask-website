Dropzone.autoDiscover = false;

document.addEventListener('DOMContentLoaded', function () {
    // Initialize Dropzone
    
    var csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content'); // Get the CSRF token from the meta tag

    var myDropzone = new Dropzone("#profile-photo-upload", { // Make sure this ID matches your form ID
        url: "/profile/picture",
        acceptedFiles: ".png,.jpg,.webp", // Specify accepted file types
        maxFilesize: 2, // Maximum file size in MB
        dictDefaultMessage: "Drag and drop or click here to upload your image", // Custom message
        maxFiles: 1,
        // Other Dropzone options...
        sending: function(file, xhr, formData) {
            formData.append("csrf_token", csrfToken); // Append the CSRF token to formData
        }
    });

    // Add event listener for invalid file type
    myDropzone.on("error", function(file, errorMessage) {
        if (errorMessage === "You can't upload files of this type.") {
            alert("Please upload only webp, png, and jpg files.");
            this.removeFile(file); // Remove the invalid file from Dropzone
        }
    });
    myDropzone.on("success", function(file) {   
        
        this.removeFile(file);
        location.reload();
    })
});