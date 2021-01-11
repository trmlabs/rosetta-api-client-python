from typing import Optional

import requests

from .models import (
    EventsBlocksRequest,
    EventsBlocksResponse,
    NetworkIdentifier
)

from .endpoints.indexer import get_range_of_block_events

def blocks(api_url : str, network_id : NetworkIdentifier, offset : Optional[int], limit : Optional[int], 
           sesison : Optional[requests.Session] = None) -> EventsBlocksResponse:
    """
    Query a sequence of BlockEvents indicating which blocks were added and removed from
    storage to reach the current state.
    
    Parameters
    ----------
    api_url: str
    network_id: NetworkIdentifier
    offset: int, optional
        The offset into the event stream to sync events from. 
        If 0, start from the begining. If none is provided, return
        the limit from the tip.
    limit: int, optional
        The maximum number of events to fetch in one call.
    session: requests.Session, optional

    Returns
    -------
    EventsBlocksResponse
        max_sequence: int
        events: list[BlockEvent]
    """
    req = EventsBlocksRequest(network_identifier=network_id, offset=offset, limit=limit)
    return get_range_of_block_events(api_url, req, session)
