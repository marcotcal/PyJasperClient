import requests
from xml.etree import ElementTree
import base64
import json


class JasperClient:

    def __init__(self, server_url):
        self.url = server_url
        self.info = None
        self.session = requests.session()
        self.connected = False

    def __del__(self):
        pass

    def server_info(self):
        cmd_url = self.url + 'rest_v2/serverInfo'
        request = requests.get(cmd_url)
        self.info = request.content

    @property
    def server_version(self):
        cmd_url = self.url + 'rest_v2/serverInfo/version'
        req = requests.get(cmd_url, cookies=self.login_cookies)
        if req.ok:
            return req.content.decode(req.encoding)
        else:
            return None

    def logout(self):
        cmd_url = self.url + 'logout.html'
        self.session.get(cmd_url)
        self.session.cookies.clear()
        self.connected = False

    def login(self, user, password):
        params = {"j_username": user, "j_password": password}
        cmd_url = self.url + 'rest_v2/login'

        r = self.session.post(url=cmd_url, data=params)
        if r.status_code == 200:
            self.connected = True
        else:
            self.connected = False
        return self.connected

    def resources(self):
        cmd_url = self.url + 'rest_v2/resources/'
        headers = {'content-type': 'application/json'}
        request = requests.get(cmd_url, auth=(self.auth_user, self.auth_password), headers=headers)

        if request.ok:
            return request.content
        else:
            return None
