#https://stackoverflow.com/questions/17358722/python-3-how-to-delete-images-in-a-folder#17358788
#deletes all jpg files in current folder
import glob
import os
def delete_imgs_in_directory():
    removing_files = glob.glob('*.jpg')
    for i in removing_files:
        os.remove(i)