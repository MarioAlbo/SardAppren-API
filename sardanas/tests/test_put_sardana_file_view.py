import os

from rest_framework import status

from sardanas.models import Sardana
from sardanas.tests.sardana_file_view_test import SardanaFileViewTest


class PutSardanaFileViewTest(SardanaFileViewTest):

    def test_upload_file_responses_204_no_content(self):
        sardana_id = self._create_sample_sardana()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as file:
                put_response = self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": file},
                                               format='multipart')

        self.assertEquals(status.HTTP_204_NO_CONTENT, put_response.status_code)

    def test_upload_file_saves_file(self):
        sardana_id = self._create_sample_sardana()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as file:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": file}, format='multipart')

        sardana = Sardana.objects.get(pk=sardana_id)
        self.assertTrue(bool(sardana.file))
        self.assertTrue(os.path.isfile(self.MEDIA_ROOT + os.sep + "sardana1.mp3"))

    def test_when_upload_file_remove_previous_file(self):
        sardana_id = self._create_sample_sardana()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as sardana1:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana1}, format='multipart')
            with open(self.sardana_2_path, 'rb') as sardana2:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana2}, format='multipart')

        self.assertEquals(1, len(os.listdir(self.MEDIA_ROOT)))
        self.assertFalse(os.path.exists(self.MEDIA_ROOT + os.sep + "sardana1.mp3"))

    def test_when_upload_file_updates_file(self):
        sardana_id = self._create_sample_sardana()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as sardana1:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana1}, format='multipart')
            with open(self.sardana_2_path, 'rb') as sardana2:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana2}, format='multipart')

        sardana = Sardana.objects.get(pk=sardana_id)
        self.assertEquals("sardana2.mp3", sardana.file.name)
        self.assertTrue(os.path.isfile(self.MEDIA_ROOT + os.sep + "sardana2.mp3"))
