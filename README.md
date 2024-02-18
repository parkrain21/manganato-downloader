# manganato-downloader
A simple manga downloader using the following modules:
- Selenium
- BeautifulSoup4
- Pillow, the Python Imaging Library (PIL)

This project was mainly created only for personal use as my SO wanted to read manga on her Kindle. The only site this supports is manganato.com.

## Instructions:
1. Go to https://manganato.com/, search for your favorite manga
2. Paste the url of the *CHAPTER* in the `BASE_URL` variable. This will scrape that chapter and the suceeding chapters automatically using selenium.
3. Works by scraping all the images for you and convert to a PDF document, just minimize the browser window and continue working on your thing.
    - to implement headless scraping in the future

Images are of reduced quality for compression purposes.