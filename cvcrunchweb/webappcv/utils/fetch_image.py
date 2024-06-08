import os
import glob
from flask import url_for

def get_photo(user_id):
    
    image_path = os.path.join(os.path.dirname(__file__),'..','static', 'images', 'profiles', f"{user_id}.*")
    print(image_path)
    # Use glob to find matching files
    matching_files = glob.glob(image_path)

    # Check if we found any files
    if matching_files:
        # If multiple files, just take the first one
        print("entrei no matching")
        existing_image = matching_files[0]
        print(existing_image)
    else:
        # Default image if no profile image is found
        print('entrei no não matching')
        existing_image = '../static/images/sillouete_1.webp'
        
    return existing_image

def get_photo_url(user_id):
    # Directory where profile images are stored relative to the 'static' folder
    image_directory = 'images/profiles'
    base_path = os.path.join(os.path.dirname(__file__), '..', 'static', image_directory, f"{user_id}")

    # Find files matching the pattern (user_id with any extension)
    matching_files = glob.glob(f"{base_path}.*")
    print("Searching for images at:", base_path + ".*")

    # Check if we found any files
    if matching_files:
        # Get the relative path of the first matching file
        relative_path = os.path.relpath(matching_files[0], os.path.join(os.path.dirname(__file__), '..', 'static'))
        # Normalize path for URL usage
        relative_path = relative_path.replace('\\', '/')  # Replace backslashes with forward slashes
        image_url = url_for('static', filename=relative_path)
        print("Matching file found, URL:", image_url)
        return image_url
    else:
        # Return the URL for the default image
        default_image_url = url_for('static', filename='images/sillouete_1.webp')
        print("No matching files, using default URL:", default_image_url)
        return default_image_url