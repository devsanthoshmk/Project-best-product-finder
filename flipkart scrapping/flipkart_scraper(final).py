import time
st=time.time()
from lxml import etree
import requests
q : str=int(input("Enter input for search:"))
url = f"https://www.flipkart.com/search?q={'&'.join(q.split())}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
             
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
r = requests.get(url, headers=headers)

tree=etree.HTML(r.text)
try:
    tree.xpath('//div[@class="_4ddWXP"]')[0]
#if (tree.xpath('//div[@class="_4ddWXP"]')!=None) or len(tree.find_all('//div[@class="_4ddWXP"]')!=0):
    print(tree.xpath('//div[@class="_4ddWXP"]'))
    print("if")
    products=tree.xpath('//div[@class="_4ddWXP"]')
    if len(products)>20:
        products=tree.xpath('//div[@class="_4ddWXP"]')[:20]
    print(products)
    full_list=[]#name#rat#price#reviews

    for product in products:
        name_atag=product.xpath('.//a[@class="s1Q9rs"]')[0]
        try:
            rat=product.xpath('.//div[@class="_3LWZlK"]')[0].text
        except IndexError:
            rat="no ratings"
        
        full_list.append([name_atag.get('title'),rat,product.xpath('.//div[@class="_30jeq3"]')[0].text,"https://www.flipkart.com"+name_atag.get('href')])

    print(full_list)
except (TypeError,IndexError):
    print('elif')
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
except:
    full_list=[]
    

print((time.time()-st)/60)