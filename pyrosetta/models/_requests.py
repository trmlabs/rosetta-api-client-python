from marshmallow import Schema, fields

from .identifiers import (AccountIdentifierSchema, 
                          BlockIdentifierSchema,
                          NetworkIdentifierSchema, 
                          TransactionIdentifierSchema
                          )

from ._identifiers import PartialBlockIdentifierSchema

from .objects import CurrencySchema

class MetadataRequestSchema(Schema):
    """
    ref: models/MetadataRequest.yaml
    """
    metadata = fields.Dict()
    
class NetworkRequestSchema(Schema):
    """
    ref: models/NetworkRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    metadata = fields.Dict()
    
class AccountBalanceRequestSchema(Schema):
    """
    ref: models/AccountBalanceRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    account_identifier = fields.Nested(AccountIdentifierSchema, required=True)
    block_identifier = fields.Nested(PartialBlockIdentifierSchema)
    currencies = fields.List(fields.Nested(CurrencySchema))
    
class AccountCoinsRequestSchema(Schema):
    """
    ref: models/AccountCoinsRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    account_identifier = fields.Nested(AccountIdentifierSchema, required=True)
    include_mempool = fields.Boolean(required=True)
    currencies = fields.List(fields.Nested(CurrencySchema))
    
class BlockRequestSchema(Schema):
    """
    ref: models/BlockRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    block_identifier = fields.Nested(PartialBlockIdentifierSchema, required=True)
    
class BlockTransactionRequestSchema(Schema):
    """
    ref: models/BlockTransactionRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    transaction_identifier = fields.Nested(TransactionIdentifierSchema, required=True)
    
class MempoolTransactionRequestSchema(Schema):
    """
    ref: models/MempoolTransactionRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    transaction_identifier = fields.Nested(TransactionIdentifierSchema, required=True)
    