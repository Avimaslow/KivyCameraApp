from filestack import Client
class Fileshare:
    def __init__(self,filepath,api_key="your api key"):
        self.filepath = filepath
        self.api_key = api_key
    def share(self):
        client = Client(self.api_key)
        new_link = client.upload(filepath= self.filepath)
        return new_link.url