from marshmallow import Schema, fields

from .validators import geq_zero

from .identifiers import (
                         AccountIdentifierSchema,
                         BlockIdentifierSchema,
                         NetworkIdentifierSchema,
                         TransactionIdentifierSchema
                         )

from .objects import AmountSchema, BlockSchema, SigningPayloadSchema, TransactionSchema, OperationSchema

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

class ConstructionCombineResponseSchema(Schema):
    """
    ref: models/ConstructionCombineResponse.yaml
    """
    signed_transaction = fields.Str(required=True)

class ConstructionDeriveResponseSchema(Schema):
    """
    ref: models/ConstructionDeriveResponse.yaml
    """
    address = fields.Str()
    account_identifier = fields.Nested(AccountIdentifierSchema)
    metadata = fields.Dict()

class TransactionIdentifierResponseSchema(Schema):
    """
    ref: models/TransactionIdentifierResponse.yaml
    """
    transaction_identifier = fields.Nested(TransactionIdentifierSchema)
    metadata = fields.Dict()

class ConstructionMetadataResponseSchema(Schema):
    """
    ref: models/ConstructionMetadataResponse.yaml
    """
    metadata = fields.Dict(required=True)
    suggested_fee = fields.List(fields.Nested(AmountSchema))


class ConstructionParseResponseSchema(Schema):
    """
    ref: models/ConstructionParseResponse.yaml
    """
    operations = fields.List(fields.Nested(OperationSchema))
    signers = fields.List(fields.Str())
    account_identifier_signers = fields.List(fields.Nested(AccountIdentifierSchema))
    metadata = fields.Dict()

class ConstructionPayloadsResponseSchema(Schema):
    """
    ref: models/ConstructionPayloadsResponse.yaml
    """
    unsigned_transaction = fields.Str(required=True)
    payloads = fields.List(fields.Nested(SigningPayloadSchema))

class ConstructionPreprocessResponseSchema(Schema):
    """
    ref: models/ConstructionPreprocessResponse.yaml
    """
    options = fields.Dict()
    required_public_keys = fields.List(fields.Nested(AccountIdentifierSchema))