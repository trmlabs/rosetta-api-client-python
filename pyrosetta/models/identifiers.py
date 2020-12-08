from marshmallow import Schema, fields

from .validators import NonNegative

class BlockIdentifier(object):

    def __init__(self, index, hash_):
        self.index = index
        self.hash = hash_

class BlockIdentifierSchema(Schema):
    """
    ref: models/BlockIdentifier.yaml
    """
    index = fields.Integer(required=True, validate=NonNegative)
    hash = fields.Str(required=True)

class SubNetworkIdentifier(object):

    def __init__(self, network, metadata=None):
        self.network = network
        self.metadata = metadata

class SubNetworkIdentifierSchema(Schema):
    """
    ref: models/SubNetworkIdentifier.yaml
    """
    network = fields.Str(required=True)
    metadata = fields.Dict()

class NetworkIdentifier(object):

    def __init__(self, blockchain, network, sub_network_identifier=None):
        self.blockchain = blockchain
        self.network = network
        self.sub_network_identifier = sub_network_identifier


class NetworkIdentifierSchema(Schema):
    """
    ref: models/Identifier.yaml
    """
    blockchain = fields.Str(required=True)
    network = fields.Str(required=True)
    sub_network_identifier = fields.Nested(SubNetworkIdentifierSchema)

class TransactionIdentifier(object):

    def __init__(self, hash_):
        self.hash = hash_


class TransactionIdentifierSchema(Schema):
    """
    ref: models/TransactionIdentifier.yaml
    """
    hash = fields.Str(required=True)

class OperationIdentifier(object):

    def __init__(self, index, network_index=None):
        self.index = index
        self.network_index = network_index


class OperationIdentifierSchema(Schema):
    """
    ref: models/OperationIdentifier.yaml
    """
    index = fields.Integer(required=True, validate=NonNegative)
    network_index = fields.Integer(validate=NonNegative)

class SubAccountIdentfier(object):

    def __init__(self, address, metadata=None):
        self.address = address
        self.metadata = metadata


class SubAccountIdentfierSchema(Schema):
    """
    ref: models/SubAccountIdentfier.yaml
    """
    address = fields.Str(required=True)
    metadata = fields.Dict()
    
class AccountIdentifier(object):

    def __init__(self, address, sub_account=None, metadata=None):
        self.address = address
        self.sub_account = sub_account
        self.metadata = metadata

class AccountIdentifierSchema(Schema):
    """
    ref: models/AccountIdentifier.yaml
    """
    address = fields.Str(required=True)
    sub_account = fields.Nested(SubAccountIdentfierSchema)
    metadata = fields.Dict()

class CoinIdentifier(object):

    def __init__(self, indentifier):
        self.identifier = identifier


class CoinIdentifierSchema(Schema):
    """
    ref: models/CoinIdentifier.yaml
    """
    identifier = fields.Str(required=True)

class PartialBlockIdentifier(object):

    def __init__(self, index=None, hash_=None):
        self.index = index
        self.hash = hash_

class PartialBlockIdentifierSchema(Schema):
    """
    ref: models/PartialBlockIdentifier.yaml
    """
    index = fields.Integer(validate=NonNegative)
    hash = fields.Str()