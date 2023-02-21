# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.topology import Topology  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTopologyController(BaseTestCase):
    """TopologyController integration test stubs"""

    def test_add_topology(self):
        """Test case for add_topology

        Send a new topology to SDX-LC
        """
        topology = {"topology_id":"urn:sdx:topology:amlight.net","name":"AmLight-OXP","version":2,"model_version":"1.0.0","time_stamp":"2021-07-07 21:19:40","nodes":[],"links":[]}
        headers = { 
        }
        response = self.client.open(
            '/v1/topology',
            method='POST',
            headers=headers,
            data=json.dumps(topology),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_topology_id(self):
        """Test case for get_topology_id

        get an existing topology
        """
        headers = { 
        }
        response = self.client.open(
            '/v1/topology/{topology_id}'.format(topology_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_topology_list(self):
        """Test case for get_topology_list

        get an existing topology
        """
        headers = { 
        }
        response = self.client.open(
            '/v1/topology',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_topology(self):
        """Test case for update_topology

        Update an existing topology
        """
        topology = openapi_server.Topology()
        headers = { 
        }
        response = self.client.open(
            '/v1/topology/{topology_id}'.format(topology_id=56),
            method='PATCH',
            headers=headers,
            data=json.dumps(topology),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
