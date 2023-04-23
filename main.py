import requests
import base64


res = requests.get("http://127.0.0.1:8000/cam")
print(res.json())


with open("test_images/individual.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    # print((my_string).decode('ascii'))
    
payload = {
    "location": "Hall B",
    "image": my_string.decode('ascii')
}

res = requests.post("http://127.0.0.1:8000/cam", json=payload)
print(res.json())