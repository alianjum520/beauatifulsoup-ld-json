import requests
import json
from bs4 import BeautifulSoup
import csv  


url ="https://instamall.pk"
htmlContent= requests.get(url).text

soup= BeautifulSoup(htmlContent,'lxml')

data_js = soup.find('script', {'type': 'application/ld+json'}).text.strip()
json_object=json.loads(data_js,strict=False)
f = csv.writer(open("test.csv", "w", newline=''))

name = json_object['name']
ProductId = json_object['productID']
url = json_object['url']
Description = json_object['description']
Image = json_object['image']
General_Sku = json_object['sku']
BrandName = json_object['brand']['name']
print('name:',name)
print('ProductId:',ProductId)
print('url:',url)
print('Description:',Description)
print('Image:',Image)
print('General sku:',General_Sku)
print('brandName:',BrandName)
f.writerow(["sku-size","Price","Availability","Url/size","Name","ProductID","URl","Description","Image","General SKU","Brand Name"])
for offer in json_object['offers']:
    sku_size = offer['sku']
    Price = offer['price']
    Availability = offer['availability']
    url_pro_size = offer['url']

    print('sku-size:',sku_size)
    print('Price:',Price)
    print('Availability:',Availability)
    print('Url/size:',url_pro_size)
    f.writerow([
        sku_size,
        Price,
        Availability,
        url_pro_size,
        name,
        ProductId,
        url,
        Description,
        Image,
        General_Sku,
        BrandName,
    ])



#print('price:',json_object['offers'][0]['price'])
#print('Availability:',json_object['offers'][0]['availability'])
#print('productUrl:',json_object['offers'][0]['url'])
#for items in json_object['offers']:
#    print('Sizes',items['itemOffered']['name'])
#    print('{}: {}'.format(items['itemOffered']['name'],items['itemOffered']['sku']))
