

**Petfinder Microservice**
This is a microservice for **Jennifer Putsche's Pet Program**.
The program receives a ZIP code in JSON format and returns data for up to **10 pet adoption facilities** within **50 miles** of the provided ZIP code.

---

**Required Python Libraries:**

* `json`
* `socket`

---

**Port Configuration:**

```
HOST = '127.0.0.1'  
PORT = 5555
```

---

**Starting the Connection (Client Side):**
To connect to the microservice:

```
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.connect((HOST, PORT))
```

---

**How to Request Data:**
You must connect to `HOST` and `PORT` using Python sockets.
Then send a ZIP code using `json.dumps()`.

The ZIP code must be sent as a JSON object. Example:

```
import json

zipcode_data = {"zipcode": "12345"}  
json_string = json.dumps(zipcode_data)  
s.sendall(json_string.encode('utf-8'))
```

---

**How to Receive Data:**
You can receive the microservice’s response like this:

```
response_data = s.recv(4096).decode('utf-8')  
response_json = json.loads(response_data)
```

---

**Invalid ZIP Code Handling:**
If the microservice receives an invalid ZIP code, it will return the value:

```
False
```


