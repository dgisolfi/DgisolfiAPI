# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPagesController(BaseTestCase):
    """PagesController integration test stubs"""

    def test_add_page(self):
        """Test case for add_page

        Upload a HTML Page.
        """
        query_string = [('filename', 'filename_example')]
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1//pages',
            method='POST',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_page(self):
        """Test case for delete_page

        Delete a HTML file by name
        """
        query_string = [('filename', 'filename_example')]
        response = self.client.open(
            '/api/v1//pages',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_page(self):
        """Test case for get_page

        Get a html file by page name
        """
        query_string = [('filename', 'filename_example')]
        response = self.client.open(
            '/api/v1//pages',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_page(self):
        """Test case for update_page

        Update a HTML Page.
        """
        query_string = [('filename', 'filename_example')]
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1//pages',
            method='PUT',
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
