from typing import Any, Dict, List, Iterable, Optional, Union

import requests

from .models import (
    AccountBalanceResponse,
    AccountCoinsResponse,
    AccountIdentifier,
    Amount,
    BlockIdentifier,
    BlockResponse,
    BlockTransactionResponse,
    CoinIdentifier,
    ConstructionDeriveResponse,
    ConstructionMetadataResponse,
    ConstructionParseResponse,
    ConstructionPayloadsResponse,
    Currency,
    EventsBlocksResponse,
    NetworkIdentifier,
    NetworkOptionsResponse,
    NetworkStatusResponse,
    MempoolTransactionResponse,
    Operation,
    Operator, 
    PublicKey,
    SearchTransactionsResponse,
    Signature,
    TransactionIdentifier,
    TransactionIdentifierResponse
)

from .utils import (
    make_AccountIdentifier,
    make_Currencies,
    make_NetworkIdentifier,
    make_PartialBlockIdentifier
)

import .network as net
import .account as acnt
import .block as blk
import .mempool as memp
import .construction as cst
import .events as evnt
import .search as srch

class RosettaAPI(object):

    def __init__(self, api_url: str, session : Optional[requests.Session] = None) -> None:
        """
        Parameters
        ----------
        api_url: str
            The url where the node is located.
        session: requests.Session, optional
            An already existing requests sesion. If none is passed
            a session will be created for this object.
        """
        self._api_url = api_url
        if session is None:
            session = requests.Session()
        self._session = session
        self._network_identifier = None

    @property
    def session(self) -> requests.Session:
        return self._session

    @property
    def url(self) -> str:
        return self._api_url

    
    def list_supported_networks(self, **kwargs) -> List[NetworkIdentifier]:
        """
        Get a list of supported networks.

        Parameters
        ----------
        **kwargs
            Any additional metadata to be passed along to the /network/list request. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        list[NetworkIdentifier]
            blockchain : str
            network : str
            subnetwork_id : SubNetworkIdentifier, optional
        """
        return net.list_supported(self.url, self.session, **kwargs)


    @property
    def current_network(self) -> Optional[NetworkIdentifier]:
        return self._network_identifier

    @network.setter
    def current_network(self, network_id: NetworkIdentifier) -> None:
        if not isinstance(network_id, NetworkIdentifier):
            raise ValueError("`current_network` must explicitly be a NetworkIdentifier. These are returned by the `supported_networks` method. If trying to set `current_network` by strings, see the `select_network` method.")
        self._network_identifier = network_id

    
    def select_network(self, blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None) -> None:
        """
        Select the `current_network` by known string values.
        
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
        """
        self.current_network = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)

    def _network_status(self, network_id : NetworkIdentifier, **kwargs) -> NetworkStatusResponse:
        """
        Private method for `network_status` to proivde an interface that
        supports calls with existing objects.
        """
        
        return net.status(self.url, network_id, self.session, **kwargs)
    
    def current_network_status(self, **kwargs) -> NetworkStatusRespone:
        """
        Get the status of the current network.
        
        Parameters
        ----------
        **kwargs
            Any additional metadata to be passed along to the /network/status. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        NetworkStatusResponse
            current_block_identifier: BlockIdentifier
            current_block_timestamp: Timestamp
            genesis_block_identifier: BlockIdentifier
            oldest_block_identifier: BlockIdentifier, optional
            sync_status: SyncStatus, optional
            peers: List[Peer]

        See Also
        --------
        select_network: For selecting a current_network.

        Raises
        ------
        RuntimeError: If not current network has been selected.
        """
        if self.current_network is None:
            raise RuntimeError("No `current_network` has been selected. See `select_network` for selecting a current network.")
        return self._network_status(self.current_network, **kwargs)
    
    def network_status(self, blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> NetworkStatusResponse:
        """
        Get the status of a desired network.
        
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
        **kwargs
            Any additional metadata to be passed along to the /network/status. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        NetworkStatusResponse
            current_block_identifier: BlockIdentifier
            current_block_timestamp: Timestamp
            genesis_block_identifier: BlockIdentifier
            oldest_block_identifier: BlockIdentifier, optional
            sync_status: SyncStatus, optional
            peers: List[Peer]
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        return self._network_status(network_id, **kwargs)

    def _network_supported_options(self, network_id : NetworkIdentifier, **kwargs) -> NetworkOptionsResponse:
        """
        Private method for `network_status` to proivde an interface that
        supports calls with existing objects.
        """
        return net.supported_options(self.url, network_id, self.session, **kwargs)
    
    def current_network_supported_options(self, **kwargs) -> NetworkOptionsResponse:
        """
        Get the supported options of the current network.

        Parameters
        ----------
        **kwargs
            Any additional metadata to be passed along to the /network/options. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        --------
        NetworkOptionsResponse
            version: Version
            allow: Allow

        See Also
        --------
        select_network: For selecting a current_network.

        Raises
        ------
        RuntimeError: If not current network has been selected.
        """
        if self.current_network is None:
            raise RuntimeError("No `current_network` has been selected. See `select_network` for selecting a current network.")
        return self._network_supported_options(self.current_network, **kwargs)

    
    def network_supported_options(self, blockchain : str, network : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> NetworkOptionsResponse:
        """
        Get the supported options of a desired network.
        
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
        **kwargs
            Any additional metadata to be passed along to the /network/options. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        NetworkOptionsResponse
            version: Version
            allow: Allow
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        return self._network_supported_options(network_id, **kwargs)

    def _balance(self, network_id : NetworkIdentifier, account_id : AccountIdentifier,
                 block_id : Optional[PartialBlockIdentifier] = None, currencies : Optional[List[Currency]] = None) -> AccountBalanceResponse:
        """
        Private method for the account balance method to proivde an interface that
        supports calls with existing objects.
        """
        return acnt.balance(self.url, self.current_network, account_id, block_id, currencies, self.session)
    
    def current_network_balance_of_account(self, account_address : str, account_metadata : Optional[Dict[str, Any]] = None, 
                                           subaccount_address : Optional[str] = None, subaccount_metadata : Optional[Dict[str, Any]] = None, 
                                           block_height : Optional[int] = None, block_hash : Optional[str] = None, 
                                           selected_currency_symbols : Optional[Union[str, Iterable[str]]] = None, 
                                           selected_currency_decimals : Optional[Union[int, Iterable[int]]] = None,
                                           selected_currency_metadata : Optional[Union[Dict[str, Any], Iterable[Union[Dict[str, Any], None]]]] = None) -> AccountBalanceResponse:
        """
        Get the balance of a specified account on the current network.

        Parameters
        ----------
        account_address: str
            Either a cryptographic key or a username identifying the account.
        account_metadata: dict[str, Any], optional
            Any additional metadata to identify the Account. Any blockchains that utilize a username
            for the address over a public key should specify the public keys here.
        subaccount_address: str, optional
            Either a cryptographic value or another unique identifier for the SubAccount
        subaccount_metadata: dict[str, Any], optional
            Any additional metadata needed to uniquely identify a SubAccount. NOTE: Two
            SubAccounts with the same address but different metadata are considered different
            SubAccounts.
        block_height: int, optional
            The index of the desired block.
        block_hash: str, optional
            The hash of the desired block.
        selected_currency_symbols: str, Iterable[str], optional
            A single str, or an iterable of string of the symbols of the desired currencies to filter
            the results upon. If this is specified, `selected_currency_decimals` must also be specified
            and of equal length.
        selected_currency_decimals: int, Iterable[int], optional
            A single int, or an iterable of ints, representing the number of decimals
            in the atomic unit of the desired currencies to filter the results upon. If this is specified,
            `selected_currency_symbols` must also be specified and of equal length.
        selected_currency_metadata: dict[str, Any], Iterable[Union[dict[str, Any], None]], optional
            A single dict, or an iterable of dicts, representing the metadata of the
            currencies. If this is specified, both `selected_currency_symbols` and `selected_currency_decimals`
            must both also be specified and of equal length.


        Returns
        -------
        AccountBalanceResponse
            block_identifier: BlockIdentifier
            balances: list[Amount]
            metadata: dict[str, Any], optional

        Raises
        ------
        ValueError: With inconsitencies in the currency parameters.
        """
        if account_metadata is None:
            account_metadata = {}
        
        account_id = make_AccountIdentifier(account_address, subaccount_address, subaccount_metadata, **account_metadata)
        try:
            block_id = make_PartialBlockIdentifier(block_height, block_hash)
        except ValueError:
            block_id = None
        
        if selected_currency_symbols is None:
            if not selected_currency_decimals is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_decimals is None:
            if not selected_currency_symbols is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_metadata is not None:
            if selected_currency_symbols is None or selected_currency_decimals is None:
                raise ValueError("If `selected_currency_metadata` is provided, both `selected_curerency_symbols` and `selected_currency_decimals` must be provided")
        The name of the blockchain. Ex: 'bitcoin'
        if selected_currency_decimals is None and selected_currency_symbols is None and selected_currency_metadata is None:
            currencies = None
        else:
            currencies = make_Currencies(selected_currency_symbols, selected_currency_decimals, selected_currency_metadata)

        return self._balance(self.current_network, account_id, block_id, currencies)
    
    def balance_of_account_on_network(self, blockchain : str, network : str, account_address : str,
                                      subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None,
                                      account_metadata : Optional[Dict[str, Any]] = None,
                                      subaccount_address : Optional[str] = None, subaccount_metadata : Optional[Dict[str, Any]] = None,
                                      block_height : Optional[int] = None, block_hash : Optional[str] = None,
                                      selected_currency_symbols : Optional[Union[str, Iterable[str]]] = None,
                                      selected_currency_decimals : Optional[Union[int, Iterable[int]]] = None,
                                      selected_currency_metadata : Optional[Union[Dict[str, Any], Iterable[Union[Dict[str, Any], None]]]] = None) -> AccountBalanceResponse:
        
        """
        Get the balance of a specified account on the specified network.

        Parameters
        ----------
        blockchain: str
            The name of the blockchain. Ex: 'bitcoin'
        network: str
            The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
        account_address: str
            Either a cryptographic key or a username identifying the account.
        subnetwork: str, optional
            The name or identifier of the subnetwork if needed. Ex: 'shard-1'
        subnetwork_metadata: dict[str, Any], optional
            Any additional metadata needed to identify the subnetwork. See the
            individual node implementation to verifiy if additional metadata is needed.
        account_metadata: dict[str, Any], optional
            Any additional metadata to identify the Account. Any blockchains that utilize a username
            for the address over a public key should specify the public keys here.
        subaccount_address: str, optional
            Either a cryptographic value or another unique identifier for the SubAccount
        subaccount_metadata: dict[str, Any], optional
            Any additional metadata needed to uniquely identify a SubAccount. NOTE: Two
            SubAccounts with the same address but different metadata are considered different
            SubAccounts.
        block_height: int, optional
            The index of the desired block.
        block_hash: str, optional
            The hash of the desired block.
        selected_currency_symbols: str, Iterable[str], optional
            A single str, or an iterable of string of the symbols of the desired currencies to filter
            the results upon. If this is specified, `selected_currency_decimals` must also be specified
            and of equal length.
        selected_currency_decimals: int, Iterable[int], optional
            A single int, or an iterable of ints, representing the number of decimals
            in the atomic unit of the desired currencies to filter the results upon. If this is specified,
            `selected_currency_symbols` must also be specified and of equal length.
        selected_currency_metadata: dict[str, Any], Iterable[Union[dict[str, Any], None]], optional
            A single dict, or an iterable of dicts, representing the metadata of the
            currencies. If this is specified, both `selected_currency_symbols` and `selected_currency_decimals`
            must both also be specified and of equal length.

        Returns
        -------
        AccountBalanceResponse
            block_identifier: BlockIdentifier
            balances: list[Amount]
            metadata: dict[str, Any], optional

        Raises
        ------
        ValueError: With inconsitencies in the currency parameters.
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        
        if account_metadata is None:
            account_metadata = {}
        
        account_id = make_AccountIdentifier(account_address, subaccount_address, subaccount_metadata, **account_metadata)
        try:
            block_id = make_PartialBlockIdentifier(block_height, block_hash)
        except ValueError:
            block_id = None
        
        if selected_currency_symbols is None:
            if not selected_currency_decimals is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_decimals is None:
            if not selected_currency_symbols is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_metadata is not None:
            if selected_currency_symbols is None or selected_currency_decimals is None:
                raise ValueError("If `selected_currency_metadata` is provided, both `selected_curerency_symbols` and `selected_currency_decimals` must be provided")
        
        if selected_currency_decimals is None and selected_currency_symbols is None and selected_currency_metadata is None:
            currencies = None
        else:
            currencies = make_Currencies(selected_currency_symbols, selected_currency_decimals, selected_currency_metadata)

        return self._balance(network_id, account_id, block_id, currencies)

    def _unspent_coins(self, network_id : NetworkIdentifier, account_id : AccountIdentifier, include_mempool : Optional[bool] = False, currencies : Optional[List[Currency]] = None) -> AccountCoinsResponse:
        """
        Private method for the account uspent coins method to proivde an interface that
        supports calls with existing objects.
        """
        return acnt.unspent_coins(self.url, network_id, account_id, include_mempool, currencies, self.session)

    def unspent_coins_of_account_on_current_network(self, account_address : str, account_metadata : Optional[Dict[str, Any]] = None, 
                                                    subaccount_address : Optional[str] = None, subaccount_metadata : Optional[Dict[str, Any]] = None, 
                                                    include_mempool : Optional[bool] = False,
                                                    selected_currency_symbols : Optional[Union[str, Iterable[str]]] = None, 
                                                    selected_currency_decimals : Optional[Union[int, Iterable[int]]] = None,
                                                    selected_currency_metadata : Optional[Union[Dict[str, Any], Iterable[Union[Dict[str, Any], None]]]] = None) -> AccountCoinsResponse:
        """
        Get the unspent coins of a specified account on the current network.

        Parameters
        ----------
        account_address: str
            Either a cryptographic key or a username identifying the account.
        account_metadata: dict[str, Any], optional
            Any additional metadata to identify the Account. Any blockchains that utilize a username
            for the address over a public key should specify the public keys here.
        subaccount_address: str, optional
            Either a cryptographic value or another unique identifier for the SubAccount
        subaccount_metadata: dict[str, Any], optional
            Any additional metadata needed to uniquely identify a SubAccount. NOTE: Two
            SubAccounts with the same address but different metadata are considered different
            SubAccounts.
        include_mempool: bool, optional
            Include the state from the mempool when looking up an account's unspent coins. NOTE:
            using this functionality breaks any guarantee of idempotency. Defaults to False.
        selected_currency_symbols: str, Iterable[str], optional
            A single str, or an iterable of string of the symbols of the desired currencies to filter
            the results upon. If this is specified, `selected_currency_decimals` must also be specified
            and of equal length.
        selected_currency_decimals: int, Iterable[int], optional
            A single int, or an iterable of ints, representing the number of decimals
            in the atomic unit of the desired currencies to filter the results upon. If this is specified,
            `selected_currency_symbols` must also be specified and of equal length.
        selected_currency_metadata: dict[str, Any], Iterable[Union[dict[str, Any], None]], optional
            A single dict, or an iterable of dicts, representing the metadata of the
            currencies. If this is specified, both `selected_currency_symbols` and `selected_currency_decimals`
            must both also be specified and of equal length.

        Returns
        -------
        AccountCoinsResponse
            account_identifer: AccountIdentifier
            coins: list[Coin]
            metadata: dict[str, Any], optional
        
        Raises
        ------
        ValueError: With inconsitencies in the currency parameters.
        """
        if account_metadata is None:
            account_metadata = {}
        
        account_id = make_AccountIdentifier(account_address, subaccount_address, subaccount_metadata, **account_metadata)
        try:
            block_id = make_PartialBlockIdentifier(block_height, block_hash)
        except ValueError:
            block_id = None
        
        if selected_currency_symbols is None:
            if not selected_currency_decimals is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_decimals is None:
            if not selected_currency_symbols is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_metadata is not None:
            if selected_currency_symbols is None or selected_currency_decimals is None:
                raise ValueError("If `selected_currency_metadata` is provided, both `selected_curerency_symbols` and `selected_currency_decimals` must be provided")
        The name of the blockchain. Ex: 'bitcoin'
        if selected_currency_decimals is None and selected_currency_symbols is None and selected_currency_metadata is None:
            currencies = None
        else:
            currencies = make_Currencies(selected_currency_symbols, selected_currency_decimals, selected_currency_metadata)

        return self._unspent_coins(self.current_network, account_id, include_mempool, currencies)

    def unspent_coins_of_account_on_network(self, blockchain : str, network : str, account_address : str,
                                            subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None,
                                            account_metadata : Optional[Dict[str, Any]] = None,
                                            subaccount_address : Optional[str] = None, subaccount_metadata : Optional[Dict[str, Any]] = None,
                                            include_mempool : Optional[bool] = False,
                                            selected_currency_symbols : Optional[Union[str, Iterable[str]]] = None,
                                            selected_currency_decimals : Optional[Union[int, Iterable[int]]] = None,
                                            selected_currency_metadata : Optional[Union[Dict[str, Any], Iterable[Union[Dict[str, Any], None]]]] = None) -> AccountBalanceResponse:
        """
        Get the unspent coins of a specified account on the specified network.

        Parameters
        ----------
        blockchain: str
            The name of the blockchain. Ex: 'bitcoin'
        network: str
            The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
        account_address: str
            Either a cryptographic key or a username identifying the account.
        subnetwork: str, optional
            The name or identifier of the subnetwork if needed. Ex: 'shard-1'
        subnetwork_metadata: dict[str, Any], optional
            Any additional metadata needed to identify the subnetwork. See the
            individual node implementation to verifiy if additional metadata is needed.
        account_metadata: dict[str, Any], optional
            Any additional metadata to identify the Account. Any blockchains that utilize a username
            for the address over a public key should specify the public keys here.
        subaccount_address: str, optional
            Either a cryptographic value or another unique identifier for the SubAccount
        subaccount_metadata: dict[str, Any], optional
            Any additional metadata needed to uniquely identify a SubAccount. NOTE: Two
            SubAccounts with the same address but different metadata are considered different
            SubAccounts.
        include_mempool: bool, optional
            Include the state from the mempool when looking up an account's unspent coins. NOTE:
            using this functionality breaks any guarantee of idempotency. Defaults to False.
        selected_currency_symbols: str, Iterable[str], optional
            A single str, or an iterable of string of the symbols of the desired currencies to filter
            the results upon. If this is specified, `selected_currency_decimals` must also be specified
            and of equal length.
        selected_currency_decimals: int, Iterable[int], optional
            A single int, or an iterable of ints, representing the number of decimals
            in the atomic unit of the desired currencies to filter the results upon. If this is specified,
            `selected_currency_symbols` must also be specified and of equal length.
        selected_currency_metadata: dict[str, Any], Iterable[Union[dict[str, Any], None]], optional
            A single dict, or an iterable of dicts, representing the metadata of the
            currencies. If this is specified, both `selected_currency_symbols` and `selected_currency_decimals`
            must both also be specified and of equal length.

        Returns
        -------
        AccountCoinsResponse
            account_identifer: AccountIdentifier
            coins: list[Coin]
            metadata: dict[str, Any], optional

        Raises
        ------
        ValueError: With inconsitencies in the currency parameters.
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        
        if account_metadata is None:
            account_metadata = {}
        
        account_id = make_AccountIdentifier(account_address, subaccount_address, subaccount_metadata, **account_metadata)
        
        if selected_currency_symbols is None:
            if not selected_currency_decimals is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_decimals is None:
            if not selected_currency_symbols is None:
                raise ValueError("Both `selected_curerency_symbols` and `selected_currency_decimals` must be provided if either is.")
        if selected_currency_metadata is not None:
            if selected_currency_symbols is None or selected_currency_decimals is None:
                raise ValueError("If `selected_currency_metadata` is provided, both `selected_curerency_symbols` and `selected_currency_decimals` must be provided")
        
        if selected_currency_decimals is None and selected_currency_symbols is None and selected_currency_metadata is None:
            currencies = None
        else:
            currencies = make_Currencies(selected_currency_symbols, selected_currency_decimals, selected_currency_metadata)

        return self._unspent_coins(network_id, account_id, include_mempool, currencies)

    def _block(self, network_id : NetworkIdentifier, block_id : PartialBlockIdentifier) -> BlockResponse:
        """
        Private method for the get block method to proivde an interface that
        supports calls with existing objects.
        """
        return blk.block(self.url, network_id, block_id, self.session)

    def block_on_current_network(self, block_height : Optional[int] = None, block_hash : Optional[str] = None) -> BlockResponse:
        """
        Get a block on the current network by either block height, or its hash.

        NOTE: At least the `block_height` or `block_hash` needs to be specified.

        Parameters
        ----------
        block_height: int, optional
            The index of the block
        block_hash: str, optional
            The hash of the block.

        Returns
        -------
        BlockResponse
            block: Block
            other_transactions: list[TransactionIdentifier], optional
        
        Raises
        ------
        ValueError: if neither `block_height` or `block_hash` are specified.
        """
        try:
            block_id = make_PartialBlockIdentifier(block_height, block_hash)
        except ValueError:
            raise ValueError("Either the `block_height` or the `block_hash` must be specified.")
        return self._block(self.current_network, block_id)

    def block_on_network(self, blockchain : str, network : str, 
                         block_height : Optional[int] = None, block_hash : Optional[str] = None,
                         subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None) -> BlockResponse:
        
        """
        Get a block on the specified network by either block height, or its hash.

        NOTE: At least the `block_height` or `block_hash` needs to be specified.

        Parameters
        ----------
        blockchain: str
            The name of the blockchain. Ex: 'bitcoin'
        network: str
            The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
        block_height: int, optional
            The index of the block
        block_hash: str, optional
            The hash of the block.
        subnetwork: str, optional
            The name or identifier of the subnetwork if needed. Ex: 'shard-1'
        subnetwork_metadata: dict[str, Any], optional
            Any additional metadata needed to identify the subnetwork. See the
            individual node implementation to verifiy if additional metadata is needed.

        Returns
        -------
        BlockResponse
            block: Block
            other_transactions: list[TransactionIdentifier], optional
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        try:
            block_id = make_PartialBlockIdentifier(block_height, block_hash)
        except ValueError:
            raise ValueError("Either the `block_height` or the `block_hash` must be specified.")
        return self._block(network_id, block_id)

    def _block_transaction(self, network_id : NetworkIdentifier, block_id : BlockIdentifier, transaction_id : TransactionIdentifier) -> BlockTransactionResponse:
        """
        Private method for the get block transaction method to proivde an interface that
        supports calls with existing objects.
        """
        return blk.transaction(self.url, network_id, block_id, transaction_id, self.session)

    def block_transaction_on_current_network(self, block_height : int, block_hash : str, transaction_hash : str) -> Transaction:
        """
        Get the specified transaciton on the given block for the current network.

        Parameters
        ----------
        block_height: int
            The index of the block.
        block_hash: str
            The hash of the block.
        transaction_hash: str
            The hash of the transaction.

        Returns
        -------
        Transaction
            transaction_identifier: TransactionIdentifier
            operations: list[Operation]
            related_transactions: list[RelatedTransaction], optional
            metadata: dict[str, Any], optional
        """
        block_id = BlockIdentifier(index=block_height, hash=block_hash)
        transaction_id = TransactionIdentifier(hash=transaction_hash)
        return self._block_transaction(self.current_network, block_id, transaction_id)


    def block_transaction_on_network(self, blockchain : str, network : str, 
                                     block_height: int, block_hash : str, transaction_hash : str,
                                     subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None) -> Transaction:
        """
        Get the specified transaction on the given block for the specified network.

        Parameters
        ----------
        blockchain: str
            The name of the blockchain. Ex: 'bitcoin'
        network: str
            The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
        block_height: int
            The index of the block.
        block_hash: str
            The hash of the block.
        transaction_hash: str
            The hash of the transaction.
        subnetwork: str, optional
            The name or identifier of the subnetwork if needed. Ex: 'shard-1'
        subnetwork_metadata: dict[str, Any], optional
            Any additional metadata needed to identify the subnetwork. See the
            individual node implementation to verifiy if additional metadata is needed.
        
        Returns
        -------
        Transaction
            transaction_identifier: TransactionIdentifier
            operations: list[Operation]
            related_transactions: list[RelatedTransaction], optional
            metadata: dict[str, Any], optional
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        block_id = BlockIdentifier(index=block_height, hash=block_hash)
        transaction_id = TransactionIdentifier(hash=transaction_hash)
        return self._block_transaction(network_id, block_id, transaction_id)

    def _all_mempool_transactions(self, network_id : NetworkIdentifier, **kwargs) -> List[TransactionIdentifier]:
        """
        Private method for the get all mempool transaction method to proivde an interface that
        supports calls with existing objects.
        """
        return memp.all_transactions(self.url, network_id, self.session, **kwargs)

    def all_mempool_transactions_on_current_network(self, **kwargs) -> List[TransactionIdentifier]:
        """
        Get all the transactions in the mempool of the current network.

        Parameters
        ----------
        **kwargs
            Any additional metadata to be passed along to the /mempool request. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        list[TransactionIdentifier]
        """
        return self._all_mempool_transactions(self.current_network, **kwargs)

    def all_mempool_transactions_on_network(self, blockchain : str, network : str, subnetwork : 
                                        Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None, 
                                        **kwargs) -> List[TransactionIdentifier]:
        """
        Get all the transactions in the mempool of the specified network.

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
        **kwargs
            Any additional metadata to be passed along to the /mempool request. 
            See the individual node implementation to verify if additional
            metadata is needed.
        """
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        return self._all_mempool_transactions(network_id, **kwargs)


    def _mempool_transaction(self, network_id : NetworkIdentifier, transaction_id : TransactionIdentifier) -> MempoolTransactionResponse:
        """
        Private method for the get transaction from mempool method to proivde an interface that
        supports calls with existing objects.
        """
        return memp.transaction(self.url, network_id, transaction_id, self.session)

    def mempool_transaction_on_current_network(self, transaction_hash : str) -> MempoolTransactionResponse:
        """
        Get the specified transaction from the mempool of the current network.

        Parameters
        ----------
        transaction_hash: str
            The hash of the transaction.

        Returns
        -------
        MempoolTransactionResponse
            transaction_identifier: TransactionIdentifier
            metadata: dict[str, Any], optional
        """
        transaction_id = TransactionIdentifier(hash=transaction_hash)
        return self._mempool_transaction(self.current_network, transaction_id)


    def mempool_transaction_on_network(self, blockchain : str, network : str, transaction_hash : str,
                                       subnetwork : Optional[str] = None, 
                                       subnetwork_metadata : Optional[Dict[str, Any]] = None) -> MempoolTransactionResponse:
        """
        Get the specified transaction from the mempool on the specified network.

        Parameters
        ----------
        blockchain: str
            The name of the blockchain. Ex: 'bitcoin'
        network: str
            The chain-id or network identifier. Ex: 'mainnet' or 'testnet'
        transaction_hash: str
            The hash of the transaction
        subnetwork: str, optional
            The name or identifier of the subnetwork if needed. Ex: 'shard-1'
        subnetwork_metadata: dict[str, Any], optional
            Any additional metadata needed to identify the subnetwork. See the
            individual node implementation to verifiy if additional metadata is needed.
        
        Returns
        -------
        MempoolTransactionResponse
            transaction_identifier: TransactionIdentifier
            metadata: dict[str, Any], optional
        """
        network_id = NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        transaction_id = TransactionIdentifier(hash=transaction_hash)
        return self._mempool_transaction(network_id, transaction_id)


    def _combine(self, network_id : NetworkIdentifier, unsigned_transaction : str, signatures : List[Signature]) -> str:
        """
        Private method for the construction combine method.
        """
        return cst.combine(self.url, network_id, unsigned_transaction, signatures, self.session)

    def _derive(self, network_id : NetworkIdentifier, public_key : PublicKey, **kwargs) -> ConstructionDeriveResponse:
        """
        Private method for the derive method
        """
        return cst.derive(self.url, network_id, public_key, self.session, **kwargs)

    def _signed_transaction_hash(self, network_id : NetworkIdentifier, signed_transaction : str) -> TransactionIdentifierResponse:
        """
        Private method for the hash method.
        """
        return cst.signed_transaction_hash(self.url, network_id, signed_transaction)

    def _metadata(self, network_id : NetworkIdentifier, options : Optional[Dict[str, Any]] = None, public_keys : Optional[List[PublicKey]] = None) -> ConstructionMetadataResponse:
        """
        Private method for metadata method.
        """
        return cst.metadata(self.url, network_id, options, public_keys, self.session)

    def _parse(self, network_id : NetworkIdentifier, signed : bool, transaction : str) -> ConstructionParseResponse:
        """
        Private method for the parse method.
        """
        return cst.parse(self.url, network_id, signed, transaction, self.session)

    def _payloads(self, network_id : NetworkIdentifier, metadata : Optional[Dict[str, Any]] = None, public_keys : Optional[List[PublicKey]] = None) -> ConstructionPayloadsResponse:
        """
        Private method for the payloads method.
        """
        return cst.payloads(self.url, network_id, metadata, public_keys, self.session)

    def _preprocess(self, network_id : NetworkIdentifier, operations : List[Operation], metadata : Optional[Dict[str, Any]] = None, max_fee : Optional[List[Amount]] = None, suggested_fee_multiplier : Optional[float] = None) -> ConstructionPreprocessResponse:
        """
        Private method for the preprocess method.
        """
        return cst.preprocess(self.url, network_id, operations, metadata, max_fee, suggested_fee_multiplier, self.session)

    def preprocess_operations_on_current_network(self, metadata : Optional[Dict[str, Any]] = None, max_fee : Optional[List[Amount]] = None, suggested_fee_multiplier : Optional[float] = None) -> ConstructionPreprocessResponse:
        return None
    
    def _submit(self, network_id : NetworkIdentifier, signed_transaction : str) -> TransactionIdentifierResponse:
        """
        Private method for the submit method
        """
        return cst.submit(self.url, network_id, signed_transaction, self.session)

    def submit_signed_transaction_on_current_network(self, signed_transaction : str) -> TransactionIdentifierResponse:
        """
        Submit a signed transaction onto the current network.

        Parameters
        ----------
        signed_transaction: str

        Returns
        -------
        TransactionIdentifierResponse
            transaction_identifier: TransactionIdentifer
            metadata: dict[str, Any], optional
        """
        return self._submit(self.current_network, signed_transaction)
    
    def submit_signed_transaction_on_network(self, blockchain : str, network : str, signed_transaction : str, subnetwork : Optional[str] = None, subnetwork_metadata : Optional[Dict[str, Any]] = None) -> TransactionIdentifierResponse:
        network_id = make_NetworkIdentifier(blockchain, network, subnetwork, subnetwork_metadata)
        return self._submit(network_id, signed_transaction)
    
    def _events_blocks(self, network_id : NetworkIdentifier, offset : Optional[int] = None, limit : Optional[int] = None) -> EventsBlocksResponse:
        """
        Private method for the events blocks method.
        """
        return evnt.blocks(self.url, network_id, offset, limit, self.session)

    def _search_transactions(self, network_id : NetworkIdentifier, operator : Optional[Operator] = "and", max_block : Optional[int] = None, offset : Optional[int] = None, transaciton_id : Optional[TransactionIdentifier] = None, account_id : Optional[AccountIdentifier] = None, coin_id : Optional[CoinIdentifer] = None, currency : Optional[Currency] = None, status : Optional[str] = None, type_ : Optional[str] = None, address : Optional[str] = None, success : Optional[bool] = None) -> SearchTransactionsResponse:
        """
        Private method for the search transactions method.
        """
        return srch.transacitons(self, network_id, operator, max_block, offset, limit, transaciton_id, account_id, currency, status, type_, address, success, self.session)


class RosettaAPIExt(RosettaAPI):
    """
    This API object will include some generalized helper methods, that can't be guarenteed to
    work for all Rosetta implementations, but in the general case, might provide to be helpful
    in most cases.
    """

    def discover_networks(self, network_metadata : Optional[Dict[str, Any]] = None, **kwargs) -> List[net.NetworkOverview]:
        """
        Discover available networks and get the supported options and status for each.

        Parameters
        ----------
        network_metadata: dict[str, Any], optional:
            Any additional metadata to be passed along to the /network/options
            and /network/status routes. See the individual node implementation
            to verify if additional metadata is needed.
        **kwargs
            Any additional metadata to be passed along to the /network/list request. 
            See the individual node implementation to verify if additional
            metadata is needed.

        Returns
        -------
        list[NetworkOverview]
            network: NetworkIdentifier
            options: NetworkOptionsResponse
            status: NetworkStatusRespone

        Fails When
        -----------
        The /network/options and /network/status endpoints need additional, but 
        different metadata. 
        """
        return net.discover(self.url, self.session, network_metadata, **kwargs)
