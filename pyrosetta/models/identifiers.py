from marshmallow import Schema, fields

from .validators import geq_zero

class BlockIdentifierSchema(Schema):
    """
    ref: models/BlockIdentifier.yaml
    """
    index = fields.Integer(required=True, validate=geq_zero)
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
    index = fields.Integer(required=True, validate=geq_zero)
    network_index = fields.Integer(validate=geq_zero)
    
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