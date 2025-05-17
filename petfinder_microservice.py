import requests
CLIENT_ID = "60XhvkrXIhsaNBOQSkaTiPMw2lYOVngKLcnpOcRj4E3OkX2N3m"
CLIENT_SECRET = "aX9Yb1AOTTwZhwibuJgY5A91RgTTaWIw0UXSpzxo"

def get_token():
    url = "https://api.petfinder.com/v2/oauth2/token"
    data = {"grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET}
    response = requests.post(url, data)
    response.raise_for_status()
    return response.json()["access_token"]
def get_organizations(zip_code, access_token):
    url = "https://api.petfinder.com/v2/organizations"
    response = requests.get(url, params={"location": zip_code, "distance": 50, "limit": 10}, headers={"Authorization": f"Bearer {access_token}"})
    return response.json()["organizations"]

def main():
    zip_code = input("Please provide a zip code: ")
    token = get_token()
    orgs = get_organizations(zip_code, token)
    for item in orgs:
        name = item["name"]
        address = item["address"]
        email = item["email"]
        phone = item["phone"]


        print(f"{name}, ({address["city"]}, {address["state"]}), Email: {email}, Phone: {phone}")


if __name__ == "__main__":
    main()
