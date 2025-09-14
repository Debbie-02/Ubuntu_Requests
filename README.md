# Ubuntu_Requests
Python Libraries Assignment

## Overview
Ubuntu_Requests is a simple Python tool that allows users to download images from the web by providing a URL. Images are saved in a dedicated directory for easy sharing and organization.

## Features
- Prompts the user for an image URL
- Downloads the image using the `requests` library
- Saves images in a `Fetched_Images` directory
- Handles errors gracefully (invalid URLs, network issues)
- Extracts the filename from the URL or generates one if missing

## Ubuntu Principles
- **Community:** Connects to the wider web by fetching images from any URL
- **Respect:** Handles errors without crashing, providing clear feedback
- **Sharing:** Organizes downloaded images for later sharing
- **Practicality:** Offers a useful tool for saving images locally

## Requirements
- Python 3.x
- `requests` library

## Installation
Install the required library:
```
pip install requests
```

## Usage
1. Run the script:
    ```
    python Ubuntu_Requests.py
    ```
2. Enter a valid image URL when prompted.
3. The image will be saved in the `Fetched_Images` directory.
