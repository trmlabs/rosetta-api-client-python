from marshmallow import Schema, fields

from .validators import geq_zero, SignatureType, CurveType, CoinAction, BlockEventType, ExemptionType

from .identifiers import (BlockIdentifierSchema, 
                          TransactionIdentifierSchema,
                          OperationIdentifierSchema,
                          AccountIdentifierSchema,
                          CoinIdentifierSchema
                          )

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

class CoinChangeSchema(Schema):
    """
    ref: models/CoinChange.yaml
    """
    coin_identifier = fields.Nested(CoinIdentifierSchema, required=True)
    coin_aciton = fields.Str(required=True, validate=CoinAction)

class CoinSchema(Schema):
    """
    ref: models/Coin.yaml
    """
    coin_identifier = fields.Nested(CoinIdentifierSchema, required=True)
    amount = fields.Nested(AmountSchema, required=True)

class OperationStatusSchema(Schema):
    """
    ref: models/OperationStatus.yaml
    """
    status = fields.Str(required=True)
    successful = fields.Boolean(required=True)

class VersionSchema(Schema):
    """
    ref: models/Version.yaml
    """
    rosetta_version = fields.Str(required=True)
    node_version = fields.Str(required=True)
    middleware_version = fields.Str()
    metadata = fields.Dict()
    
class BalanceExemptionSchema(Schema):
    """
    ref: models/BalanceExemption.yaml
    """
    sub_account_address = fields.Str()
    currency = fields.Nested(CurrencySchema)
    exemption_type = fields.Str(validate=ExemptionType)
    
class AllowSchema(Schema):
    """
    ref: models/Allow.yaml
    """
    operation_statuses = fields.List(fields.Nested(OperationStatusSchema))
    opertaion_types = fields.List(fields.Str())
    errors = fields.List(fields.Nested(ErrorSchema))
    historical_balance_lookup = fields.Boolean(required=True)
    timestamp_start_index = fields.Integer(validate=geq_zero)
    call_methods = fields.List(fields.Str())
    balance_exemptions = fields.List(fields.Nested(BalanceExemptionSchema))
    mempool_coins = fields.Boolean(required=True)
    
class SyncStatusSchema(Schema):
    """
    ref: models/SyncStatus.yaml
    """
    current_index = fields.Integer(required=True, validate=geq_zero)
    target_index = fields.Integer(validate=geq_zero)
    stage = fields.Str()
    
class PeerSchema(Schema):
    """
    ref: models/Peer.yaml
    """
    peer_id = fields.Str(required=True)
    metadata = fields.Dict()

class BlockEventSchema(Schema):
    """
    ref: models/BlockEvent.yaml
    """
    sequence = fields.Integer(required=True, validate=geq_zero)
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    type = fields.Str(required=True, validate=BlockEventType)

class BlockTransactionSchema(Schema):
    """
    ref: models/BlockTransaction.yaml
    """
    block_identifier = fields.Nested(BlockIdentifierSchema, required=True)
    transaction = fields.Nested(TransactionSchema, required=True)