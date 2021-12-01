import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import cv2
import numpy as np
from os.path import exists


for j in range(0,46):                                                                                # Loop through pages 1 to 47
    pagenum = j + 1
    url = "https://www.digikala.com/treasure-hunt/products/?pageno=" + str(pagenum) + "&sortby=4"    # Link to Competition page products
    page = requests.get(url).text                                                                    # Extract html source code
    soup = BeautifulSoup(page,'lxml')
    products = soup.find_all('a', class_ = 'c-product-box__img' )                                    # Get All products urls from their class 
    products_str = str(products)                                                                      
    pattern1 = re.compile(r'href=\"(\S*)\"')                                                         # Extract products url with regex
    x = pattern1.findall(products_str)

    for i in x:                                                                                      # Loop Products 
        url2 = "https://www.digikala.com" + i
        page2 = requests.get(url2).text                                                              # Extract html source code of product page
        soup2 = BeautifulSoup(page2,'lxml')
        images = soup2.find_all('li', class_ = 'js-product-thumb-img' )                              # Get All Images urls from their class               
        images_str = str(images)                
        pattern2 = re.compile(r'data-src=\"(\S*\.jpg)')                                              # Extract images url with regex
        x2 = pattern2.findall(images_str)
        


        for k in x2:                                                                                 # Iterate through images and correct their name in order to save them
            imageurl = k.replace("/", "")
            imagefile = imageurl.replace(":", "")   
            urllib.request.urlretrieve(k, 'C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+imagefile)   # Downlaod Image
            try:
                original = cv2.imread('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+imagefile)
                duplicate = cv2.imread('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\'+imagefile)
                difference = cv2.subtract(original, duplicate)
                b, g, r = cv2.split(difference)
                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:                   # Check to see if images are the same 
                    print("The images are completely Equal")
                else :
                    print("Found It")
                    print(imagefile)
                    print(imageurl)
                    f = open("key.txt", "a")
                    f.write(imagefile)
                    f.close()
                    # Imports PIL module 
                    from PIL import Image
  
                    # open method used to open different extension image file
                    im = Image.open('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+imagefile) 
  
                    # This method will show image in any image viewer 
                    im.show() 
            except:
                # Imports PIL module 
                from PIL import Image
  
                # open method used to open different extension image file
                im = Image.open('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+imagefile) 
  
                # This method will show image in any image viewer 
                im.show() 
                f = open("err.txt", "a")
                f.write(imagefile)
                f.close()
