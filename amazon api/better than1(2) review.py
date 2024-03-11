import requests

url = "https://amazon-merchant-data.p.rapidapi.com/get-reviews"

querystring = {"asin":"B08L6ZD883","country":"in","page":"1"}

headers = {
	"X-RapidAPI-Key": "912fd7ecd8msh6444ef1b2239c88p1b8993jsn343eee19f83c",
	"X-RapidAPI-Host": "amazon-merchant-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())