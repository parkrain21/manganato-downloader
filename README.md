# manganato-downloader
A simple manga downloader using the following modules:
- Selenium
- BeautifulSoup4
- Pillow, the Python Imaging Library (PIL)

This project was initially created only for manganato(.)com, I will try to fully automate this one and add support for more sites.

## Instructions:
1. Go to https://manganato.com/, search for your favorite manga
2. Paste the url in the `BASE_URL` variable. Do not change anything!
3. This will automatically scrape all the images for you and convert to pdf, just minimize the browser window
    - to implement headless scraping in the future

Images are of reduced quality for compression purposes.