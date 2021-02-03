"""
Convience functions for constructing objects from CLI accessible
parameters.
"""
from typing import Any, Dict, List, Iterable, Optional, Union

from ..models import (
    AccountIdentifier,
    BlockIdentifier,
    Currency,
    NetworkIdentifier,
    PartialBlockIdentifier,
    SubAccountIdentifier,
    SubNetworkIdentifier
)

def make_NetworkIdentifier(blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None) -> NetworkIdentifier:
    """
    Parameters
    ----------
    blockchain: str
        The name of the blockchain. Ex: 'bitcoin'
    network: str
        The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
    subnetwork: str, optional
        The name or identifier of the subnetwork if needed. Ex: 'shard-1'
    subnetwork_metadata: dict[str, Any], optional
        Any additional metadata needed to identify the subnetwork. See the
        individual node implementation to verifiy if additional metadata is needed.

    Returns
    -------
    NetworkIdentifier
    """
    subnetwork_id = None
    if subnetwork is not None:
        subnetwork_id = SubNetworkIdentifier(network=subnetwork, metadata=subnetwork_metadata)
    return NetworkIdentifier(blockchain=blockchain, network=network, subnetwork=subnetwork_id)


def make_AccountIdentifier(address : str, subaccount_address : Optional[str] = None, subaccount_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> AccountIdentifier:
    """
    Parameters
    ----------
    address: str
        Either a cryptographic key or a username
    subaccount_address: str, optional
        Either a cryptographic value or another unique identifier for the SubAccount
    subaccount_metadata: dict[str, Any], optional
        Any additional metadata needed to uniquely identify a SubAccount. NOTE: Two
        SubAccounts with the same address but different metadata are considered different
        SubAccounts.
    **kwargs
        Any additional metadata to identify the Account. Any blockchains that utilize a username
        for the address over a public key should specify the public keys here.

    Return
    ------
    AccountIdentifier
    """
    subaccount_id = None
    if subaccount_address is not None:
        subaccount_id = SubAccountIdentifier(address=subaccount_address, metadata=subaccount_metadata)
    return AccountIdentifier(address=address, sub_account=subaccount_id, metadata=kwargs)


def make_PartialBlockIdentifier(index : Optional[int] = None, hash_ : Optional[str] = None) -> PartialBlockIdentifier:
    """
    NOTE: At least the index or hash must be specified.

    Parameters
    ----------
    index: int
        The block height
    hash_: str
        The hash of the block

    Returns
    -------
    PartialBlockIdentifier

    Raises
    ------
    ValueError: If neither the index or hash is provided.
    """
    if index is None and hash_ is None:
        raise ValueError("A value for either index or hash_ must be provided.")
    return PartialBlockIdentifier(index=index, hash=hash_)


def make_Currencies(symbols : Union[str, Iterable[str]], decimals : Union[int, Iterable[int]], 
                    metadata : Optional[Union[Dict[str, Any], Iterable[Union[None, Dict[str, Any]]]]] = None) -> List[Currency]:
    """
    If any of the parameters are iterables, all parameters should be iterables of even length.
    
    Parameters
    ----------
    symbols: str, Iterable[str]
        A single str, or an iterable of string of the symbols of the currencies.
    decimals: int, Iterable[int]
        A single int, or an iterable of ints, representing the number of decimals
        in the atomic unit of the currencies.
    metadata: dict[str, Any], Iterable[dict[str, Any]], optional
        A single dict, or an iterable of dicts, representing the metadata of the
        currencies.
    
    Raises
    ------
    ValueError: If the length of the iterables isn't even across the parameters.

    Returns
    -------
    list[Currency]
    """
    if isinstance(symbols, str):
        if not isinstance(decimals, int):
            raise ValueError("The length of all the currencies parameters must be the same.")
        if metadata is not None:
            if not isinstance(metadata, dict):
                raise ValueError("The length of all the currencies parameters must be the same.")
        return [make_Currency(symbols, decimals, metadata)]
    
    if len(symbols) != len(decimals):
        raise ValueError("The length of all the currencies parameters must be the same.")
    if metadata is not None:
        if len(metadata) != len(symbols):
            raise ValueError("The length of all the currencies parameters must be the same.")
    else:
        metadata = [None]*len(symbols)
    
    currencies = []
    for sym, dec, md in zip(symbols, decimals, metadata):
        currencies.append(make_Currency(symbol, decimals, **metadata))
    return currencies

def make_Currency(symbol : str, decimals : int, metadata : Optional[Dict[str, Any]] = None) -> Currency:
    """
    Parameters
    ----------
    symbol: str
        The symbol associated with the currency.
    decimals: int
        The number of decimal places in the standard unit example. For
        example BTC has 8 decimals (10**8 satoshis), this doesn't assume
        base 10 though.
    **kwargs
        Any additional metadata related to the currency itself.
    """
    return Currency(symbol=symbol, decimals=decimals, metadata=metadata)

def make_Signatures():
    pass

def make_Signature():
    pass
