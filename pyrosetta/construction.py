from typing import Any, Dict, List, Optional

import requests

from .models import (
    ConstructionCombineRequest,
    ConstructionDeriveRequest,
    ConstructionDeriveResponse,
    ConstructionHashRequest,
    ConstructionMetadataRequest,
    ConstructionMetadataResponse,
    ConstructionParseRequest,
    ConstructionParseResponse,
    ConstructionPayloadsRequest,
    ConstructionPayloadsResponse,
    ConstructionPreprocessRequest,
    ConstructionPreprocessResponse,
    ConstructionSubmitRequest,
    NetworkIdentifier,
    Operation,
    PublicKey,
    Signature,
    TransactionIdentifierResponse
)

from .endpoints.construction import (
    create_request_to_fetch_metadata,
    create_network_transaction_from_signatures,
    derive_account_id_from_pubkey,
    generate_unsigned_transaction_and_signing_payloads,
    get_hash_of_signed_transaction,
    get_metadata_for_transaction_construction,
    parse_transaction,
    submit_signed_transaction
)

def combine(api_url : str, network_id : NetworkIdentifier, unsigned_transaction : str, signatures : List[Signature], session : Optional[requests.Session] = None) -> str:
    """
    Combine will create a network-specific transaction from an unsigned transaction and an array of signatures.
    A signed transaction will be returned which should then be sent to the submit method.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    unsigned_transaction: str
    signatures: list[Signature]
    session: requests.Session, optional
    
    Returns
    -------
    str
        This is the signed transaction which should then be passed along to the submit method.
    """
    req = ConstructionCombineRequest(network_identifier=network_id, unsigned_transaction=unsigned_transaction, signatures=signatures)
    resp = create_network_transaction_from_signatures(api_url, req, session)
    return resp.signed_transaction

def derive(api_url : str, network_id : NetworkIdentifier, public_key : PublicKey, session : Optional[requests.Session] = None, **kwargs) -> ConstructionDeriveResponse:
    """
    Get the network-specific account identifier associated with the public key.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    public_key: PublicKey
    **kwargs
        Any additional metadata to be passed along to the /construction/derive request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    ConstructionDeriveResponse
        address: str, optional
        account_identifier: AccountIdentifier, optional
        metadata: dict[str, Any], optional
    """
    req = ConstructionDeriveRequest(network_identifier=network_id, public_key=public_key, metadata=kwargs)
    return derive_account_id_from_pubkey(api_url, req, session)

def signed_transaction_hash(api_url : str, network_id : NetworkIdentifier, signed_transaction : str, sesison : Optional[requests.Session] = None) -> TransactionIdentifierResponse:
    """
    Get the network-specific hash of the signed transaction.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    signed_transaction: str
    session: requests.Session, optional

    Returns
    -------
    TransactionIdentifierResponse
        transaction_identifier: TransacitonIdentifier
        metadata: dict[str, Any], optional
    """
    req = ConstructionHashRequest(network_identifier=network_id, signed_transaction=signed_transaction)
    return get_hash_of_signed_transaction(api_url, req, session)

def metadata(api_url : str, network_id : NetworkIdentifier, options : Optional[Dict[str, Any]] = None, 
             public_keys : Optional[List[PublicKey]] = None, session : Optional[requests.Session] = None) -> ConstructionMetadataResponse:
    """
    Get any information needed to construction a transaction for a specific network.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    options: dict[str, Any], optional
    public_keys: list[PublicKey], optional
    session: requests.Session, optional

    Returns
    -------
    ConstructionMetadataResponse
        metadata: dict[str, Any]
        suggested_fee: list[Amount], optional
    """
    req = ConstructionMetadataRequest(network_identifier=network_id, options=options, public_keys=public_keys)
    return get_metadata_for_transaction_construction(api_url, req, session)

def parse(api_url : str, network_id : NetworkIdentifier, signed : bool, transaction : str, session : Optional[request.Session]= None) -> ConstructionParseResponse:
    """
    Called on both signed and unsigned transactions to understand the intent of transaction.

    A nice sanity check before signing (payloads) and broadcasting (combine).

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    signed: bool
    transaction: str
        This should be the return of either payloads or combine.
    session: requests.Session, optional

    Returns
    -------
    ConstructionParseResponse
        operations: list[Operation]
        signers: list[str], optional
        account_identifier_signers: list[AccountIdentifier], optional
        metadata: dict[str, Any], optional
    """
    req = ConstructionParseRequest(network_identifier=network_id, signed=signed, transaction=transaction)
    return parse_transaction(api_url, req, session)


def payloads(api_url : str, network_id : NetworkIdentifier, operations : List[Operation], 
             metadata : Optional[Dict[str, Any]] = None, public_keys : Optional[List[PublicKey]] = None, 
             session : Optional[requests.Session]) -> ConstructionPayloadsResponse:
    """
    Called with an array of operations and the metadata from the metadata method.
    
    Returns an unsigned transaction blob and collection of payloads that must be signed
    by particular AccountIdentifiers using a certain SignatureType.

    The array of Operations often times cannot specify all the "effects" of a transaciton,
    however the "intent" can be deterministically specified. Parsing the transaction via the
    Data API will contain a superset of the Operations provided here.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    metadata: dict[str, Any], optional
        This is the metadata returned from the metadata method.
    public_keys: list[PublicKey], optional
    session: requests.Session, optional

    Returns
    -------
    ConstructionPayloadsResponse
        unsigned_transaction: str
        payloads: list[SigningPayload]
    """
    req = ConstructionPayloadsRequest(network_identifier=network_id, operations=operations, metadata=metadata, public_keys=public_keys)
    return generate_unsigned_transaction_and_signing_payloads(api_url, req, session)

def preprocess(api_url : str, network_id : NetworkIdentifier, operations : List[Operation], metadata : Optional[Dict[str, Any]] = None,
               max_fee : Optional[List[Amount]] = None, suggested_fee_multiplier : Optional[float] = None, 
               session : Optional[requests.Session] = None) -> ConstructionPreprocessResponse:
    """
    Called prior to payloads to construct a request for any metadata needed. 

    The returned `options` will be sent to the metadata method unmodified.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    opertations: list[Operation]
    metadata: dict[str, Any], optional
    max_fee: list[Amount], optional
    suggest_fee_multiplier: float, optional
    session: requests.Session, optional

    Returns
    -------
    ConstructionPreprocessResponse
        options: dict[str, Any], optional
            These options are sent directly to the metadata method
        required_public_keys: list[AccountIdentifier], optional
    """
    req = ConstructionPreprocessRequest(network_identifier=network_id, operations=operations, metadata=metadata, max_fee=max_fee, suggested_fee_multiplier=suggested_fee_multiplier)
    return create_request_to_fetch_metadata(api_url, req, session)

def submit(api_url : str, network_id : NetworkIdentifier, signed_transaction : str, session : Optional[requests.Sesison] = None) -> TransactionIdentifierResponse:
    """
    Submit a pre-signed transaction to the node.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    signed_transaction: str
    session: requests.Session, optional

    Returns
    -------
    TransactionIdentifierResponse
        transaction_identifier: TransacitonIdentifier
        metadata: dict[str, Any], optional
    """
    req = ConstructionSubmitRequest(network_identifier=network_id, signed_transaction=signed_transaction)
    return submit_signed_transaction(api_url, req, session)
