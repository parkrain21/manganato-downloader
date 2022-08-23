from PIL import Image
from multiprocessing import Pool
import os
import shutil

manga_dir = os.path.join(os.getcwd(), "Manga_raws")
manga_name = ""

def get_chapter_num(chapter):
    chapter_split = chapter.split('_')
    for i, c in enumerate(chapter_split):
        if c.lower() == 'chapter' and chapter_split[i+1].isnumeric():
            return chapter_split[i+1]

# From Stackoverflow, collating pdfs directly using pure PIL
def make_pdf_dirs(manga_name, chapter_num):
    pdf_dirname = os.path.join(os.getcwd(), "Manga PDFs", manga_name)
    if not os.path.exists(pdf_dirname):
        os.makedirs(pdf_dirname, exist_ok=True)

    filename = os.path.join(pdf_dirname, f"{manga_name} - Chapter {chapter_num}.pdf")

    return(os.path.join(pdf_dirname, filename))


def output():

    for root, dirs, files in os.walk(manga_dir):
        if dirs and not files:
            total_chapters = len(dirs)
        # if current iteration is the chapter folder
        if root != manga_dir and dirs == []:
            manga_name = root.split('\\')[-2] 
            chapter = root.split('\\')[-1]
            chapter_num = get_chapter_num(chapter)

            chapter_dir = files
            chapter_dir.sort(key=lambda x: int(x.split('.')[0].split('_')[1]))

            images = [ 
                Image.open(os.path.join(os.path.join(root, page))) 
                for page in chapter_dir 
            ]

            filename = make_pdf_dirs(manga_name, chapter_num)
   
            images[0].save(filename, "PDF" ,resolution=100.0, optimize=True, quality=35, save_all=True, append_images=images[1:])

            shutil.rmtree(root, ignore_errors=True)
    
    print(f"{total_chapters} chapters for {manga_name} converted to PDF.")
