class TwoLevelCache:
    def __init__(self, mem_cache_size, file_cache_size, s3_bucket_name):
        self.mem_cache = LRU(mem_cache_size)
        self.file_cache = LRU(file_cache_size)
        self.s3_bucket_name = s3_bucket_name
        self.s3 = boto3.client("s3")
    
    def create(self, key, data):
        # store data in mem cache
        evicted_keys = self.mem_cache.create(key, data)
        # store evicted keys in file  cache
        for evicted_key in evicted_keys:
            self.file_cache.create(evicted_key, self.mem_cache.read(evicted_key))
        # store data in S3
        self.s3.put_object(Bucket=self.s3_bucket_name, Key=key, Body=data)
        
    def read(self, key):
        data = self.mem_cache.read(key)
        if data is None:
            data = self.file_cache.read(key)
            if data is None:
                # read data from S3
                data = self.s3.get_object(Bucket=self.s3_bucket_name, Key=key)["Body"].read()
                # store data in file cache
                self.file_cache.create(key, data)
            # store data in mem cache
            self.mem_cache.create(key, data)
        return data
    
    def delete(self, key):
        self.mem_cache.delete(key)
        self.file_cache.delete(key)
        self.s3.delete_object(Bucket=self.s3_bucket_name, Key=key)
