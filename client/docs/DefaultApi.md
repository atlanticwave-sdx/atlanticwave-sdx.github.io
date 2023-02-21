# openapi_client.DefaultApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_topology**](DefaultApi.md#delete_topology) | **DELETE** /v1/topology/{topology_id} | Delete a Topology
[**get_user_user_id**](DefaultApi.md#get_user_user_id) | **GET** /users/{user_id} | Get User Info by User ID
[**patch_users_user_id**](DefaultApi.md#patch_users_user_id) | **PATCH** /users/{user_id} | Update User Information
[**post_user**](DefaultApi.md#post_user) | **POST** /user | Create New User


# **delete_topology**
> delete_topology(topology_id)

Delete a Topology

id of topology that nedds to be deleted.

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_message import ErrorMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    topology_id = 1 # int | Id of an existing topology.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Topology
        api_instance.delete_topology(topology_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| Id of an existing topology. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_user_id**
> User get_user_user_id(user_id)

Get User Info by User ID

Retrieve the information of the user with the matching user ID.

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.error_message import ErrorMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_id = "user_id_example" # str | Id of an existing user.

    # example passing only required values which don't have defaults set
    try:
        # Get User Info by User ID
        api_response = api_instance.get_user_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_user_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of an existing user. |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Found |  -  |
**404** | User Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users_user_id**
> User patch_users_user_id(user_id)

Update User Information

Update the information of an existing user.

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.patch_users_user_id_request import PatchUsersUserIdRequest
from openapi_client.model.error_message import ErrorMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_id = "user_id_example" # str | Id of an existing user.
    patch_users_user_id_request = PatchUsersUserIdRequest(
        user_name="user_name_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        password="password_example",
        user_status=True,
    ) # PatchUsersUserIdRequest | Patch user properties to update. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update User Information
        api_response = api_instance.patch_users_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->patch_users_user_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update User Information
        api_response = api_instance.patch_users_user_id(user_id, patch_users_user_id_request=patch_users_user_id_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->patch_users_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of an existing user. |
 **patch_users_user_id_request** | [**PatchUsersUserIdRequest**](PatchUsersUserIdRequest.md)| Patch user properties to update. | [optional]

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Updated |  -  |
**404** | User Not Found |  -  |
**409** | Email Already Taken |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> User post_user()

Create New User

Create a new user

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.post_user_request import PostUserRequest
from openapi_client.model.error_message import ErrorMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    post_user_request = PostUserRequest(
        user_name="user_name_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        password="password_example",
    ) # PostUserRequest | Post the necessary fields for the API to create a new user. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create New User
        api_response = api_instance.post_user(post_user_request=post_user_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->post_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_request** | [**PostUserRequest**](PostUserRequest.md)| Post the necessary fields for the API to create a new user. | [optional]

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Created |  -  |
**400** | Missing Required Information |  -  |
**409** | Email Already Taken |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

