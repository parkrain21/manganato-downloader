from PIL import Image
import os

manga_dir = os.path.join(os.getcwd(), "Manga_raws")

def compress_image(img_source):
    with Image.open(img_source) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        img.save(os.path.join(img_source), "JPEG", optimize=True, quality=40)


def compression_stats():
    original_size = 0
    compressed_size = 0
    for root, dirs, files in os.walk(manga_dir):
        if root != manga_dir and dirs == []:
            for file in files:
                img_dir = os.path.join(root, file)
                original_size += os.path.getsize(img_dir)

    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Compressed")):
        if root != manga_dir and dirs == []:
            for file in files:
                img_dir = os.path.join(root, file)
                compressed_size += os.path.getsize(img_dir)

    print(f"Original Size: {round(original_size/1048576, 2)}MB")
    print(f"After Compression: {round(compressed_size/1048576, 2)}MB")
    print(f"Data saved: {round(abs((compressed_size-original_size)/original_size)*100, 2)}%")


def compress_downloaded_images(manga_name, chapter, img_source):
    img_destination = os.path.join(os.getcwd(), "Compressed", manga_name, chapter)
    img_name = '_comp.'.join(os.path.basename(img_source).split('.'))

    with Image.open(img_source) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")

        if not os.path.exists(img_destination):
            os.makedirs(img_destination)
        
        img.save(os.path.join(img_destination, img_name), "JPEG", optimize=True, quality=40)

def main():
    '''
    (Deprecated) Compresses all pages from the Manga_raws folder and saves in the Compressed folder.  
    '''
    for root, dirs, files in os.walk(manga_dir):
        # if current iteration is the chapter folder
        if root != manga_dir and dirs == []:
            manga_name = root.split('\\')[-2]
            chapter = root.split('\\')[-1]
            for file in files:
                img_dir = os.path.join(root, file)
                compress_downloaded_images(manga_name, chapter, img_dir)




