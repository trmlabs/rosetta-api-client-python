import asyncio
import itertools

def chunk(it, size):
    it = iter(it)
    for c in iter(lambda: tuple(islice(it, size)), ()):
        yield c

async def post_request(session, url, request):
    """
    Parameters
    ----------
    session: aiohttp.ClientSession
    url: str
    request: dict
    """
    return await session.post(url, json=request)

async def post_requests(session, request_map, concurrent_requests=0):
    """
    Parameters
    ----------
    session: aiohttp.ClientSession
    dict: url -> request
    """
    requests = []
    for i, (url, request) in enumerate(request_map.items()):
        requests.append(asyncio.create_task(post_request(session, url, request)))
    
    if concurrent_requests <= 0:
        yield await asyncio.gather(*requests)
    else:
        for group in chunk(requests, concurrent_requests):
            yield await asyncio.gather(*group)