from marshmallow import Schema, fields

from .validators import NonNegative

class BlockIdentifierSchema(Schema):
    """
    ref: models/BlockIdentifier.yaml
    """
    index = fields.Integer(required=True, validate=NonNegative)
    hash = fields.Str(required=True)

class SubNetworkIdentifierSchema(Schema):
    """
    ref: models/SubNetworkIdentifier.yaml
    """
    network = fields.Str(required=True)
    metadata = fields.Dict()

class NetworkIdentifierSchema(Schema):
    """
    ref: models/Identifier.yaml
    """
    blockchain = fields.Str(required=True)
    network = fields.Str(required=True)
    sub_network_identifier = fields.Nested(SubNetworkIdentifierSchema)

class TransactionIdentifierSchema(Schema):
    """
    ref: models/TransactionIdentifier.yaml
    """
    hash = fields.Str(required=True)

class OperationIdentifierSchema(Schema):
    """
    ref: models/OperationIdentifier.yaml
    """
    index = fields.Integer(required=True, validate=NonNegative)
    network_index = fields.Integer(validate=NonNegative)
    
class SubAccountIdentfierSchema(Schema):
    """
    ref: models/SubAccountIdentfier.yaml
    """
    address = fields.Str(required=True)
    metadata = fields.Dict()
    
class AccountIdentifierSchema(Schema):
    """
    ref: models/AccountIdentifier.yaml
    """
    address = fields.Str(required=True)
    sub_account = fields.Nested(SubAccountIdentfierSchema)
    metadata = fields.Dict()

class CoinIdentifierSchema(Schema):
    """
    ref: models/CoinIdentifier.yaml
    """
    identifier = fields.Str(required=True)
    
class PartialBlockIdentifierSchema(Schema):
    """
    ref: models/PartialBlockIdentifier.yaml
    """
    index = fields.Integer(validate=NonNegative)
    hash = fields.Str()