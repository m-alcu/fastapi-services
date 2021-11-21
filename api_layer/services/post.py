import requests

class Post:

    @classmethod    
    def get_all(self):
        return requests.get('http://server:8000/api/post')

    @classmethod
    def get(self, id):
        return requests.get('http://server:8000/api/post/' + str(id))

    @classmethod
    def create(self, **post):
        return requests.post('http://server:8000/api/post', json=post)

    @classmethod
    def put(self, id: int, **post):
        return requests.put('http://server:8000/api/post/' + str(id), json=post)

    @classmethod
    def delete(self, id: int):
        return requests.delete('http://server:8000/api/post/' + str(id))
