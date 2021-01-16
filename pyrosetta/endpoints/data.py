from typing import Optional

import requests

from ..models import (
    AccountBalanceRequest,
    AccountBalanceResponse,
    AccountCoinsRequest,
    AccountCoinsResponse,
    BlockRequest,
    BlockResponse,
    BlockTransactionRequest,
    BlockTransactionResponse,
    MempoolResponse,
    MempoolTransactionRequest,
    MempoolTransactionResponse,
    MetadataRequest,
    NetworkRequest,
    NetworkListResponse,
    NetworkOptionsResponse,
    NetworkStatusResponse
)

from ..utils.communication import post_request

def get_available_networks(api_url : str, req : MetadataRequest, session : Optional[requests.Session] = None) -> NetworkListResponse:
    """
    req: MetadataRequest
    resp: NetworkListResponse
    ref: /network/list
    """
    url = '{}/network/list'.format(api_url)
    resp = post_request(url, req.json(), session)
    return NetworkListResponse(**resp.json())

def get_network_options(api_url : str, req: NetworkRequest, session : Optional[requests.Session] = None) -> NetworkOptionsResponse:
    """
    req: NetworkRequest
    resp: NetworkOptionsResponse
    ref: /network/options
    """
    url = '{}/network/options'.format(api_url)
    resp = post_request(url, req.json(), session)
    return NetworkOptionsResponse(**resp.json())

def get_network_status(api_url : str, req: NetworkRequest, session : Optional[requests.Session] = None) -> NetworkStatusResponse:
    """
    req: NetworkRequest
    resp: NetworkStatusResponse
    ref: /network/status
    """
    url = '{}/network/status'.format(api_url)
    resp = post_request(url, req.json(), session)
    return NetworkStatusResponse(**resp.json())

def get_account_balance(api_url : str, req : AccountBalanceRequest, session : Optional[requests.Session] = None) -> AccountBalanceResponse:
    """
    req: AccountBalanceRequest
    resp: AccountBalanceResponse
    ref: /account/balance
    """
    url = '{}/account/balance'.format(api_url)
    resp = post_request(url, req.json(), session)
    return AccountBalanceResponse(**resp.json())

def get_account_unspent_coins(api_url : str, req : AccountCoinsRequest, session : Optional[requests.Session] = None) -> AccountCoinsResponse:
    """
    req: AccountCoinsRequest
    resp: AccountCoinsResponse
    ref: /account/coins
    """
    url = '{}/account/coins'.format(api_url)
    resp = post_request(url, req.json(), session)
    return AccountCoinsResponse(**resp.json())


def get_block(api_url : str, req : BlockRequest, session : Optional[requests.Session] = None) -> BlockResponse:
    """
    req: BlockRequest
    resp: BlockResponse
    ref: /block
    """
    url = '{}/block'.format(api_url)
    resp = post_request(url, req.json(), session)
    return BlockResponse(**resp.json())

    
def get_block_transaction(api_url : str, req : BlockTransactionRequest, session : Optional[requests.Session] = None) -> BlockTransactionResponse:
    """
    req: BlockTransactionRequest
    resp: BlockTransactionResponse
    ref: /block/transaction
    """
    url = '{}/block/transaction'.format(api_url)
    resp = post_request(url, req.json(), session)
    return BlockTransactionResponse(**resp.json())



def get_mempool_transaction_ids(api_url : str, req : NetworkRequest, session : Optional[requests.Session] = None) -> MempoolResponse:
    """
    req: NetworkRequest
    resp: MempoolResponse
    ref: /mempool
    """
    url = '{}/mempool'.format(api_url)
    resp = post_request(url, req.json(), session)
    return MempoolResponse(**resp.json())


def get_mempool_transaction(api_url : str, req : MempoolTransactionRequest, session : Optional[requests.Session] = None) -> MempoolTransactionResponse:
    """
    req: MempoolTransactionRequest
    resp: MempoolTransactionResponse
    ref: /mempool/transaction
    """
    url = '{}/mempool/transaction'.format(api_url)
    resp = post_request(url, req.json(), session)
    return MempoolTransactionResponse(**resp.json())
