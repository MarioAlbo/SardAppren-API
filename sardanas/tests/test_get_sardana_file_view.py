from rest_framework import status

from sardanas.tests.sardana_file_view_test import SardanaFileViewTest


class GetSardanaFileViewTest(SardanaFileViewTest):

    def test_download_file_responses_200_ok(self):
        sardana_id = self._create_sample_sardana()
        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as sardana:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana}, format='multipart')

            response = self.client.get("/sardanas/" + str(sardana_id) + "/file")
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_download_file_returns_file(self):
        sardana_id = self._create_sample_sardana()
        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
            with open(self.sardana_1_path, 'rb') as sardana:
                self.client.put("/sardanas/" + str(sardana_id) + "/file", {"file": sardana}, format='multipart')

            response = self.client.get("/sardanas/" + str(sardana_id) + "/file")

        with open(self.sardana_1_path, 'rb') as sardana:
            self.assertEquals(sardana.read(), response.content)
