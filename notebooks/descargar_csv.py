import requests

urls = {
    "cases": "https://api.vitaldb.net/cases",
    "labs":  "https://api.vitaldb.net/labs",
    "trks":  "https://api.vitaldb.net/trks"
}

for name, url in urls.items():
    r = requests.get(url)
    with open(f"data/raw/{name}.csv", "wb") as f:
        f.write(r.content)
    print(f"Descargado {name}.csv")