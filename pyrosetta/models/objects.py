from marshmallow import Schema, fields

from .validators import geq_zero, SignatureType, CurveType
from .identifiers import (BlockIdentifierSchema, 
                          TransactionIdentifierSchema,
                          OperationIdentifierSchema,
                          AccountIdentifierSchema
                          )

from ._objects import CoinChangeSchema

class OperationSchema(Schema):
    """
    ref: models/Operation.yaml
    """
    operation_identifier = fields.Nested(OperationIdentifierSchema, required=True)
    related_operations = fields.List(fields.Nested(OperationIdentifierSchema))
    type = fields.Str(required=True)
    status = fields.Str(required=True)
    account = fields.Nested(AccountIdentifierSchema)
    coin_change = fields.Nested(CoinChangeSchema)
    metadata = fields.Dict()

class TransactionSchema(Schema):
    """
    ref: models/Transaction.yaml
    """
    transaction_identifier = fields.Nested(TransactionIdentifierSchema, required=True)
    operations = fields.List(fields.Nested(OperationSchema))
    metadata = fields.Dict()

class BlockSchema(Schema):
    """
    ref: models/Block.yaml
    """
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    parent_block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    timestamp = fields.Integer(required=True, validate=geq_zero)
    transactions = fields.List(fields.Nested(TransactionSchema))
    metadata = fields.Dict()
    
class CurrencySchema(Schema):
    """
    ref: models/Currency.yaml
    """
    symbol = fields.Str(required=True)
    decimals = fields.Integer(required=True, validate=geq_zero)
    metadata = fields.Dict()

class AmountSchema(Schema):
    """
    ref: models/Amount.yaml
    """
    value = fields.Str(required=True)
    currency = fields.Nested(CurrencySchema, required=True)
    metadata = fields.Dict()


class ErrorSchema(Schema):
    """
    ref: models/Error.yaml
    """
    code = fields.Integer(required=True, validate=geq_zero)
    message = fields.Str(required=True)
    description = fields.Str()
    retriable = fields.Boolean(required=True)
    details = fields.Dict()

class SigningPayloadSchema(Schema):
    """
    ref: models/SigningPayload.yaml
    """
    address = fields.Str()
    account_identifier = fields.Nested(AccountIdentifierSchema)
    hex_bytes = fields.Str(required=True)
    signature_type = fields.Str(validate=SignatureType)

class PublicKeySchema(Schema):
    """
    ref: models/PublicKey.yaml
    """
    hex_bytes = fields.Str(required=True)
    curve_type = fields.Str(required=True, validate=CurveType)

class SignatureSchema(Schema):
    """
    ref: models/Signature.yaml
    """
    sigining_payload = fields.Nested(SigningPayloadSchema, required=True)
    public_key = fields.Nested(PublicKeySchema, required=True)
    signature_type = fields.Str(required=True, validate=SignatureType)
    hex_bytes = fields.Str(required=True)
