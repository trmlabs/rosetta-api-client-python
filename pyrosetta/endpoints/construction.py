def create_network_transaction_from_signatures(req : ConstructionCombineRequest):
    """
    req: ConstructionCombineRequest
    resp: ConstructionCombineResponse
    ref: /construction/combine
    """
    url = '{}/construction/combine'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionCombineResponse(**resp.json())

def derive_account_id_from_pubkey(req : ConstructionDeriveRequest):
    """
    req: ConstructionDeriveRequest
    resp: ConstructionDeriveResponse
    ref: /construction/derive
    """
    url = '{}/construction/derive'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionDeriveResponse(**resp.json())

def get_hash_of_signed_transaction(req : ConstructionHashRequest):
    """
    req: ConstructionHashRequest
    resp: TransactionIdentifierResponse
    ref: /construction/hash
    """
    url = '{}/construction/hash'.format(API_URL)
    resp = post_request(url, req.json())
    return TransactionIdentifierResponse(**resp.json())

def get_metadata_for_transaction_construction(req : ConstructionMetadataRequest):
    """
    req: ConstructionMetadataRequest
    resp: ConstructionMetadataResponse
    ref: /construction/metadata
    """
    url = '{}/construction/metadata'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionMetadataResponse(**resp.json())

def parse_transaction(req : ConstructionParseRequest):
    """
    req: ConstructionParseRequest
    resp: ConstructionParseResponse
    ref: /construction/parse
    """
    url = '{}/construction/parse'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionParseResponse(**resp.json())

def generate_unsigned_transaction_and_signing_payloads(req : ConstructionPayloadsRequest):
    """
    req: ConstructionPayloadsRequest
    resp: ConstructionPayloadsResponse
    ref: /construction/payloads
    """
    url = '{}/construction/payloads'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionPayloadsResponse(**resp.json())

def create_request_to_fetch_metadata(req : ConstructionPreprocessRequest):
    """
    req: ConstructionPreprocessRequest
    resp: ConstructionPreprocessResponse
    ref: /construction/preprocess
    """
    url = '{}/construction/preprocess'.format(API_URL)
    resp = post_request(url, req.json())
    return ConstructionPreprocessResponse(**resp.json())

def submit_signed_transaction(req : ConstructionSubmitRequest):
    """
    req: ConstructionSubmitRequest
    resp: TransactionIdentifierResponse
    ref: /construction/submit
    """
    url = '{}/construction/submit'.format(API_URL)
    resp = post_request(url, req.json())
    return TransactionIdentifierResponse(**resp.json())