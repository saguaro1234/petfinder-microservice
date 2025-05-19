This is a microservice for Jennifer Putsche's Pet program. 
The program receives a zip code in JSON format and returns the data for 10 pet adoption facilities within 50 miles of that zip code.
# 🐾 Petfinder Microservice

**For:** Jennifer Putsche's Pet Program  
**Purpose:**  
This microservice receives a U.S. ZIP code in JSON format and returns data for up to **10 pet adoption facilities** located within a **50-mile radius** of the provided ZIP code.

---

## 📦 Required Python Libraries

- `json`
- `socket`

---

## 🌐 Microservice Connection Configuration

```python
HOST = '127.0.0.1'
PORT = 5555


Required Python Libraries:
JSON, socket
These can be imported by including the statements:
import socket
import json
at the top of the file.

Intitalize ports:
HOST = '127.0.0.1'
PORT = 5555

Start connection:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  
How to request data:
You must connect HOST and PORT using python sockets. and then send a zip code from the main program using json.dumps()
zipcode bust be sent as JSON
ex. json_string = {"zipcode": (enter zip code here)}
and can be sent with this clause
s.sendall(json_string.encode('utf-8'))

How to receive data:
your code can receive data by using the clause
response_data = s.recv(4096).decode('utf-8')
response_json = json.loads(response_data)

if the microservice receives an invalid zipcode it will return the value False.
