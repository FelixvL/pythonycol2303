import requests
from io import BytesIO
from PIL import Image
 
def shady():
    response = requests.get('https://source.unsplash.com/1600x900/?cats')
    img = Image.open(BytesIO(response.content))
    img.show()
