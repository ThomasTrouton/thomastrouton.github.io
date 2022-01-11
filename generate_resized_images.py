import pathlib
import glob
from PIL import Image 


def rename_image(path):
    image_sizes = {"xxs":300, "xs":500, "s":800, "m":1200, "l":1600, "xl":2000}

    for (size,pixels) in image_sizes.items():
        new_path = path.replace("original",size)
        pathlib.Path(new_path).parent.mkdir(parents=True, exist_ok=True)
        image = Image.open(path)
        if (max(image.width, image.height) > pixels):
            image.thumbnail((pixels, pixels))
            image.save(".".join(new_path.split(".")[:-1])+".webp", optimize=True, quality=95, format="WEBP")
            print("create image at" + new_path + " with pixels " + str(pixels))

if __name__ == "__main__":
    image_list = glob.glob("/home/thomas/projects/thomastrouton.github.io/**/*.jp*",recursive=True)
    for image in image_list:
        rename_image(image)

