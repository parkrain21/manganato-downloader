from email.mime import base
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import requests
import time
import os

'''
    Manganelo semi-auto downloader 1.0

1. Go to readmanganato.com, search for your favorite manga
2. Paste the url in the paste_url variable. Do not change anything!
3. Change how many chapters you like. This will download everything from chapter 1
'''

def download_chapter(raw_url, chapters, just_this_chapter=False):     
    driver = webdriver.Edge()

# main loop, loop through one chapter at a time
    base_url = '-'.join(raw_url.split('-')[:2])
    if just_this_chapter == True:
        url = raw_url
    else:
        for chapter in range(1, chapters+1):        
            url = f'{base_url}-{chapter}'        

        # gets the raw HTML file for every chapter
            html_doc = requests.get(url).text
            soup = BeautifulSoup(html_doc, 'lxml')

        # put all image urls in a list
            images = soup.find_all('img')
            manga_pages = []
            for img in images:
                page = img.get('src')
                if page[-3:] == 'jpg':
                    manga_pages.append(page)

        # make a folder for the raw pics    
            title = soup.title.text.split('-')[0]
            folder_name = ''.join(title.split()[:3]) + ', Chapter ' + str(chapter)
            new_folder = os.path.join(os.getcwd(), 'Pics' , folder_name)
            try: 
                os.makedirs(new_folder)
            except OSError as error: 
                pass  

        # this loop is the core program logic
            for i in range(len(manga_pages)):
                img_url = manga_pages[i]

                if i+1 < 100 and i+1 < 10:
                    page_no = f'00{i+1}'
                elif i+1 < 100 and i+1 >= 10:
                    page_no = f'0{i+1}'

                filename = f'{title.split()[-1]}-{page_no}'

                if requests.get(img_url) != 200:
                    driver.get(img_url)
                    # time.sleep(0.1)
                    driver.find_element_by_xpath('//*[@id="reload-btn"]').click()
                    time.sleep(0.05)
                    driver.find_element_by_xpath('/html/body/img').screenshot(f'D:\Personal Docs\IT Projects\Manga Downloader\Pics\{folder_name}\{filename}.png')
                    # print('error!!!!!!')
                else:
                    urllib.request.urlretrieve(img_url, filename)

if __name__ == '__main__':
    print('running download script')

