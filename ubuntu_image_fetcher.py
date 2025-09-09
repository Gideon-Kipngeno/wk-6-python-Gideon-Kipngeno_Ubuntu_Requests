import requests
import os
import hashlib
from urllib.parse import urlparse
from mimetypes import guess_extension

# Directory where images will be saved
FETCH_DIR = "Fetched_Images"
# Allowed image MIME types for safety
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp", "image/bmp"}

def get_filename_from_url(url, content_type):
    # Extracts the filename from the URL or generates one based on content type
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        # If no filename or extension, guess extension from content type
        ext = guess_extension(content_type.split(";")[0]) or ".jpg"
        filename = f"downloaded_image{ext}"
    return filename

def is_duplicate(filepath, content):
    # Checks if a file already exists and if its content matches the new content
    if not os.path.exists(filepath):
        return False
    with open(filepath, "rb") as f:
        existing_hash = hashlib.sha256(f.read()).hexdigest()
    new_hash = hashlib.sha256(content).hexdigest()
    return existing_hash == new_hash

def fetch_image(url):
    try:
        # Attempt to fetch the image from the URL
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check if the Content-Type is a supported image type
        content_type = response.headers.get("Content-Type", "")
        if not any(content_type.startswith(t) for t in ALLOWED_IMAGE_TYPES):
            print(f"✗ Skipped: Content-Type '{content_type}' is not a supported image type.")
            return

        filename = get_filename_from_url(url, content_type)
        filepath = os.path.join(FETCH_DIR, filename)
        content = response.content

        # Prevent saving duplicate images
        if os.path.exists(filepath) and is_duplicate(filepath, content):
            print(f"✗ Duplicate: {filename} already exists and is identical. Skipping download.")
            return

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors gracefully
        print(f"✗ Connection error: {e}")
    except Exception as e:
        # Handle other errors gracefully
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    # Ensure the fetch directory exists
    os.makedirs(FETCH_DIR, exist_ok=True)

    # Prompt user for one or more URLs, separated by comma or space
    urls = input("Please enter image URLs (comma or space separated): ").replace(',', ' ').split()
    if not urls:
        print("No URLs provided.")
        return

    # Fetch each image in the list
    for url in urls:
        fetch_image(url.strip())

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()