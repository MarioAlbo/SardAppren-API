import shutil

from rest_framework.test import APITestCase


class SardanaFileViewTest(APITestCase):

    def setUp(self):
        self.sardana1_path = "sardanas/tests/res/sardana1.mp3"
        self.sardana2_path = "sardanas/tests/res/sardana2.mp3"
        self.MEDIA_ROOT = 'test'

    def tearDown(self):
        shutil.rmtree(self.MEDIA_ROOT)

    def create_sample_sardana(self):
        params = {
            "title": "Sardana 1",
            "first_compass_position": 5.29,
            "number_curts": 24,
            "number_llargs": 32,
            "beats_per_minute_curts": 5.4,
            "beats_per_minute_llargs": 5.6
        }
        post_response = self.client.post("/sardanas/", params, format='json')
        sardana_id = post_response.data['id']
        return sardana_id
