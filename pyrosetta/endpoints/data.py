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

def get_available_networks(req : MetadataRequest) -> NetworkListResponse:
    """
    req: MetadataRequest
    resp: NetworkListResponse
    ref: /network/list
    """
    url = '{}/network/list'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkListResponse(**resp.json())

def get_network_options(req: NetworkRequest) -> NetworkOptionsResponse:
    """
    req: NetworkRequest
    resp: NetworkOptionsResponse
    ref: /network/options
    """
    url = '{}/network/options'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkOptionsResponse(**resp.json())

def get_network_status(req: NetworkRequest) -> NetworkStatusResponse:
    """
    req: NetworkRequest
    resp: NetworkStatusResponse
    ref: /network/status
    """
    url = '{}/network/status'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkStatusResponse(**resp.json())

def get_account_balance(req : AccountBalanceRequest) -> AccountBalanceResponse:
    """
    req: AccountBalanceRequest
    resp: AccountBalanceResponse
    ref: /account/balance
    """
    url = '{}/account/balance'.format(API_URL)
    resp = post_request(url, req.json())
    return AccountBalanceResponse(**resp.json())

def get_account_unspent_coins(req : AccountCoinsRequest) -> AccountCoinsResponse:
    """
    req: AccountCoinsRequest
    resp: AccountCoinsResponse
    ref: /account/coins
    """
    url = '{}/account/coins'.format(API_URL)
    resp = post_request(url, req.json())
    return AccountCoinsResponse(**resp.json())


def get_block(req : BlockRequest) -> BlockResponse:
    """
    req: BlockRequest
    resp: BlockResponse
    ref: /block
    """
    url = '{}/block'.format(API_URL)
    resp = post_request(url, req.json())
    return BlockResponse(**resp.json())

    
def get_block_transaction(req : BlockTransactionRequest) -> BlockTransactionResponse:
    """
    req: BlockTransactionRequest
    resp: BlockTransactionResponse
    ref: /block/transaction
    """
    url = '{}/block/transaction'.format(API_URL)
    resp = post_request(url, req.json())
    return BlockTransactionResponse(**resp.json())



def get_mempool_transaction_ids(req : NetworkRequest) -> MempoolResponse:
    """
    req: NetworkRequest
    resp: MempoolResponse
    ref: /mempool
    """
    url = '{}/mempool'.format(API_URL)
    resp = post_request(url, req.json())
    return MempoolResponse(**resp.json())


def get_mempool_transaction(req : MempoolTransactionRequest) -> MempoolTransactionResponse:
    """
    req: MempoolTransactionRequest
    resp: MempoolTransactionResponse
    ref: /mempool/transaction
    """
    url = '{}/mempool/transaction'.format(API_URL)
    resp = post_request(url, req.json())
    return MempoolTransactionResponse(**resp.json())
