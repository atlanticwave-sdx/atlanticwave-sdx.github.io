"""
    SDX LC

    SDX Topology validation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: lmarinve@fiu.edu
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.topology_api import TopologyApi  # noqa: E501


class TestTopologyApi(unittest.TestCase):
    """TopologyApi unit test stubs"""

    def setUp(self):
        self.api = TopologyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_topology(self):
        """Test case for add_topology

        Send a new topology to SDX-LC  # noqa: E501
        """
        pass

    def test_get_topology_id(self):
        """Test case for get_topology_id

        get an existing topology  # noqa: E501
        """
        pass

    def test_get_topology_list(self):
        """Test case for get_topology_list

        get an existing topology  # noqa: E501
        """
        pass

    def test_update_topology(self):
        """Test case for update_topology

        Update an existing topology  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()