import requests
import os

server_port = os.getenv("SERVER", "server:8000")

url = "http://" + server_port + "/api/post"

class Post:

    @classmethod    
    def get_all(self):
        return requests.get(url)

    @classmethod
    def get(self, id):
        return requests.get(url +'/' + str(id))

    @classmethod
    def create(self, **post):
        return requests.post(url, json=post)

    @classmethod
    def put(self, id: int, **post):
        return requests.put(url + '/' + str(id), json=post)

    @classmethod
    def delete(self, id: int):
        return requests.delete(url +'/' + str(id))
