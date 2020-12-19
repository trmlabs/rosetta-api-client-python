from pyrosetta.endpoints.data import get_available_networks, get_network_options
from pyrosetta.models import MetadataRequest, NetworkRequest

req=MetadataRequest()
net_info=get_available_networks(req)

req2 = NetworkRequest(net_info.network_identifiers[0])
print(get_network_options(req2))