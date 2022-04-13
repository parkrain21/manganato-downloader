from re import A
from fpdf import FPDF
import os

pdf = FPDF()

lroots = []
ldirs = []
lfiles = []
for root, dirs, files in os.walk('.\\Pics\\'):
    for name in files:
        x = os.path.join(root,name)
        print(x)

# print(lroots)