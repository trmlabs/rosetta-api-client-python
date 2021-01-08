"""
Get current version, status, and useful initialization info of the supported
network(s).
"""

from textwrap import indent
from typing import Any, List, Optional, NamedTuple

from .models import (
    MetadataRequest,
    NetworkIdentifier,
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

def discover_networks(**kwargs) -> List[NetworkOverview]:
    """
    Discover the availble networks supported by the Rosetta server
    and any information about them.

    Parameters
    ----------
    **kwargs
        Any additional metadata to be passed along to the /network/list request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    List[NetworkOverview]
    """
    nws = []
    network_ids = supported_networks(**kwargs)
    for network_id in network_ids:
        opts = _supported_network_options(network_id)
        status = _network_status(network_id)
        nws.append(NetworkOverview(network_id, opts, status))
    return nws

def supported_networks(**kwargs) -> List[NetworkIdentifier]:
    """
    Get a list of networks that the Rosetta server supports.

    Parameters
    ----------
    **kwargs
        Any additional metadata to be passed along to the /network/list request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    List[NetworkIdentifier]
        A list of networks that the rosetta server supports.
    """
    req = MetadataRequest(metadata=kwargs)
    resp = get_available_networks(req)
    return resp.network_identifiers


def _supported_network_options(network_identifier : NetworkIdentifier) -> ImplementationDetails:
    """
    Parameters
    ----------
    network_identifier: NetworkIdentifier

    Returns
    -------
    NetworkOptionsResponse
    """
    resp = get_network_options(network_identifier)
    return ImplementationDetails(resp.version, resp.details)

def supported_network_options(blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> ImplementationDetails:
    """
    Parameters
    ----------
    blockchain: str
        The name of the blockchain. Ex: 'bitcoin'
    network: str
        The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
    subnetwork: str, optional
        The name or identifier of the subnetwork if needed. Ex: 'shard-1'
    subnetwork_metadata: dict[str, Any], optional
        Any additional metadata needed to identify the subnetwork. See the
        individual node implementation to verifiy if additional metadata is needed.
    ** kwargs
        Any additional metadata to be passed along to the request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    NetworkOptionsResponse
    """
    subnetwork_id = None
    if subnetwork is not None:
        subnetwork_id = SubNetworkIdentifier(network=subnetwork, metadata=subnetwork_metadata)
    network_id = NetworkIdentifier(blockchain=blockchain, network=network, subnetwork=subnetwork_id, metadata=kwargs)
    return _supported_network_options(network_id)

def _network_status(network_identifier : NetworkIdentifier) -> NetworkStatusResponse:
    """
    Parameters
    ----------
    network_identifier: NetworkIdentifier

    Returns
    -------
    NetworkStatusResponse
    """
    return get_network_status(network_identifier)

def network_status(blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> NetworkStatusResponse:
    """
    Parameters
    ----------
    blockchain: str
        The name of the blockchain. Ex: 'bitcoin'
    network: str
        The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
    subnetwork: str, optional
        The name or identifier of the subnetwork if needed. Ex: 'shard-1'
    subnetwork_metadata: dict[str, Any], optional
        Any additional metadata needed to identify the subnetwork. See the
        individual node implementation to verifiy if additional metadata is needed.
    ** kwargs
        Any additional metadata to be passed along to the request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    NetworkStatusResponse
    """
    subnetwork_id = None
    if subnetwork is not None:
        subnetwork_id = SubNetworkIdentifier(network=subnetwork, metadata=subnetwork_metadata)
    network_id = NetworkIdentifier(blockchain=blockchain, network=network, subnetwork=subnetwork_id, metadata=kwargs)
    return _network_status(network_id)
