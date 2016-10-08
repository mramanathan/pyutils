#! _*_ coding: utf-8 _*_

#!/usr/bin/python3

url = 'http://www.nationalgeographic.com/photography/photo-of-the-day/'

import requests
from bs4 import BeautifulSoup as bs

def get_image_url(page):
    """ from the html payload return the image url """
    soup = bs(page, "html.parser")
    for meta in soup.findAll('meta'):
        metaname = meta.get('name', '').lower()
        metadesc = meta.get('description', '').lower()
        imgloc   = meta.get('content')
        if "description" in metaname:
            imgdesc = meta.get('content')
            print("Topic of today's photo: ")
            print(imgdesc)
        if "image:src" in metaname:
            return(imgloc)



def fetch_day_photo(url):
    """ Given the url, fetch the html body containing the photo url """
    response = requests.get(url)
    return response.content



if __name__ == "__main__":
    page = fetch_day_photo(url)
    photo_url = get_image_url(page)
    print("Image URL is : ", photo_url)
    imgloc = fetch_day_photo(photo_url)
    with open("photo.jpg", "wb") as f:
        f.write(imgloc)
