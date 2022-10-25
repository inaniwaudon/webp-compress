import glob
import json
import os
import sys
from PIL import ExifTags, Image

base_dir = "D:/compressed-photo/"

def get_exif(img):
    exif_dict = {}
    exif = img._getexif()
    for key, value in exif.items():
        if key in ExifTags.TAGS:
            if type(value) is str or type(value) is int or type(value) is float or type(value) is tuple:
                exif_dict[ExifTags.TAGS[key]] = value
    return exif_dict, exif.get(0x112, 1)

def rotate_image(img, orientation):
    if orientation == 1:
        return img
    if orientation == 2:
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    if orientation == 3:
        return img.transpose(Image.ROTATE_180)
    if orientation == 4:
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    if orientation == 5:
        return img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_90)
    if orientation == 6:
        return img.transpose(Image.ROTATE_270)
    if orientation == 7:
        return img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_270)
    if orientation == 8:
        return img.transpose(Image.ROTATE_90)

org_dir = sys.argv[1]
dst_dir = base_dir + org_dir.split("/")[-1]
from_index = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
print("to:" + dst_dir)

os.mkdir(dst_dir)
matches = os.path.join(org_dir, "*")

for i, path in enumerate(glob.glob(matches)):
    if i < from_index:
        continue

    filename = os.path.splitext(os.path.basename(path))
    webp_path = os.path.join(dst_dir, filename[0] + ".webp")
    temp_png_path = os.path.join(dst_dir, filename[0] + ".png")
    json_path = os.path.join(dst_dir, filename[0] + ".json")

    img = Image.open(path)
    exif, orientation = get_exif(img)
    with open(json_path, "w") as fp:
        json.dump(exif, fp, indent=2, ensure_ascii=False)

    rotated_img = rotate_image(img, orientation)
    rotated_img.save(webp_path)
    print(f"saved: {webp_path}")
