import requests

class BaseRequest:
    def __init__(self):
        self.session = requests.Session()
        self.base_url="https://jsonplaceholder.typicode.com"

    def send_request(self, method, url, **kwargs):
        url = self.base_url + url
        response = self.session.request(method, url, **kwargs)
        print(f"{method} {url}->{response.status_code}")
        return response

    def get(self, url, **kwargs):
        return self.send_request("GET", url, **kwargs)
    def post(self, url, **kwargs):
        return self.send_request("POST", url, **kwargs)
    def put(self, url, **kwargs):
        return self.send_request("PUT", url, **kwargs)
    def delete(self, url, **kwargs):
        return self.send_request("DELETE", url, **kwargs)