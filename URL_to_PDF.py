import os
import requests
from bs4 import BeautifulSoup
import pdfkit

def fetch_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def save_pdf(url, file_path):
    try:
        pdfkit.from_url(url, file_path)
    except Exception as e:
        print(f"Failed to create PDF for {url}: {e}")

def main(url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    links = fetch_links(url)
    for i, link in enumerate(links):
        file_name = f"link_{i+1}.pdf"
        file_path = os.path.join(output_dir, file_name)
        save_pdf(link, file_path)
        print(f"Saved: {file_path}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    output_dir = os.path.expanduser("~/Desktop/PDFs")
    main(url, output_dir)
