# manganelo--downloader
A simple manga downloader using the following modules:
- Selenium
- BeautifulSoup4
- Pillow, the Python Imaging Library (PIL)

This project was mainly created only for personal use as my SO wanted to read manga on her Kindle. The only site this supports is Manganelo.

## Instructions:
1. run `pip install -r requirements.txt` after cloning this repo.
2. Go to https://m.manganelo.com/wwww, search for your favorite manga
3. Run `manga-downloader.py`.
4. Paste the url of the *CHAPTER* when prompted after running the script (or modify in the `BASE_URL` variable). This will scrape that chapter and the suceeding chapters automatically using selenium.
5. Works by scraping all the images for you and convert to a PDF document, just minimize the browser window and continue working on your thing.
    - to implement headless scraping in the future

Images are of reduced quality for compression purposes.
