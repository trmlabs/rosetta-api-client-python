def get_range_of_block_events(req : EventsBlocksRequest):
    """
    req: EventsBlocksRequest
    resp: EventsBlocksResponse
    ref: /events/blocks
    """
    url = '{}/events/blocks'.format(API_URL)
    resp = post_request(url, req.json())
    return EventsBlocksResponse(**resp.json())

def search_for_transactions(req : SearchTransactionsRequest):
    """
    req: SearchTransactionsRequest
    resp: SearchTransactionsResponse
    ref: /search/transactions
    """
    url = '{}/search/transactions'.format(API_URL)
    resp = post_request(url, req.json())
    return SearchTransactionsResponse(**resp.json())