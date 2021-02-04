import unittest
from jasperclient import jasperclient

__TEST_URL__ = 'http://your_domain:8080/jasperserver/'
__SERVER_VERSION__ = '7.2.0'


class JasperTest(unittest.TestCase):

    def setUp(self):
        self.client = jasperclient.JasperClient(__TEST_URL__)

    def test_server_version(self):
        self.assertIsNotNone(self.client.server_version, "Error getting server information")

    def test_server_version(self):
        self.assertEqual(self.client.server_version, __SERVER_VERSION__, "Not the expected version")


if __name__ == '__main__':
    unittest.main()
