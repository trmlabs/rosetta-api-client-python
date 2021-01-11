from typing import Any, Dict, Optional

import requests

def post_request(url : str, data : Dict[str, Any], session : Optional[requests.Session] = None) -> requests.Response:
    """
    Post a request to the url with the given data,
    optionally using a provided session.

    Parameters
    ----------
    url: str
        The url to post to.
    data: dict[str, Any]
        The json data to include in the post request.
    session: requests.Session, optional
        The persistent session to use, if None is provided
        a new one will be created and destroyed for the
        individual call.
    """
    if session is not None:
        return session.post(url, data=data)
    return requests.post(url, data=data)
