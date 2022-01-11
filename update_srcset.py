import glob
from PIL import Image
import re

def get_srcset(path):
    images = glob.glob("./" + path.replace("original","*").replace(".jpg",".*").replace(".jpeg",".*"))
    results =[]
    for img in images:
        width = Image.open(img).width
        print("found:" + img + " with width: " + str(width))
        results.append((width, img))
    results.sort()
    srcset = "srcset=\"" + ", ".join([img + " " + str(px) + "w" for px, img in results])
    srcset = srcset + "\""
    return srcset


if __name__ == "__main__":

    a_file = open("index.html", "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    result_lines = []
    for line in list_of_lines:
        if "<img" in line and "src=" in line:
            line = re.sub("srcset=\".*?\"", "",line)
            path = line.split("src=\"")[1].split("\"")[0]
            line = line.replace("src=", get_srcset(path) + " src=" )
            result_lines.append(line)
        else:
            result_lines.append(line)
    
    output_file = open("index.html","w")
    output_file.writelines(result_lines)
    output_file.close()