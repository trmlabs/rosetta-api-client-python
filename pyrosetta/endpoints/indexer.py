from typing import Optional
from urllib.parse import urljoin

import requests

from ..models import (
    EventsBlocksRequest,
    EventsBlocksResponse,
    SearchTransactionsRequest,
    SearchTransactionsResponse
)

from ..utils.communication import post_request

def get_range_of_block_events(api_url : str, req : EventsBlocksRequest, session : Optional[requests.Session] = None) -> EventsBlocksResponse:
    """
    req: EventsBlocksRequest
    resp: EventsBlocksResponse
    ref: /events/blocks
    """
    url = urljoin(api_url, 'events/blocks')
    resp = post_request(url, req.json(), session)
    return EventsBlocksResponse(**resp.json())

def search_for_transactions(api_url : str, req : SearchTransactionsRequest, session : Optional[requests.Session] = None) -> EventsBlocksResponse:
    """
    req: SearchTransactionsRequest
    resp: SearchTransactionsResponse
    ref: /search/transactions
    """
    url = urljoin(api_url, 'search/transactions')
    resp = post_request(url, req.json(), session)
    return SearchTransactionsResponse(**resp.json())
