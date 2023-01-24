import os
import time
import pymemcache
from boto.s3.connection import S3Connection
import boto3

class FS:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.mkdir(directory)

    def list(self):
        return os.listdir(self.directory)

    def create(self, filename, data):
        path = os.path.join(self.directory, filename)
        with open(path, 'wb') as f:
            f.write(data)

    def read(self, filename):
        path = os.path.join(self.directory, filename)
        with open(path, 'rb') as f:
            return f.read()

    def delete(self, filename):
        path = os.path.join(self.directory, filename)
        os.remove(path)

class Mem:
    def __init__(self):
        self.client = pymemcache.client.Client(('localhost', 11211))

    def create(self, key, data):
        self.client.set(key, data)

    def read(self, key):
        return self.client.get(key)

    def delete(self, key):
        self.client.delete(key)

class AWSS3:
    def __init__(self, ak, sk, host):
        self.conn = boto3.connect_s3(ak, sk, host=host)
        
    def list(self, bucket):
        return self.conn.get_bucket(bucket).list()
    
    def write(self, bucket, key, data):
        self.conn.get_bucket(bucket).new_key(key).set_contents_from_string(data)
        
    def read(self, bucket, key):
        return self.conn.get_bucket(bucket).get_key(key).get_contents_as_string()
            

#  Example usage
fs = FS()
fs.create()
print(fs.list())

# Read an image file and store it as bytes
with open("image.jpg", "rb") as f:
    img_data = f.read()

# Write the image data to a file in the R directory
fs.write("image.jpg", img_data)

# Read the data back from the file and display as image
img_data2 = fs.read("image.jpg")
Image.frombytes(img_data2)

# Connect to memcache
mc = Memcache("localhost", 11211)

# Store the image data in memcache
mc.set("image", img_data)

# Read the data back from memcache and display as image
img_data3 = mc.get("image")
Image.frombytes(img_data3)

# Connect to AWS S3
s3 = AWSS3("AK", "SK", "s3.eu-west-3.amazonaws.com")

# List keys in the "ensta" bucket
print(s3.list("ensta"))

# Write the image data to a key in the "ensta" bucket
s3.write("ensta", "image", img_data)

# Read the data back from the key and display as image
img_data4 = s3.read("ensta","key_name")
img4 = Image.open(io.BytesIO(img_data4))
img4.show()