from download import download_chapter
from to_pdf import convert_chapter

'''
    Manganelo semi-auto downloader 1.0

1. Go to readmanganato.com, search for your favorite manga
2. Paste the url in the paste_url variable. Do not change anything!
3. Change how many chapters you like. This will download everything from chapter 1

'''

paste_url = 'https://readmanganato.com/manga-em981495/chapter-25'
chapters = 1

download_chapter(paste_url, chapters, just_this_chapter=True)
convert_chapter()
