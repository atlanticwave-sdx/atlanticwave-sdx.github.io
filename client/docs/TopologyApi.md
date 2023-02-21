# openapi_client.TopologyApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_topology**](TopologyApi.md#add_topology) | **POST** /v1/topology | Send a new topology to SDX-LC
[**get_topology_id**](TopologyApi.md#get_topology_id) | **GET** /v1/topology/{topology_id} | get an existing topology
[**get_topology_list**](TopologyApi.md#get_topology_list) | **GET** /v1/topology | get an existing topology
[**update_topology**](TopologyApi.md#update_topology) | **PATCH** /v1/topology/{topology_id} | Update an existing topology


# **add_topology**
> Topology add_topology(topology)

Send a new topology to SDX-LC

Create a topology

### Example


```python
import time
import openapi_client
from openapi_client.api import topology_api
from openapi_client.model.topology import Topology
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
    api_instance = topology_api.TopologyApi(api_client)
    topology = Topology(
        topology_id="urn:sdx:topology:WBqUULeGNgcXUQlU.iCVqz",
        name="amLight",
        version=1,
        model_version="model_version_example",
        time_stamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        nodes=[
            Node(
                node_id="urn:sdx:node:WBqUULeGNgcXUQlU.iCVqz",
                name="amLight",
                location=Location(
                    address="address_example",
                    latitude=-90.0,
                    longitude=-90.0,
                ),
                ports=[
                    Port(
                        port_id="urn:sdx:port:WBqUULeGNgcXUQlU.iCVqz",
                        name="WBqUULeGNgcXUQlU.iCVqz",
                        node="node_example",
                        type="100FE",
                        mtu=1,
                        status="up",
                        state="enabled",
                    ),
                ],
            ),
        ],
        links=[
            Link(
                link_id="urn:sdx:link:WBqUULeGNgcXUQlU.iCVqz",
                name="WBqUULeGNgcXUQlU.iCVqz",
                ports=[
                    Port(
                        port_id="urn:sdx:port:WBqUULeGNgcXUQlU.iCVqz",
                        name="WBqUULeGNgcXUQlU.iCVqz",
                        node="node_example",
                        type="100FE",
                        mtu=1,
                        status="up",
                        state="enabled",
                    ),
                ],
                type="intra",
                bandwidth=1,
                residual_bandwidth=0,
                latency=1,
                packet_loss=0,
                availability=0,
                status="up",
                state="enabled",
            ),
        ],
    ) # Topology | placed for adding a new topology

    # example passing only required values which don't have defaults set
    try:
        # Send a new topology to SDX-LC
        api_response = api_instance.add_topology(topology)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopologyApi->add_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology** | [**Topology**](Topology.md)| placed for adding a new topology |

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Connection |  -  |
**405** | Invalid input |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_id**
> Topology get_topology_id(topology_id)

get an existing topology

ID of the topology

### Example


```python
import time
import openapi_client
from openapi_client.api import topology_api
from openapi_client.model.topology import Topology
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
    api_instance = topology_api.TopologyApi(api_client)
    topology_id = 1 # int | Id of an existing topology.

    # example passing only required values which don't have defaults set
    try:
        # get an existing topology
        api_response = api_instance.get_topology_id(topology_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopologyApi->get_topology_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| Id of an existing topology. |

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Topology not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_list**
> Topology get_topology_list()

get an existing topology

ID of the topology

### Example


```python
import time
import openapi_client
from openapi_client.api import topology_api
from openapi_client.model.topology import Topology
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = topology_api.TopologyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get an existing topology
        api_response = api_instance.get_topology_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopologyApi->get_topology_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology**
> Topology update_topology(topology_id)

Update an existing topology

ID of topology that needs to be updated.

### Example


```python
import time
import openapi_client
from openapi_client.api import topology_api
from openapi_client.model.topology import Topology
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
    api_instance = topology_api.TopologyApi(api_client)
    topology_id = 1 # int | Id of an existing topology.
    topology = Topology(
        topology_id="urn:sdx:topology:WBqUULeGNgcXUQlU.iCVqz",
        name="amLight",
        version=1,
        model_version="model_version_example",
        time_stamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        nodes=[
            Node(
                node_id="urn:sdx:node:WBqUULeGNgcXUQlU.iCVqz",
                name="amLight",
                location=Location(
                    address="address_example",
                    latitude=-90.0,
                    longitude=-90.0,
                ),
                ports=[
                    Port(
                        port_id="urn:sdx:port:WBqUULeGNgcXUQlU.iCVqz",
                        name="WBqUULeGNgcXUQlU.iCVqz",
                        node="node_example",
                        type="100FE",
                        mtu=1,
                        status="up",
                        state="enabled",
                    ),
                ],
            ),
        ],
        links=[
            Link(
                link_id="urn:sdx:link:WBqUULeGNgcXUQlU.iCVqz",
                name="WBqUULeGNgcXUQlU.iCVqz",
                ports=[
                    Port(
                        port_id="urn:sdx:port:WBqUULeGNgcXUQlU.iCVqz",
                        name="WBqUULeGNgcXUQlU.iCVqz",
                        node="node_example",
                        type="100FE",
                        mtu=1,
                        status="up",
                        state="enabled",
                    ),
                ],
                type="intra",
                bandwidth=1,
                residual_bandwidth=0,
                latency=1,
                packet_loss=0,
                availability=0,
                status="up",
                state="enabled",
            ),
        ],
    ) # Topology |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing topology
        api_response = api_instance.update_topology(topology_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopologyApi->update_topology: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing topology
        api_response = api_instance.update_topology(topology_id, topology=topology)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TopologyApi->update_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| Id of an existing topology. |
 **topology** | [**Topology**](Topology.md)|  | [optional]

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Topology not found |  -  |
**405** | Validation exception |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

