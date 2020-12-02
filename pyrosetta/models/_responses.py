from marshmallow import Schema, fields

from .validators import geq_zero

from .identifiers import NetworkIdentifierSchema, BlockIdentifierSchema, TransactionIdentifierSchema

from .objects import AmountSchema, BlockSchema, TransactionSchema

from ._objects import (VersionSchema, 
                       AllowSchema, 
                       SyncStatusSchema, 
                       PeerSchema,
                       CoinSchema
                       )

class NetworkListResponseSchema(Schema):
    """
    ref: models/NetworkListResponse.yaml
    """
    network_identifiers = fields.List(fields.Nested(NetworkIdentifierSchema))
    
class NetworkOptionsResponseSchema(Schema):
    """
    ref: models/NetworkOptionsResponse.yaml
    """
    version = fields.Nested(VersionSchema)
    allow = fields.Nested(AllowSchema)
    
class NetworkStatusResponseSchema(Schema):
    """
    ref: models/NetworkStatusResponse.yaml
    """
    current_block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    current_block_timestamp = fields.Integer(required=True, validate=geq_zero)
    genesis_block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    oldest_block_identifier = fields.Nested(BlockIdentifierSchema)
    sync_status = fields.Nested(SyncStatusSchema)
    peers = fields.List(fields.Nested(PeerSchema))


class AccountBalanceResponseSchema(Schema):
    """
    ref: models/AccountBalanceResponse.yaml
    """
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    balances = fields.List(fields.Nested(AmountSchema))
    metadata = fields.Dict()
    
class AccountCoinsResponseSchema(Schema):
    """
    ref: models/AccountCoinsResponse.yaml
    """
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    balances = fields.List(fields.Nested(CoinSchema))
    metadata = fields.Dict()
    
class BlockResponseSchema(Schema):
    """
    ref: models/BlockResponse.yaml
    """
    block = fields.Nested(BlockSchema)
    other_transactions = fields.List(fields.Nested(TransactionIdentifierSchema))
    
class BlockTransactionResponseSchema(Schema):
    """
    ref: models/BlockTransactionResponse.yaml
    """
    transaction = fields.Nested(TransactionSchema, required=True)
    
class MempoolResponseSchema(Schema):
    """
    ref: models/MempoolResponse.yaml
    """
    transaction_identifiers = fields.List(fields.Nested(TransactionIdentifierSchema))
    
class MempoolTransactionResponseSchema(Schema):
    """
    ref: models/MempoolTransactionResponse.yaml
    """
    transaction = fields.Nested(TransactionSchema, required=True)
    metadata = fields.Dict()
    