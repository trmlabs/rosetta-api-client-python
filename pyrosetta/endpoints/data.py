from .. import API_URL

from ..models import (
                      AccountBalanceRequest,
                      AccountCoinsRequest,
                      BlockRequest,
                      BlockTransactionRequest,
                      MempoolTransactionRequest,
                      MetadataRequest,
                      NetworkRequest,
                      NetworkListResponse,
                      NetworkOptionsResponse,
                      NetworkStatusResponse
                     )

from ..utils.communication import post_request

def get_available_networks(req : MetadataRequest):
    """
    req: MetadataRequest
    resp: NetworkListResponse
    ref: /network/list
    """
    url = '{}/network/list'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkListResponse(**resp.json())

def get_network_options(req: NetworkRequest):
    """
    req: NetworkRequest
    resp: NetworkOptionsResponse
    ref: /network/options
    """
    url = '{}/network/options'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkOptionsResponse(**resp.json())

def get_network_status(req: NetworkRequest):
    """
    req: NetworkRequest
    resp: NetworkStatusResponse
    ref: /network/status
    """
    url = '{}/network/status'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkStatusResponse(**resp.json())

def get_account_balance(req : AccountBalanceRequest):
    """
    req: AccountBalanceRequest
    resp: AccountBalanceResponse
    ref: /account/balance
    """
    url = '{}/account/balance'.format(API_URL)
    resp = post_request(url, req.json())
    return AccountBalanceResponse(**resp.json())

def get_account_unspent_coins():
    """
    req: AccountCoinsRequest
    resp: AccountCoinsResponse
    ref: /account/coins
    """
   pass


def get_block():
    """
    req: BlockRequest
    resp: BlockResponse
    ref: /block
    """
    pass
    
def get_block_transaction():
    """
    req: BlockTransacitonRequest
    resp: BlockTransactionResponse
    ref: /block/transaction
    """
    pass


def get_mempool_transaction_ids():
    """
    req: NetworkRequest
    resp: MempoolResponse
    ref: /mempool
    """
    pass

def get_mempool_transaction():
    """
    req: MempoolTransactionRequest
    resp: MempoolTransactionResponse
    ref: /mempool/transaction
    """
    pass