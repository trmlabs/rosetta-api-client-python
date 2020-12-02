from marshmallow import Schema, fields

from .identifiers import (
                          AccountIdentifierSchema,
                          BlockIdentifierSchema,
                          CoinIdentifierSchema,
                          NetworkIdentifierSchema,
                          PartialBlockIdentifierSchema, 
                          TransactionIdentifierSchema
                          )

from .objects import (
                      AmountSchema, 
                      CurrencySchema, 
                      OperationSchema, 
                      PublicKeySchema, 
                      SignatureSchema
                     )

from .validators import Operator, NonNegative

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

class ConstructionCombineRequestSchema(Schema):
    """
    ref: models/ConstructionCombineRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    unsigned_transaction = fields.Str(required=True)
    signatures = fields.List(fields.Nested(SignatureSchema))

class ConstructionDeriveRequestSchema(Schema):
    """
    ref: models/ConstructionDeriveRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    public_key = fields.Nested(PublicKeySchema, required=True)
    metadata = fields.Dict()

class ConstructionHashRequestSchema(Schema):
    """
    ref: models/ConstructionHashRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    signed_transaction = fields.Str(required=True)

class ConstructionMetadataRequestSchema(Schema):
    """
    ref: models/ConstructionMetadataRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    options = fields.Dict()
    public_keys = fields.List(fields.Nested(PublicKeySchema))

class ConstructionParseRequestSchema(Schema):
    """
    ref: models/ConstructionParseRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    signed = fields.Boolean(required=True)
    transaction = fields.Str(required=True)

class ConstructionPayloadsRequestSchema(Schema):
    """
    ref: models/ConstructionPayloadRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    operations = fields.List(fields.Nested(OperationSchema))
    metadata = fields.Dict()
    public_keys = fields.List(fields.Nested(PublicKeySchema))

class ConstructionPreprocessRequestSchema(Schema):
    """
    ref: models/ConstructionPreprocessRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    operations = fields.List(fields.Nested(OperationSchema))
    metadata = fields.Dict()
    max_fee = fields.List(fields.Nested(AmountSchema))
    suggested_fee_multiplier = fields.Float()

class ConstructionSubmitRequestSchema(Schema):
    """
    ref: models/ConstructionSubmitRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    signed_transaction = fields.Str(required=True)

class EventsBlocksRequestSchema(Schema):
    """
    ref: models/EventsBlocksRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    offset = fields.Integer(validate=NonNegative)
    limit = fields.Integer(validate=NonNegative)

class SearchTransactionsRequestSchema(Schema):
    """
    ref: models/SearchTransactionsRequest.yaml
    """
    network_identifier = fields.Nested(NetworkIdentifierSchema, required=True)
    operator = fields.Str(validate=Operator)
    max_block = fields.Integer(validate=NonNegative)
    offset = fields.Integer(validate=NonNegative)
    limit = fields.Integer(validate=NonNegative)
    transaction_identifier = fields.Nested(TransactionIdentifierSchema)
    account_identifier = fields.Nested(AccountIdentifierSchema)
    coin_identifier = fields.Nested(CoinIdentifierSchema)
    currency = fields.Nested(CurrencySchema)
    status = fields.Str()
    type = fields.Str()
    address = fields.Str()
    success = fields.Boolean()