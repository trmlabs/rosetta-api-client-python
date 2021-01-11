from typing import List, Optional

import requests

from .models import (
    NetworkIdentifier,
    NetworkRequest,
    TransactionIdentifier,
    MempoolTransactionRequest,
    MempoolTransactionResponse
)

from .endpoints.data import (
    get_mempool_transaction,
    get_mempool_transaction_ids
)

def all_transactions(api_url : str, network_id : NetworkIdentifier, session : Optional[requests.Session] = None, **kwargs) -> List[TransactionIdentifier]:
    """
    Get all the transactions in the mempool.

    Parameters
    ----------
    api_url: str,
    network_id: NetworkIdentifier
    session: requests.Session, optional
    **kwargs
        Any additional metadata to be passed along to the /mempool request. 
        See the individual node implementation to verify if additional
        metadata is needed.

    Returns
    -------
    list[TransactionIdentifier]
    """
    req = NetworkRequest(network_identifier=network_id, metadata=kwargs)
    resp = get_mempool_transaction_ids(api_url, req, session)
    return resp.transaction_identifiers


def transaction(api_url : str, network_id : NetworkIdentifier, transaction_id : TransactionIdentifier, session : Optional[requests.Session] = None) -> MempoolTransactionResponse:
    """
    Get a specific transaction in the mempool.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    transaction_id: TransactionIdentifier
    session: requests.Session, optional

    Returns
    -------
    MempoolTransactionResponse
    """
    req = MempoolTransactionRequest(network_identifier=network_id, transaction_identifier=transaction_id)
    return get_mempool_transaction(api_url, req, session)
