import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import cv2
import numpy as np
from os.path import exists


for j in range(0,46):
    pagenum = j + 1
    print(pagenum)
    url = "https://www.digikala.com/treasure-hunt/products/?pageno=" + str(pagenum) + "&sortby=4"
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    jobs = soup.find_all('a', class_ = 'c-product-box__img' )
    jobs_str = str(jobs)
    pattern1 = re.compile(r'href=\"(\S*)\"')
    x = pattern1.findall(jobs_str)

    for i in x:    
        url2 = "https://www.digikala.com" + i
        
        page2 = requests.get(url2).text
        soup2 = BeautifulSoup(page2,'lxml')
        
        jobs2 = soup2.find_all('li', class_ = 'js-product-thumb-img' )
        jobs_str2 = str(jobs2)
        pattern2 = re.compile(r'data-src=\"(\S*\.jpg)')
        x2 = pattern2.findall(jobs_str2)
        


        for k in x2:
            newstr1 = k.replace("/", "")
            newstr = newstr1.replace(":", "")
                
            urllib.request.urlretrieve(k, 'C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+newstr)
            try:
                original = cv2.imread('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+newstr)
                duplicate = cv2.imread('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\'+newstr)
                difference = cv2.subtract(original, duplicate)
                b, g, r = cv2.split(difference)
                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    print("The images are completely Equal")
                else :
                    print("Found It")
                    print(newstr)
                    print(url2)
                    f = open("key.txt", "a")
                    f.write(newstr)
                    f.close()
                    # Imports PIL module 
                    from PIL import Image
  
                    # open method used to open different extension image file
                    im = Image.open('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+newstr) 
  
                    # This method will show image in any image viewer 
                    im.show() 
            except:
                # Imports PIL module 
                from PIL import Image
  
                # open method used to open different extension image file
                im = Image.open('C:\\Users\\Administrator.S-VM1\\Desktop\\python\\Hunt\\images\\'+newstr) 
  
                # This method will show image in any image viewer 
                im.show() 
                f = open("err.txt", "a")
                f.write(newstr)
                f.close()
