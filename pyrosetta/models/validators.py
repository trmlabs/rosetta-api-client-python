from marshmallow import ValidationError

def geq_zero(n):
    return n >= 0

def CoinAction(s):
    """
    ref: models/CoinAction.yaml
    """
    if s not in ('coin_created', 'coin_spent'):
        raise ValidationError('{} is not a valid CoinAction'.format(s))
    return True

def SignatureType(s):
    """
    ref: models/SignatureType.yaml
    """
    if s not in ('ecdsa', 'ecdsa_recovery', 'ed25519', 'schnorr_1', 'schnorr_poseidon'):
        raise ValidationError('{} is not a valid SignatureType'.format(s))
    return True

def CurveType(s):
    """
    ref: models/CurveType.yaml
    """
    if s not in ('secp256k1', 'secp256r1', 'edwards25519', 'tweedle'):
        raise ValidationError('{} is not a valid CurveType'.format(s))
    return True

def ExemptionType(s):
    """
    ref: models/ExemptionType.yaml
    """
    if s not in ('greater_or_equal', 'less_or_equal', 'dynamic'):
        raise ValidationError('{} is not a valid ExemptionType'.format(s))
    return True