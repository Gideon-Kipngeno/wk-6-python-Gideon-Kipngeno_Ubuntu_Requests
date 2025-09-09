# Ubuntu_Requests

Ubuntu Image Fetcher is a Python-based tool built in the spirit of Ubuntu—"I am because we are." This project connects to the global web community, respectfully fetches shared image resources, and organizes them for future appreciation.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Output](#example-output)
- [Challenge Features](#challenge-features)
- [Contributing](#contributing)
- [Evaluation Criteria](#evaluation-criteria)
- [Ubuntu Philosophy](#ubuntu-philosophy)
- [License](#license)

---

## About

This project is inspired by the Ubuntu philosophy, which emphasizes community, sharing, and respect. The Ubuntu Image Fetcher allows users to fetch images from the internet in a mindful and organized way.

---

## Features

- Prompt the user for one or more image URLs
- Create a directory called `Fetched_Images` if it doesn't exist
- Download images from the provided URLs
- Save images to the `Fetched_Images` directory with appropriate filenames
- Handle errors gracefully (network, HTTP, file issues)
- Prevent duplicate downloads(Please enter image URLs (comma or space separated): https://images.pexels.com/photos/1181703/pexels-photo-1181703.jpeg
✗ Duplicate: pexels-photo-1181703.jpeg already exists and is identical. Skipping download.)
- Check HTTP headers for safe image types

---

## Getting Started

### Prerequisites

- Python 3.7+
- `requests` library

Install the required library:

````bash
pip install requests
````

Clone the Repository
```` bash
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests
````
Usage
Run the script:
```` bash
python ubuntu_image_fetcher.py
````
**Output**
You will be prompted to enter one or more image URLs (separated by commas or spaces).

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (comma or space separated): https://images.pexels.com/photos/2102416/pexels-photo-2102416.jpeg, https://images.pexels.com/photos/2102415/pexels-photo-2102415.jpeg, https://images.pexels.com/photos/2102413/pexels-photo-2102413.jpeg, https://images.pexels.com/photos/1181703/pexels-photo-1181703.jpeg
✓ Successfully fetched: pexels-photo-2102416.jpeg
✓ Image saved to Fetched_Images/pexels-photo-2102416.jpeg

Connection strengthened. Community enriched.

**Challenge Features**
Multiple URLs: Enter several image URLs at once.
Safety Precautions: Only downloads images with safe content types.
Duplicate Prevention: Checks for duplicate images before saving.
HTTP Header Checks: Verifies Content-Type before saving.

**Contributing**
Contributions are welcome! Please fork the repository and submit a pull request.

- Fork the repo
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a pull request

**Evaluation Criteria**
1. Proper use of the requests library for fetching content
2. Effective error handling for network issues
3. Appropriate file management and directory creation
4. Clean, readable code with clear comments
5. Faithfulness to Ubuntu principles of community and respect

**Ubuntu Philosophy**
"A person is a person through other persons."
— Ubuntu philosophy

Your program connects you to the work of others across the web.

**License**
This project is open source and available under the MIT License. ````