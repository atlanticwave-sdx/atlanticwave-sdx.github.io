# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_delete_topology(self):
        """Test case for delete_topology

        Delete a Topology
        """
        headers = { 
        }
        response = self.client.open(
            '/v1/topology/{topology_id}'.format(topology_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_user_id(self):
        """Test case for get_user_user_id

        Get User Info by User ID
        """
        headers = { 
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_users_user_id(self):
        """Test case for patch_users_user_id

        Update User Information
        """
        inline_object = openapi_server.InlineObject()
        headers = { 
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id='user_id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_user(self):
        """Test case for post_user

        Create New User
        """
        inline_object1 = openapi_server.InlineObject1()
        headers = { 
        }
        response = self.client.open(
            '/user',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object1),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
