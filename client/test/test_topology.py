"""
    SDX LC

    SDX Topology validation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: lmarinve@fiu.edu
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.link import Link
from openapi_client.model.node import Node
globals()['Link'] = Link
globals()['Node'] = Node
from openapi_client.model.topology import Topology


class TestTopology(unittest.TestCase):
    """Topology unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTopology(self):
        """Test Topology"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Topology()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
