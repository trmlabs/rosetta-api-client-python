from typing import Optional

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
    url = '{}/events/blocks'.format(api_url)
    resp = post_request(url, req.json(), session)
    return EventsBlocksResponse(**resp.json())

def search_for_transactions(api_url : str, req : SearchTransactionsRequest, session : Optional[requests.Session] = None) -> EventsBlocksResponse:
    """
    req: SearchTransactionsRequest
    resp: SearchTransactionsResponse
    ref: /search/transactions
    """
    url = '{}/search/transactions'.format(api_url)
    resp = post_request(url, req.json(), session)
    return SearchTransactionsResponse(**resp.json())