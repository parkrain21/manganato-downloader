from fpdf import FPDF
import os

def convert_chapter():

# initialize the pdf class 
    pdf = FPDF()
    root_pics = '.\\Pics\\'

# get the directory of the raw images for pdf conversion
# dapat pero chapter folder lang ang pag walk (fix this pls)
    images = []
    counter = 1
    for root, dirs, files in os.walk('.\\Pics\\'):
        # skip the first iteration!!!!!!
        if root == root_pics:
            continue
        else:
            for file in files:
                images.append(os.path.join(root,file))
# code block that handles conversion, loops through every image on
# the folder, returns a collated pdf then deletes all raw images.
        for page in images:
            pdf.add_page()
            pdf.image(page)
        pdf.output(f"Chapter {counter}.pdf", "F")
        images = []
        counter += 1

if __name__ == '__main__':
    print('running conversion script')