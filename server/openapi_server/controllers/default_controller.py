import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_message import ErrorMessage  # noqa: E501
from openapi_server.models.patch_users_user_id_request import PatchUsersUserIdRequest  # noqa: E501
from openapi_server.models.post_user_request import PostUserRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def delete_topology(topology_id):  # noqa: E501
    """Delete a Topology

    id of topology that nedds to be deleted. # noqa: E501

    :param topology_id: Id of an existing topology.
    :type topology_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_user_id(user_id):  # noqa: E501
    """Get User Info by User ID

    Retrieve the information of the user with the matching user ID. # noqa: E501

    :param user_id: Id of an existing user.
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def patch_users_user_id(user_id, patch_users_user_id_request=None):  # noqa: E501
    """Update User Information

    Update the information of an existing user. # noqa: E501

    :param user_id: Id of an existing user.
    :type user_id: str
    :param patch_users_user_id_request: Patch user properties to update.
    :type patch_users_user_id_request: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        patch_users_user_id_request = PatchUsersUserIdRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_user(post_user_request=None):  # noqa: E501
    """Create New User

    Create a new user # noqa: E501

    :param post_user_request: Post the necessary fields for the API to create a new user.
    :type post_user_request: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_user_request = PostUserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
