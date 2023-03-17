import argparse
import glob
import json
import os
from PIL import ExifTags, Image

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
        return img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
    if orientation == 6:
        return img.transpose(Image.ROTATE_270)
    if orientation == 7:
        return img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    if orientation == 8:
        return img.transpose(Image.ROTATE_90)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("org_dir")
    parser.add_argument("dst_dir")
    parser.add_argument("-f", "--fromindex", type=int, default=0)
    args = parser.parse_args()

    if not os.path.exists(args.dst_dir):
        os.mkdir(args.dst_dir)

    matches = os.path.join(args.org_dir, "*")
    sorted_files = sorted(glob.glob(matches))

    for i, path in enumerate(sorted_files):
        if i < args.fromindex:
            continue

        filename = os.path.splitext(os.path.basename(path))
        webp_path = os.path.join(args.dst_dir, filename[0] + ".webp")
        json_path = os.path.join(args.dst_dir, filename[0] + ".json")

        if os.path.exists(webp_path):
            print(f"{i}\talready exists: {webp_path}")
            continue

        img = Image.open(path)
        exif, orientation = get_exif(img)
        with open(json_path, "w") as fp:
            json.dump(exif, fp, indent=2, ensure_ascii=False)

        rotated_img = rotate_image(img, orientation)
        rotated_img.save(webp_path)
        print(f"{i}\tsaved: {webp_path}")
