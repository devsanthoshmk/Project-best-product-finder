import time
st=time.time()
from lxml import etree
import requests
q="laptop"
url = f"https://www.flipkart.com/search?q={'&'.join(q.split())}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
             
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
r = requests.get(url, headers=headers)

tree=etree.HTML(r.text)
products=tree.xpath('//div[@class="_2kHMtA"]')
if len(products)>20:
    products=tree.xpath('//div[@class="_2kHMtA"]')[:20]
print(products)
full_list=[]#name#rat#price#reviews

for product in products:
    try:
        rat=product.xpath('.//div[@class="_3LWZlK"]')[0].text
    except IndexError:
        rat="no ratings"
    
    full_list.append([product.xpath('.//div[@class="_4rR01T"]')[0].text,rat,product.xpath('.//div[@class="_30jeq3 _1_WHN1"]')[0].text,"https://www.flipkart.com"+product.xpath('a[@class="_1fQZEK"]')[0].get('href')])

print(full_list[0])
print((time.time()-st)/60)