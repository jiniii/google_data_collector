import httplib2
import json

class GoogleData:
    def __init__(self):
        self.base_url = 'https://www.googleapis.com/plus/v1/people/me'

    def get_data(self, access_token):
        url = self.base_url + "?access_token=" + access_token
        j = httplib2.Http().request(url)[1]
        return json.loads(j.decode("utf-8"))

