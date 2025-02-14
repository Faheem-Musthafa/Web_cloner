# Website Cloner

## Overview
This Python script allows you to clone a static website by downloading its HTML, CSS, JavaScript, and image files. The script modifies local references so that the cloned site can be viewed offline.

## Features
- Downloads and saves HTML, CSS, JavaScript, and images locally
- Updates file paths for offline viewing
- Handles common web assets like `<link>`, `<script>`, and `<img>`

## Requirements
Ensure you have Python installed along with the following dependencies:

```sh
pip install requests beautifulsoup4
```

## Usage
Run the script and enter the website URL when prompted:

```sh
python website_cloner.py
```

Alternatively, modify the script to specify a URL directly:

```python
clone_website("https://example.com")
```

## Notes
- This script is intended for educational purposes only. Do not use it to clone websites without permission.
- The script only clones static assets and may not work correctly for dynamic websites that rely on backend processing.

## License
This project is licensed under the MIT License.

