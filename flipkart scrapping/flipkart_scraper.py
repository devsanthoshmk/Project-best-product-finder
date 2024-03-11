from lxml import etree
# import requests
# url = f"https://www.flipkart.com/search?q=keyboard%20skin&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
# r = requests.get(url, headers=headers)

file=open('flipkart scrapping/del.html')
html_content=file.read()
tree=etree.HTML(html_content)

products=tree.xpath('//div[@class="_4ddWXP"]')
print(len(products))
for i in products:
    