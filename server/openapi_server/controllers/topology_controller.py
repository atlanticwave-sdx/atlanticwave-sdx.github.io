import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.topology import Topology  # noqa: E501
from openapi_server import util


def add_topology(topology):  # noqa: E501
    """Send a new topology to SDX-LC

    Create a topology # noqa: E501

    :param topology: placed for adding a new topology
    :type topology: dict | bytes

    :rtype: Union[Topology, Tuple[Topology, int], Tuple[Topology, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        topology = Topology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_topology_id(topology_id):  # noqa: E501
    """get an existing topology

    ID of the topology # noqa: E501

    :param topology_id: Id of an existing topology.
    :type topology_id: int

    :rtype: Union[Topology, Tuple[Topology, int], Tuple[Topology, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_topology_list():  # noqa: E501
    """get an existing topology

    ID of the topology # noqa: E501


    :rtype: Union[Topology, Tuple[Topology, int], Tuple[Topology, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_topology(topology_id, topology=None):  # noqa: E501
    """Update an existing topology

    ID of topology that needs to be updated. # noqa: E501

    :param topology_id: Id of an existing topology.
    :type topology_id: int
    :param topology: 
    :type topology: dict | bytes

    :rtype: Union[Topology, Tuple[Topology, int], Tuple[Topology, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        topology = Topology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
