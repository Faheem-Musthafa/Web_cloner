import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Ensure required modules are installed
def ensure_dependencies():
    try:
        import requests
        import bs4
    except ModuleNotFoundError:
        print("Required modules not found. Ensure requests and beautifulsoup4 are installed.")
        sys.exit(1)

# Function to download a file
def download_file(url, folder):
    local_filename = os.path.join(folder, os.path.basename(urlparse(url).path))
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded: {url}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Function to clone a website
def clone_website(base_url, output_folder="cloned_site"):
    os.makedirs(output_folder, exist_ok=True)
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to access website: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup.find_all(['link', 'script', 'img']):
        src = tag.get('href') or tag.get('src')
        if src and not src.startswith(('http', 'https')):
            full_url = urljoin(base_url, src)
            download_file(full_url, output_folder)
            local_path = os.path.basename(urlparse(full_url).path)
            if tag.name == 'link':
                tag['href'] = local_path
            elif tag.name == 'script':
                tag['src'] = local_path
            elif tag.name == 'img':
                tag['src'] = local_path
    
    with open(os.path.join(output_folder, "index.html"), "w", encoding='utf-8') as file:
        file.write(str(soup))
    print("Website cloning complete!")

# Example Usage
if __name__ == "__main__":
    ensure_dependencies()
    url = input("Enter the website URL to clone: ")
    clone_website(url)
