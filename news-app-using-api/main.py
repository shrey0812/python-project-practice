import requests 

query = input("What are you looking for today\n")
api = "7ff26b1492fa44ebb9261b961d4a2382"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-27&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()

articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n********************************\n")
    