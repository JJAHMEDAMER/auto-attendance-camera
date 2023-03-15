import requests
import base64

with open("1.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

res = requests.get("http://127.0.0.1:8000/cam")


payload = {
    "image": str(my_string)
}

res = requests.post("http://127.0.0.1:8000/cam", json=payload)

print(res.json())