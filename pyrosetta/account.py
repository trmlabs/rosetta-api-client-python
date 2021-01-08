"""
State of accounts.
"""

from typing import List, Optional

import requests

from .models import (
    AccountBalanceRequest,
    AccountBalanceResponse,
    AccountConinsRequest,
    AccountCoinsResponse,
    AccountIdentifier,
    Currency,
    NetworkIdentifier,
    PartialBlockIdentifier
)

from .endpoints.data import (
    get_account_balance,
    get_account_unspent_coins
)

def balance(api_url : str, network_id: NetworkIdentifier, account_id : AccountIdentifier, block_id : Optional[PartialBlockIdentifier] = None, currencies : Optional[List[Currency]] = None, session : Optional[requests.Session] = None) -> AccountBalanceResponse:
    """
    Parameters
    -----------
    api_url : str
        The url to the node's api.
    network_id : NetworkIdentifier
    account_id: AccountIdentifier
        Any included metadata is also included in being checked for uniqueness.
    block_id : PartialBlockIdentifier, optional
        It may be possible to specify only the index or hash. If neither is specified,
        it's assumed the current block is being requested.
    currencies, optional:
        Only balance of type Currency is returned. If none are specified, all 
        available currencies will be returned. 
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.


    Returns
    -------
    AccountBalanceResponse
    """
    req = AccountBalanceRequest(network_id, account_id, block_id, currencies)
    return get_account_balance(api_url, req, session)

def unspent_coins(api_url : str, network_id : NetworkIdentifier, account_id : AccountIdentifier, include_mempool : bool, currencies : Optional[List[Currency]] = None, session : Optional[requests.Session] = None) -> AccountCoinsResponse:
    """
    Parameters
    ----------
    api_url : str
        The url to the node's api.
    network_id : NetworkIdentifier
    account_id : AccountIdentifier
        Any included metadata is also included in being checked for uniqueness.
    include_mempool: bool
        Include the state from the mempool when looking up an account's unspent coins. Note,
        using this functionality breaks any guarantee of idempotency.
    currencies: list[Currency], optional
        Only balance of type Currency is returned. If none are specified, all 
        available currencies will be returned.
    session : requests.Session, optional
        The persistent requests session to use. If none is
        provided, a new session will be created for the single
        request.

    Returns 
    --------
    AccountCoinsResponse
    """
    req = AccountBalanceRequest(network_id, account_id, include_mempool, currencies)
    return get_account_unspent_coins(api_url, req, session)