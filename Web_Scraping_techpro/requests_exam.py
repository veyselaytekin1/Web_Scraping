import requests
import json

class Product:
    def __init_(self) -> None:
        self.url = 'https://dummyjson.com/products'


    def get_all_product(self):
        response = request.get(self.url)   
        products = response.json() #kisa kulanim alttaki yerine 

        # products = response.text  #response'u texte cevirdi
        # products = json.loads(products) # texti python objesine cevirdibunlara gerek kalmadan kisa yolu var

        return products

#-------------------
import requests
import json
class Product:
    def __init__(self) -> None:
        self.url = "https://dummyjson.com/products"
    def get_all_product(self):
        respose = requests.get(self.url)  # galiba bu fotolari almak icin kullaniyoruz
        # products = json.loads(respose.text) # ilk kullanım
        products = respose.json() #ikinci kullanım
    def get_single_product(self, product_id):
        response =  requests.get(f"{self.url}/{product_id}") #bu formülü sitenin url'sine bakarak yazdi
        #https://dummyjson.com/products/product_id
        product = response.json() # bununlada galiba json formatina uygn halde getirdi, json,programlama dilleri arasinda ortak bir dil
        return product
        return products
    #https://dummyjson.com/products/search?q=phone
    def search_product(self, name):
        pyload = {'q': name}
        response = requests.get(f"{self.url}/search/", params=pyload) #url'de serach yaparak icinde phone yazan kelimeleri getiriyoruz
        product = response.json()
        return product
      #https://dummyjson.com/products?limit=10&skip=10&select=title,price
    def select_product(self, limit, skip, select):
        pyload = {'limit': limit, 'skip': skip , 'select': select}
        response = requests.get(f"{self.url}", params=pyload)
        return response.json()
product = Product()
# print(product.get_all_product())
# print(product.get_single_product(5))
print(product.search_product('phone'))
print(product.select_product(10, 10, 'title'))        

