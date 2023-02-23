# import requests
# import json

# url = 'https://dummyjson.com/products' #bu url ye farkli seyler ekleyerek baska veriler cagirabiliriz

# response = requests.get(url, params = {'limit':15, 'skip':20})  #

# print(response.status_code)
# products = json.loads(response.text)
# products = products['products']

# for product in products:
#     print(product['title'])

# # bu yukardaki kodlar ile veri cagirdik+
# internetten gelen json verisini python objesine ceviriyoruz, str hatasini asmak icin json.load() yapiyoruz


import requests
import json
# print(products['products'])
# user = "{'username': 'ömer', 'age': 27, 'email': 'omer@gmail.com'}"
# print(user['username'])
url = "https://dummyjson.com/products"
# response = requests.get(url, params={'limit': 15, 'skip': 20})
# print(response.status_code)
# products = response.text
# print(type(products))
# products = json.loads(response.text)
# print(type(products))


# products = products['products']
# for product in products:
#     print(f"ürünün basligi: {product['title']}nürünün fiyati: {product['price']} ürünün idsi: {product['id']}")



# -----------------2yol:

response = requests.get(url, params = {'limit':15, 'skip':20})

products = response.json()
print(products['products'])  #bu sekilde de verileri alabiliriz, daha kisa yol ile



print('-------------') 