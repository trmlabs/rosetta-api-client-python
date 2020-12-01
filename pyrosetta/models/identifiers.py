from marshmallow import Schema, fields

from .validators import geq_zero

class BlockIdentifierSchema(Schema):
    index = fields.Integer(required=True, validate=geq_zero)
    hash = fields.Str(required=True)

class SubNetworkIdentifierSchema(Schema):
    network = fields.Str(required=True)
    metadata = fields.Dict()

class NetworkIdentifierSchema(Schema):
    blockchain = fields.Str(required=True)
    network = fields.Str(required=True)
    sub_network_identifier = fields.Nested(SubNetworkIdentifierSchema)

class TransactionIdentifierSchema(Schema):
    hash = fields.Str(required=True)


class OperationIdentifierSchema(Schema):
    index = fields.Integer(required=True, validate=geq_zero)
    network_index = fields.Integer(validate=geq_zero)
    
class SubAccountIdentfierSchema(Schema):
    address = fields.Str(required=True)
    metadata = fields.Dict()
    
class AccountIdentifierSchema(Schema):
    address = fields.Str(required=True)
    sub_account = fields.Nested(SubAccountIdentfierSchema)
    metadata = fields.Dict()