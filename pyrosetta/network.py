"""
Get current version, status, and useful initialization info of the supported
network(s).
"""
from textwrap import indent
from typing import Any, Dict, List, Optional, NamedTuple

import requests

from .models import (
    MetadataRequest,
    NetworkIdentifier,
    NetworkRequest,
    NetworkOptionsResponse,
    NetworkStatusResponse,
    SubNetworkIdentifier
)

from .endpoints.data import (
    get_network_options,
    get_network_status,
    get_supported_networks,
    
)

class NetworkOverview(NamedTuple):
    network : NetworkIdentifier
    options : NetworkOptionsResponse
    status : NetworkStatusResponse

    def __str__(self):
        nw = "Network:\n{}\n".format(self.network)
        opts = "Implementation Details:\n{}\n".format(self.options)
        status = "Status:\n{}".format(self.status)

def discover(api_url : str, session : Optional[request.Session] = None, network_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> List[NetworkOverview]:
    """
    Discover the availble networks supported by the Rosetta server
    at the api_url and any information about them.

    NOTE: If /network/options and /network/status need additional but different
    metadata, this will not work.

    Parameters
    ----------
    api_url : str
        The url to the node's api.
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.
    network_metadata: dict[str, Any], optional:
        Any additional metadata to be passed along to the /network/options
        and /network/status routes. See the individual node implementation
        to verify if additional metadata is needed.
    **kwargs
        Any additional metadata to be passed along to the /network/list request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    list[NetworkOverview]
        network: NetworkIdentifier
        options: NetworkOptionsResponse
        status: NetworkStatusRespone
    """
    nws = []
    network_ids = list_supported(api_url, session, **kwargs)
    for network_id in network_ids:
        opts = supported_options(api_url, network_id, session)
        status = status(api_url, network_id, session)
        nws.append(NetworkOverview(network_id, opts, status))
    return nws

def list_supported(api_url : str, session : Optional[requests.Session] = None, **kwargs) -> List[NetworkIdentifier]:
    """
    Get a list of networks that the Rosetta server at the api_url supports.

    Parameters
    ----------
    api_url : str
        The url to the node's api.
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.
    **kwargs
        Any additional metadata to be passed along to the /network/list request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    list[NetworkIdentifier]
    """
    req = MetadataRequest(metadata=kwargs)
    resp = get_available_networks(api_url, req, session)
    return resp.network_identifiers


def supported_options(api_url : str, network_identifier : NetworkIdentifier, session : Optional[requests.Session] = None, **kwargs) -> ImplementationDetails:
    """
    Get the supported options of a specified network 
    and usage information for the Rosetta server at the api_url.
    
    Parameters
    ----------
    api_url : str
        The url to the node's api.
    network_identifier: NetworkIdentifier
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.
    **kwargs
        Any additional metadata to be passed along to the /network/options request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    NetworkOptionsResponse
        version: Version
        allow: Allow
    """
    req = NetworkRequest(network_identifier=network_identifier, metadata=kwargs)
    return get_network_options(api_url, req, session)



def status(api_url : str, network_identifier : NetworkIdentifier, session : Optional[requests.Session] = None, **kwargs) -> NetworkStatusResponse:
    """
    Parameters
    ----------
    api_url : str
        The url to the node's api.
    network_identifier: NetworkIdentifier
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.
    **kwargs
        Any additional metadata to be passed along to the /network/status request. 
        See the individual node implementation to verify if additional
        metadata is needed.
    

    Returns
    -------
    NetworkStatusResponse
        current_block_identifier: BlockIdentifier
        current_block_timestamp: Timestamp
        genesis_block_identifier: BlockIdentifier
        oldest_block_identifier: BlockIdentifier, optional
        sync_status: SyncStatus, optional
        peers: List[Peer]
    """
    req = NetworkRequest(network_identifier=network_identifier, metadata=kwargs)
    return get_network_status(api_url, req, session)
