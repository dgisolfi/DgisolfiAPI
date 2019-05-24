# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestStaticController(BaseTestCase):
    """StaticController integration test stubs"""

    def test_add_static(self):
        """Test case for add_static

        Upload a static file.
        """
        query_string = [('filename', 'filename_example')]
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1//static',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_static(self):
        """Test case for delete_static

        Delete a static file by name
        """
        query_string = [('filename', 'filename_example')]
        response = self.client.open(
            '/api/v1//static',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_static(self):
        """Test case for get_static

        Get a static file by name
        """
        query_string = [('filename', 'filename_example')]
        response = self.client.open(
            '/api/v1//static',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_static(self):
        """Test case for update_static

        Update a Static File.
        """
        query_string = [('filename', 'filename_example')]
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1//static',
            method='PUT',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
