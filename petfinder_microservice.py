import requests
import socket
import json


HOST = '127.0.0.1'
PORT = 5555
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(4096).decode('utf-8')
            if not data:
                return
            json_data = json.loads(data)
            zip_code = json_data.get("zipcode", "")
            token = get_token()
            orgs = get_organizations(zip_code, token)
            response = {}
            for item in orgs:
                org = {}
                name = item["name"]
                address = item["address"]
                email = item["email"]
                phone = item["phone"]
                org["name"] = name
                org["email"] = email
                org["phone"] = phone
                org["address"] = (address["city"], address["state"])
                response[name] = org
            conn.sendall(json.dumps(response).encode('utf-8'))

if __name__ == "__main__":
    main()
