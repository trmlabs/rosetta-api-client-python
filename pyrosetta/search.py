from typing import Optional

import requests

from .models import (
    AccountIdentifier,
    CoinIdentifier,
    Currency,
    Operator,
    NetworkIdentifier,
    TransactionIdentifier,
    SearchTransactionsRequest,
    SearchTransactionsResponse
)

from .endpoints.indexer import search_for_transactions

def transactions(api_url : str, network_id : NetworkIdentifier, operator : Optional[Operator] = "and",
                 max_block : Optional[int] = None, offset : Optional[int] = None, limit : Optional[int] = None,
                 transaction_id : Optional[TransactionIdentifier] = None, account_id : Optional[AccountIdentifier] = None,
                 coin_id : Optional[CoinIdentifier] = None, currency : Optional[Currency] = None,
                 status : Optional[str] = None, type_ : Optional[str] = None, address : Optional[str] = None,
                 success : Optional[bool] = None, sesion : Optional[requests.Session] = None) -> SearchTransactionsResponse:
    """
    Search for transactions that match given conditions.

    Parameters
    ----------
    api_url: str
    network_id: NetworkIdenfier
    operator: Operator, optional
        This is either "and" or "or", and determines how multiple conditions
        should be applied. Defaults to "and"
    max_block: int, optional
        The newest block to consider when searching. If none is provided,
        the current block is assumed.
    offset: int, optional
        Offset into the query result to start returning transactions.
        If any query parameters are changed, this offset will also change.
    limit: int, optional
        The maximum number of transactions to return in a call.
    transaction_id : TransactionIdentifier, optional
    account_id : AccountIdentifier, optional
        Any included metadata in this will be considered unique when searching
    coin_id: CoinIdentifier, optional
    currency: Currency, optional
    status: str, optional
        The network-specific operation type.
    type_: str, optional
        the network-specific operation type.
    address: str, optional
        The AccountIdentifier.address, this will get all transactions related to
        an account address regardless of the subaccount.
    success: bool, optional
        A synthetic condition populated by parsing network-specific operation statuses 
        (using the mapping provided in /network/options).
    session: requests.Session, optional

    Returns
    -------
    SearchTransactionsResponse
        transactions: list[BlockTransaction]
        total_count: int
        next_offset: int, optional
            Used when paginated results, if this is not populated
            there are no more results.
    """
    req = SearchTransactionsRequest(network_identifier=network_id, operator=operator, max_block=max_block,
                                    offset=offset, limit=limit, transaction_identifier=transaction_id,
                                    account_identifier=account_id, coin_identifier=coin_id, currency=currency,
                                    status=status, type=type_, address=address, success=success)
    return search_for_transactions(api_url, req, session)
