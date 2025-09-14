import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    # Create "Fetched_Images" directory if it doesn't exist
    images_dir = "Fetched_Images"
    os.makedirs(images_dir, exist_ok=True)

    try:
        # Try fetching the image from the URL
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  # If URL doesn't have a filename, generate one
            filename = "downloaded_image.jpg"

        # Full path to save image
        file_path = os.path.join(images_dir, filename)

        # Save the image in binary mode
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Image successfully saved as {file_path}")

    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL. Please enter a valid image URL.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_image()
