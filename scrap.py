from pyrosetta.endpoints.data import get_available_networks
from pyrosetta.models import MetadataRequest

req = MetadataRequest()
print(get_available_networks(req))