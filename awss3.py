import botocore.session
session = botocore.session.get_session()
s3 = session.create_client('s3', region_name='us-east-1')

class awss3:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = s3
    # méthodes list, create, read,  delete 
    def list(self):
        return self.s3.list_objects(Bucket=self.bucket_name)['Contents']
    def create(self, key, data):
        self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=data)
    def read(self, key):
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        return obj['Body'].read()
    def delete(self, key):
        self.s3.delete_object(Bucket=self.bucket_name, Key=key)
        

