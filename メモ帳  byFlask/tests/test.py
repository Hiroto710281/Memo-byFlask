 import unittest

import main


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        client = main.app.test_client()
        rv = client.post('/', data=dict(memo='テスト'))
        self.html = rv.data.decode('utf-8').lower()

    def test_result(self):
        self.assertTrue('テスト' in self.html, msg='メモが正しく書き込まれていません')
