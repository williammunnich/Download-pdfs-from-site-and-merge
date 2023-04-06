from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
from return_list_of_local_imgs import return_imgs_in_directory
def merge_imgs_to_pdf(chapter_name):
    list_of_local_imgs = return_imgs_in_directory()
    images = [
        Image.open("" + f)
        for f in list_of_local_imgs
    ]

    pdf_path = chapter_name + ".pdf"
        
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )