import os
from PIL import Image

class FS:
    def __init__(self, path):
        self.path = path
    
    def create_dir(self, dir_name):
        os.mkdir(os.path.join(self.path, dir_name))
        
    def list_dir(self):
        return os.listdir(self.path)
    
    def read_file(self, file_name):
        with open(os.path.join(self.path, file_name), "rb") as f:
            byte_data = f.read()
        return byte_data
    
    def write_file(self, file_name, byte_data):
        with open(os.path.join(self.path, file_name), "wb") as f:
            f.write(byte_data)
            
    def show_image(self, file_name):
        image = Image.open(os.path.join(self.path, file_name))
        image.show()
        
# Example  usage
fs = FS("C:/Users/stefa/Desktop/Scripts")
fs.create_dir("R")
print(fs.list_dir())
byte_data = fs.read_file("I.jpg")
fs.write_file("F.jpg", byte_data)
fs.show_image("I.jpg")
byte_data2 = fs.read_file("F.jpg")
fs.show_image("F.jpg")
