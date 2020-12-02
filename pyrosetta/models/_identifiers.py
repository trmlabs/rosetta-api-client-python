from marshmallow import Schema, fields

from .validators import geq_zero

class CoinIdentifierSchema(Schema):
    """
    ref: models/CoinIdentifier.yaml
    """
    identifier = fields.Str(required=True)
    
class PartialBlockIdentifierSchema(Schema):
    """
    ref: models/PartialBlockIdentifier.yaml
    """
    index = fields.Integer(validate=geq_zero)
    hash = fields.Str()