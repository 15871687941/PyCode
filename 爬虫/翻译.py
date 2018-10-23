import requests

start_url = "http://fy.iciba.com/ajax.php?a=fy"
response = requests.post(start_url, data={
    "f": "auto",
    "t": "auto",
    "w": "翻译"
})
start_url.isalpha()
start_url.upper()
start_url.lower()
result = response.json()
print(type(result))
print(result['content']['out'])


