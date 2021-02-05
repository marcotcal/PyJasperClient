import requests
import datetime
from xml.etree import ElementTree


class JasperClient:

    class Resource:

        def __init__(self):
            self.creation_date = None
            self.label = None
            self.permission_mask = None
            self.update_date = None
            self.uri = None
            self.version = None
            self.resource_type = None

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
        req = self.session.get(cmd_url)
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

    def read_resources(self, resource_type):
        if not self.connected:
            return

        resources = []
        cmd_url = self.url + 'rest_v2/resources/?recursive=true&type={}'.format(resource_type)
        headers = {'content-type': 'application/json'}
        r = self.session.get(url=cmd_url, headers=headers)
        recs = ElementTree.fromstring(r.content.decode('utf-8'))
        for rec in recs:
            a = self.Resource()
            for field in rec:
                if field.tag == 'creationDate':
                    a.creation_date = datetime.datetime.strptime(field.text, '%Y-%m-%dT%H:%M:%S')
                elif field.tag == 'label':
                    a.label = field.text
                elif field.tag == 'permissionMask':
                    a.permission_mask = field.text
                elif field.tag == 'uri':
                    a.uri = field.text
                elif field.tag == 'version':
                    a.version = field.text
                elif field.tag == 'resourceType':
                    a.resource_type = field.text

            resources.append(a)

        return resources

    def execute_report(self, uri, params, output):
        if not self.connected:
            return None

        cmd_url = self.url + 'rest_v2/reports' + uri + '.pdf'
        req = self.session.get(cmd_url, params=params)
        if req.ok:
            if output is not None:
                file = open(output, "wb")
                file.write(req.content)
                return None
            else:
                return req.content

