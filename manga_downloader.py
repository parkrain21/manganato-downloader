from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
import sys

from compress import compress_image
from pdf_collation import output, get_chapter_num

<<<<<<< HEAD
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else input("Please specify a manga link..\n")
=======
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else input("Please specify a manga link")
>>>>>>> 9d4fa5a5a9b5f3f9a6d87b4b525a9233261cd1f5
# BASE_URL = 'https://readmanganato.com/manga-aa951409/chapter-142'

# Initialize the driver instance
driver = webdriver.Edge()
driver.implicitly_wait(15)

def download_chapters(auto_compress=True):
    CURRENT_URL = BASE_URL
    driver.get(CURRENT_URL)

    # needed to bypass the cloudflare firewall
    headers = {"Referer": f"{CURRENT_URL}"}

    while True:
        time.sleep(5)
        scroll_to_bottom(driver)

        # fetches all the image links and compiles them in a list
        html_doc = requests.get(CURRENT_URL).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        images = soup.findAll('img')
        url_list = [img['src'] for img in images if img['src'].endswith(".jpg")]

<<<<<<< HEAD
        manga_name = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[4]/h1").text.split(' ')
        manga_name = ' '.join(manga_name[0:manga_name.index('CHAPTER')])
=======
        manga_name = ""
>>>>>>> 9d4fa5a5a9b5f3f9a6d87b4b525a9233261cd1f5
        chapter_num = ""

        # downloads the images into jpg files and saves them into a folder
        original_size = 0
        compressed_size = 0

        for img_link in url_list:
            r = requests.get(img_link, headers=headers)

            # Image link format sample: https://v4.mkklcdnv6tempv2.com/img/tab_4/03/01/38/em981495/chapter_1/1-o.jpg

<<<<<<< HEAD
=======
            manga_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/a[2]").text
>>>>>>> 9d4fa5a5a9b5f3f9a6d87b4b525a9233261cd1f5
            page = img_link.split('/')[-1].split('-')[0]            # Get the page number (1-o.jpg) 
            chapter = img_link.split('/')[-2]                       # Get the chapter string for the folder name (chapter_1)
            chapter_num = get_chapter_num(chapter)                  # Get the chapter number from the string (1)

            img_dir = create_dirs(manga_name, chapter, page)

            # Initial image download
            with open( img_dir , "wb+") as f:
                f.write(r.content)
            original_size += os.path.getsize( img_dir )

            # Compress the downloaded image if parameter is True (default)
            if auto_compress:
                compress_image( img_dir )
                compressed_size += os.path.getsize( img_dir )

        if auto_compress:
            print(f"{manga_name} Chapter {chapter_num} -- Downloaded and compressed {len(url_list)} pages. ({round(abs((compressed_size-original_size)/original_size)*100, 2)}% compression | {round(original_size/1048576, 2)}MB -> {round(compressed_size/1048576, 2)}MB)")
        else:
            print(f"{manga_name} Chapter {chapter_num} -- Downloaded {len(url_list)} pages.")
        
        url_list = []

        # PDF Conversion function
        output()

        # GOTO next chapter, if available
        try:
            # click the NEXT CHAPTER button
            next_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[1]/div/a[2]")
<<<<<<< HEAD
            if next_xpath.text == "NEXT CHAPTER":
                next_xpath.click()
                time.sleep(3)
                CURRENT_URL = driver.current_url

            # if the next button does not exist or cannot be found
        except Exception as e:
            print(f"All chapters downloaded for {manga_name}!")
        finally:
=======

            # if the next button does not exist or cannot be found
        except Exception as e:
            next_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[1]/div/a")

        if next_xpath.text == "NEXT CHAPTER":
            next_xpath.click()
            time.sleep(3)
            CURRENT_URL = driver.current_url
        else:
            print(f"All chapters downloaded for {manga_name}!")
>>>>>>> 9d4fa5a5a9b5f3f9a6d87b4b525a9233261cd1f5
            driver.close()
            break

def scroll_to_bottom(driver):
    # Scroll down to the bottom of the page to load all JavaScript
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    finally:
        time.sleep(0.2)

def create_dirs(manga_name, chapter, page=None):
    os.makedirs(os.path.join(os.getcwd(), "Manga_raws", f"{manga_name}", f"{chapter}"), exist_ok=True)
    if page:
        img_dirname =  os.path.join(os.getcwd(), "Manga_raws", f"{manga_name}", f"{chapter}", f"page_{page}.jpg")
    else:
        img_dirname =  os.path.join(os.getcwd(), "Manga_raws", f"{manga_name}", f"{chapter}")

    return img_dirname

if __name__ == "__main__":
    download_chapters()
    
