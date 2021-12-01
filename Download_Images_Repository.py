import requests
from bs4 import BeautifulSoup
import re
import urllib.request

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
            urllib.request.urlretrieve(k, 'V:\\python\\Hunt\\'+newstr)

