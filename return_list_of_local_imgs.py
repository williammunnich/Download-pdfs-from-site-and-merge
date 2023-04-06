import glob
def return_imgs_in_directory():
    img_files = glob.glob('*.jpg')
    return img_files