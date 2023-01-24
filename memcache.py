import pymemcache
from PIL import Image

# Connect to  memcached
client = pymemcache.client.base.Client(('localhost', 11211))

# Read data from file I
with open('I.txt', 'rb') as file:
    data = file.read()
    T = bytearray(data)

# Display image
img = Image.frombytes('RGB', (640, 480), T)
img.show()

# Store data in memcached with key 'K'
client.set('K', T)

# Read data from memcached with key 'K'
T2 = client.get('K')

# Display image
img2 = Image.frombytes('RGB', (640, 480), T2)
img2.show()
