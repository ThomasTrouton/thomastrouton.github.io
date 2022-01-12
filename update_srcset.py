import glob
from PIL import Image
import re
from bs4 import BeautifulSoup

def get_srcset(path):
    images = glob.glob("./" + path.replace("original","*").replace(".jpg",".webp*").replace(".jpeg",".webp"))
    results =[]
    for img in images:
        width = Image.open(img).width
        results.append((width, img))
    results.sort()
    return ", ".join([img + " " + str(px) + "w" for px, img in results])


if __name__ == "__main__":

    a_file = open("index.html", "r")
    soup = BeautifulSoup(a_file.read(), 'html.parser')
    a_file.close()
    for img in soup.find_all('img'):
        srcset = get_srcset(img.get('src'))
        img["srcset"] = srcset
    output_file = open("index.html","w")
    output_file.write(soup.prettify(formatter="html5"))
    output_file.close()