def create_network_transaction_from_signatures():
    """
    req: ConstructionCombineRequest
    resp: ConstructionCombineResponse
    ref: /construction/combine
    """
    pass

def derive_account_id_from_pubkey():
    """
    req: ConstructionDeriveRequest
    resp: ConstructionDeriveResponse
    ref: /construction/derive
    """
    pass

def get_hash_of_signed_transaction():
    """
    req: ConstructionHashRequest
    resp: TransactionIdentifierResponse
    ref: /construction/hash
    """
    pass

def get_metadata_for_transaction_construction():
    """
    req: ConstructionMetadataRequest
    resp: ConstructionMetadataResponse
    ref: /construction/metadata
    """
    pass

def parse_transaction():
    """
    req: ConstructionParseRequest
    resp: ConstructionParseResponse
    ref: /construction/parse
    """
    pass

def generate_unsigned_transaction_and_signing_payloads():
    """
    req: ConstructionPayloadsRequest
    resp: ConstructionPayloadsResponse
    ref: /construction/payloads
    """
    pass

def create_request_to_fetch_metadata():
    """
    req: ConstructionPreprocessRequest
    resp: ConstructionPreprocessResponse
    ref: /construction/preprocess
    """
    pass

def submit_signed_transaction():
    """
    req: ConstructionSubmitRequest
    resp: TransactionIdentifierResponse
    ref: /construction/submit
    """
    pass