import xml.etree.ElementTree as et
from subprocess import call
import os
import re
import shutil

makeSVGs = True
moveSVGs = True
extractd = True

if makeSVGs:
    os.chdir('./fonts')
    fonts = os.listdir('./')
    for font in fonts:
        escapedSpacesFont = font.replace(' ', '\ ')
        os.system("fontforge -lang=ff -c 'Open($1); SelectWorthOutputting(); Select(65); Export(\"svg\"); endloop;' " + escapedSpacesFont)
    os.chdir('../')

if moveSVGs:
    pathForSVGs = './svg'
    files = os.listdir('./fonts')
    for f in files:
        if f.startswith('$'):
            shutil.move(os.path.join('./fonts',f), pathForSVGs)

if extractd:
    files = os.listdir('./svg')
    for f in files:
        try:
            content = et.parse(os.path.join('./svg',f)).getroot()
            d = []
            for ele in content.findall('.//{http://www.w3.org/2000/svg}path'):
                d = ele.attrib['d']
            print f, "-->", d
        except:
            print("Cannot parse: ", f)
        print ""