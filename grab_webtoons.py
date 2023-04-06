from all_links_from_url import grab_webtoon_chapter_links
from down_jpg import grab_imgs
from merge_imgs_to_pdf import merge_imgs_to_pdf
from del_imgs_in_directory import delete_imgs_in_directory

webtoon_mainpage = input("Give the URL of the WebToon list of chapters: ")
webtoon_chapter_links = grab_webtoon_chapter_links(webtoon_mainpage)
for chapter_link in webtoon_chapter_links:
    chapter_name = chapter_link.split("/")[-2] + chapter_link.split("/")[-1]
    grab_imgs(chapter_link)
    merge_imgs_to_pdf(chapter_name)
    delete_imgs_in_directory()
    
    