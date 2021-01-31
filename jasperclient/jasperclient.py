

class JasperClient:

    def __init__(self, server_url):
        self.url = server_url

    def __del__(self):
        pass

    @staticmethod
    def server_info():
        return 'tests'
