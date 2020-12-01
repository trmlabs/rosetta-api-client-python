from marshmallow import Schema, fields

from .validators import geq_zero
from .identifiers import BlockIdentifierSchema, TransactionIdentifierSchema

class OperationSchema(Schema):
    pass

class TransactionSchema(Schema):
    transaction_identifier = fields.Nested(TransactionIdentifierSchema, required=True)
    operations = fields.List(fields.Nested(OperationSchema))
    metadata = fields.Dict()

class BlockSchema(Schema):
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    parent_block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    timestamp = fields.Integer(required=True, validate=geq_zero)
    transactions = fields.List(fields.Nested(TransactionSchema))
    metadata = fields.Dict()
    

class AmountSchema(Schema):
    pass

class CurrencySchema(Schema):
    pass

class ErrorSchema(Schema):
    pass

class SigningPayloadSchema(Schema):
    pass

class PublicKeySchema(Schema):
    pass

class SignatureSchema(Schema):
    pass
