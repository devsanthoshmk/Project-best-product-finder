import time
st=time.time()
from lxml import etree
import requests

url = f"https://www.flipkart.com/search?q=keyboard%20skin&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
r = requests.get(url, headers=headers)
'''commit'''
file=open('flipkart scrapping/del.html')
html_content=file.read()
tree=etree.HTML(html_content)

products=tree.xpath('//div[@class="_4ddWXP"]')[:20]
full_list=[]#name#rat#price#reviews

for product in products:
    name_atag=product.xpath('.//a[@class="s1Q9rs"]')[0]
    try:
        rat=product.xpath('.//div[@class="_3LWZlK"]')[0].text
    except IndexError:
        rat="no ratings"
    
    full_list.append([name_atag.get('title'),rat,product.xpath('.//div[@class="_30jeq3"]')[0].text,"https://www.flipkart.com"+name_atag.get('href')])

print((time.time()-st)/60)