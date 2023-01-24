import boto3
import os
import pymemcache

class Tiering:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.memcache = pymemcache.client.base.Client(('localhost', 11211))

    def create(self, key, data, cost):
        if cost < 100:
            self.s3.put_object(Bucket='bucket124187', Key=key, Body=data)
        elif 100 <= cost < 1000:
            with open(key, 'wb') as f:
                f.write(data)
        else:
            self.memcache.set(key, data)

    def delete(self, key, cost):
        if cost < 100:
            self.s3.delete_object(Bucket='bucket124187', Key=key)
        elif 100 <= cost < 1000:
            os.remove(key)
        else:
            self.memcache.delete(key)

    def read(self, key, cost):
        if cost < 100:
            obj = self.s3.get_object(Bucket='bucket124187', Key=key)
            return obj['Body'].read()
        elif 100 <= cost < 1000:
            with open(key, 'rb') as f:
                return f.read()
        else:
            return self.memcache.get(key)
            