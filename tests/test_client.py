import unittest
from jasperclient import jasperclient


class JasperTest(unittest.TestCase):

    def setUp(self):
        self.client = jasperclient.JasperClient()

    def test_server_information(self):
        self.assertIsNotNone(self.client.server_info(), "Error getting server information")


if __name__ == '__main__':
    unittest.main()
