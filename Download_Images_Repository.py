import requests
from bs4 import BeautifulSoup
import re
import urllib.request


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
            urllib.request.urlretrieve(k, ''C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\'+imagefile)

