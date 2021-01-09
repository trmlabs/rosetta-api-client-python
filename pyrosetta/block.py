from typing import Optional

import requests

from .models import (
    BlockIdentifier,
    BlockRequest,
    BlockResponse,
    BlockTransactionRequest,
    BlockTransactionResponse,
    NetworkIdentifier,
    PartialBlockIdentifier,
    TransactionIdentifier
)

from .endpoints.data import (
    get_block,
    get_block_transaction
)

def block(api_url : str, network_id : NetworkIdentifier, block_id : PartialBlockIdentifier, session : Optional[requests.Sesion] = None) -> BlockResponse:
    """
    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    block_id: PartialBlockIdentifier
    session: requests.Session, optional

    Returns
    -------
    BlockResponse
    """
    req = BlockRequest(network_identifier=network_id, block_identifier=block_id)
    return get_block(api_url, req, session)

def transaction(api_url : str, network_id : NetworkIdentifier, block_id : BlockIdentifier, transaction_id : TransactionIdentifier, session : Optional[requests.Sesison] = None) -> BlockTransactionResponse:
    """
    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    block_id: BlockIdentifier
    transaction_id: TransactionIdentifier
    session: requests.Session, optional

    Returns
    -------
    BlockTransactionResponse
    """
    req = BlockTransactionRequest(network_identifier=network_id, block_identifier=block_id, transaction_identifier=transaction_id)
    return get_block_transaction(api_url, req, session)