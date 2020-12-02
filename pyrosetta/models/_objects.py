from marshmallow import Schema, fields

from .objects import CurrencySchema, ErrorSchema, AmountSchema

from .validators import CoinAction, ExemptionType, geq_zero
from ._identifiers import CoinIdentifierSchema

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