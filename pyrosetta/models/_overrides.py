from textwrap import indent

from ._models import *

def str_SubNetworkIdentifier(self : SubNetworkIdentifier) -> str:
    sn = "Subnetwork: {}".format(self.network)
    if self.metadata:
        md_h = "Additional Metadata:"
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        return "\n".join(sn, md_h, indent(md, 2))
    return sn

SubNetworkIdentifier.__str__ = str_SubNetworkIdentifier

def str_NetworkIdentifier(self : NetworkIdentifier) -> str:
    bc = "Blockchain: {}".format(self.blockchain)
    nw = "Network: {}".format(self.network)
    if self.sub_network_identifier:
        return "\n".join(bc, nw, str(self.sub_network_identifier))
    return "\n".join(bc, nw)

NetworkIdentifier.__str__ = str_NetworkIdentifier

def str_OperationStatus(self : OperationStatus) -> str:
    status = "Status: {}".format(self.status)
    successful = "Operation.Amount affects Operation.Account: {}".format(self.successful)
    return "\n".join(status, successful)

OperationStatus.__str__ = str_OperationStatus

def str_Error(self : Error) -> str:
    out = ["Error {}: {}".format(self.code, self.message)]
    if self.description is not None:
        out.append("Description: {}".format(self.description))
    out.append("Retriable: {}".format(self.retriable))
    if self.details:
        out.append("Details:")
        dets = "\n".join(["- {}: {}".format(key, val) for key, val in self.details.items()])
        out.append(indent(dets, 2))
    return "\n".join(*out)

Error.__str__ = str_Error

def str_Currency(self : Currency) -> str:
    sym = "Symbol: {}".format(self.symbol)
    decimals = "Decimals of standard unit: {}".format(self.decimals)
    if self.metadata:
        md_h = "Additional Metadata:"
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        return "\n".join(sym, decimals, md_h, indent(md, 2))
    return "\n".join(sym, decimals)

Currency.__str__ = str_Currency


def str_BalanceExemption(self : BalanceExemption) -> str:
    out = []
    if self.sub_account_address is not None:
        out.append("SubAccount Address: {}".format(self.sub_account_address))
    if self.currency is not None:
        out.append("Currency: {}".format(str(self.currency)))
    if self.exemption_type is not None:
        out.append("Exemption Type: {}".format(self.exemption_type))

BalanceExemption.__str__ = str_BalanceExemption

def str_Allow(self : Allow) -> str:
    out = []
    out.append("Suppported Operation Statuses:")
    stats = "\n".join(["- {}".format(status) for status in self.operation_statuses])
    out.append(indent(stats, 2))
    out.append("Supported Operation Types:")
    ts = "\n".join(["- {}".format(t) for t in self.operation_types])
    out.append(indent(ts, 2))
    out.append("Possible Errors:")
    es = "\n".join(["- {}".format(str(e)) for e in self.errors])
    out.append(indent(es, 2))
    out.append("Historical Balance Lookup Supported: {}".format(self.historical_balance_lookup))
    if self.timestamp_start_index is not None:
        out.append("First valid block timestamp: {}".format(self.timestamp_start_index))
    out.append("Supported /call Methods:")
    ms = "\n".join(["- {}".format(m) for m in self.call_methods])
    out.append(indent(ms, 2))
    out.append("Account balances that can change without a corresponding Operation:")
    bes = "\n".join(["- {}".format(be) for be in self.balance_exemptions])
    out.append(indent(bes, 2))
    out.append("Uspent coins can be updated based on mempool contents: {}".format(self.mempool_coins))
    return "\n".join(*out)

Allow.__str__ = str_Allow

def str_Version(self : Version) -> str:
    out = ['Rosetta Version: {}'.format(self.rosetta_version)]
    out.append('Node Version: {}'.format(self.node_version))
    if self.middleware_version is not None:
        out.append('Middleware Version: {}'.format(self.middleware_version))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

Version.__str__ = str_Version

def str_BlockIdentifier(self : BlockIdentifier) -> str:
    return "Block Height: {}\nHash: {}".format(self.index, self.hash)

BlockIdentifier.__str__ = str_BlockIdentifier

def str_SyncStatus(self : SyncStatus) -> str:
    out = []
    if self.current_index is not None:
        out.append("Index of last synced block in current stage: {}".format(self.current_index))
    if self.target_index is not None:
        out.append("Index of target block to sync to in current stage".format(self.target_index))
    if self.stage is not None:
        out.append("Stage of sync process: {}".format(self.stage))
    if self.synced is not None:
        out.append("Synced up to most recent block: {}".format(self.synced))
    return "\n".join(out)

SyncStatus.__str__ = str_SyncStatus

def str_Peer(self : Peer) -> str:
    i = "id: {}".format(self.peer_id)
    if self.metadata:
        md_h = "Additional Metadata:"
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        return "\n".join(i, md_h, indent(md, 2))
    return i

Peer.__str__ = str_Peer
        
def str_NetworkOptionsResponse(self : NetworkOptionsResponse) -> str:
    v = "Version Info:\n{}\n".format(indent(str(self.version), 2))
    d = "Implementation Details:\n{}".format(indent(str(self.details), 2))
    return "\n".join(v, d)

NetworkOptionsResponse.__str__ = str_NetworkOptionsResponse

def str_NetworkStatusResponse(self : NetworkStatusResponse) -> str:
    out = ["Current Block:"]
    out.append(indent(str(self.current_block_identifier), 2))
    out.append("Current Block Timestamp: {}".format(self.current_block_timestamp))
    out.append("Genesis Block:")
    out.append(indent(str(self.genesis_block_identifier), 2))
    if self.oldest_block_identifier is not None:
        out.append("Oldest Block:")
        out.append(indent(str(self.oldest_block_identifier), 2))
    if self.sync_status is not None:
        out.append("Sync Status:")
        out.append(indent(str(self.sync_status), 2))
    out.append("Peers:")
    pl = "\n".join(["- {}".format(p) for p in self.peers])
    out.append(indent(pl, 2))
    return "\n".join(*out)

NetworkStatusResponse.__str__ = str_NetworkStatusResponse

def str_Amount(self : Amount) -> str:
    amt = '{} atomic units of {} (*B**{})'.format(self.value, self.currency.symbol, self.currency.decimals)
    if self.metadata:
        md_h = "Additional Metadata:"
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        return "\n".join(amt, indent(md_h, 2), indent(md, 4))
    return amt

Amount.__str__ = str_Amount

def str_AccountBalanceResponse(self : AccountBalanceResponse) -> str:
    out = ["Block:"]
    out.append(ident(str(self.block_identifier), 2))
    out.append("Balances:")
    for balance in self.balances:
        out.append(indent("- {}".format(str(balance), 2)))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

AccountBalanceResponse.__str__ = str_AccountBalanceResponse

def str_Coin(self : Coin) -> str:
    return "Balance of {} on coin_id: {}".format(self.amount, self.coin_identifier.identifier)

Coin.__str__ = str_Coin

def str_AccountCoinsResponse(self : AccountCoinsResponse) -> str:
    out = ["Block:"]
    out.append(ident(str(self.block_identifier), 2))
    out.append("Coins:")
    for coin in self.coins:
        out.append(indent("- {}".format(str(coin), 2)))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

AccountCoinsResponse.__str__ = str_AccountCoinsResponse

def str_OperationIdentifier(self : OperationIdentifier) -> str:
    idx = "Index: {}".format(self.index)
    if self.network_index is not None:
        net_idx = "Network Index: {}".format(self.network_index)
        return "\n".join(idx, net_idx)
    return idx

OperationIdentifier.__str__ = str_OperationIdentifier

def str_CoinChange(self : CoinChange) -> str:
    return "{} with coin id: {}".format(self.coin_action, self.coin_identifier.identifier)

CoinChange.__str__ = str_CoinChange

def str_Operation(self : Operation) -> str:
    out = ["Operation:"]
    out.append(indent(str(self.operation_identifier), 2))
    if related_operations is not None:
        out.append("Related Operations:")
        for related in self.related_operations:
            out.append(indent(str(related), 2))
    
    out.append("type: {}".format(self.type)) 
    if self.status is not None:
        out.append("Status: {}".format(self.status))
    if self.account is not None:
        out.append("Account:")
        out.append(indent(str(self.account), 2))
    if self.amount is not None:
        out.append("Amount:")
        out.append(indent(str(self.amount), 2))
    if self.coin_change is not None:
        out.append("Coin Change: {}".format(self.coin_change))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

Operation.__str__ = str_Operation

def str_RelatedTransaction(self : RelatedTransaction) -> str:
    out = []
    if self.network_identifier is not None:
        out.append("Network:")
        out.append(indent(str(self.network_identifier), 2))
    out.append("Transaction: {}".format(self.transaction_identifier.hash))
    out.append("Direction: {}".format(self.direction))
    return "\n".join(*out)

RelatedTransaction.__str__ = str_RelatedTransaction

def str_Transaction(self : Transaction) -> str:
    out = ["Transaction id: {}".format(self.transaction_identifier.hash)]
    out.append("Operations:")
    for operation in self.operations:
        op = "- {}".format(operation)
        out.append(indent(op, 2))
    if self.related_transactions is not None:
        out.append("Related Transactions:")
        for related in self.related_transactions:
            rt = "- {}".format(related)
            out.append(indent(rt, 2))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

Transaction.__str__ = str_Transaction

def str_Block(self : Block) -> str:
    out = ["Block:"]
    out.append(indent(str(self.block_identifier), 2))
    out.append("Parent Block:")
    out.append(indent(str(self.parent_block_identifier), 2))
    out.append("Timestamp: {}".format(self.timestamp))
    out.append("Transactions:")
    for tran in self.transactions:
        t = "- {}".format(tran)
        out.append(indent(t, 2))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

Block.__str__ = str_Block

def str_BlockResponse(self : BlockResponse) -> str:
    out = []
    if self.block is not None:
        out.append("Block")
        out.append(indent(str(self.block), 2))
    if self.other_transactions is not None:
        out.append("Other Transactions:")
        for tid in self.other_transactions:
            ot = "- {}".format(tid.hash)
            out.append(indent(ot, 2))
    if out:
        return "\n".join(*out)
    return ""

BlockResponse.__str__ = str_BlockResponse

def str_MempoolTransactionResponse(self : MempoolTransactionResponse) -> str:
    out = ["Transaction:"]
    out.append(indent(str(self.transaction), 2))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

MempoolTransactionResponse.__str__ = str_MempoolTransactionResponse

def str_ConstructionDeriveResponse(self : ConstructionDeriveResponse) -> str:
    out = []
    if self.address is not None:
        out.append("Address: {}".format(self.address))
    if self.account_identifier is not None:
        out.append("Account:")
        out.append(indent(str(self.account_identifier), 2))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

ConstructionDeriveResponse.__str__ = str_ConstructionDeriveResponse

def str_TransactionIdentifierResponse(self : TransactionIdentifierResponse) -> str:
    out = ["Transaction: {}".format(self.transaction_identifier.hash)]
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

TransactionIdentifierResponse.__str__ = str_TransactionIdentifierResponse

def str_ConstructionMetadataResponse(self : ConstructionMetadataResponse) -> str:
    out = ["Metadata:"]
    md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
    out.append(indent(md, 2))
    if self.suggested_fee is not None:
        out.append("Suggested Fee(s):")
        fees = "\n".join(["- {}".format(str(amt)) for amt in self.suggested_fee])
        out.append(indent(fees, 2))
    return "\n".join(*out)

ConstructionMetadataResponse.__str__ = str_ConstructionMetadataResponse

def str_ConstructionParseResponse(self : ConstructionParseResponse) -> str:
    out = ["Operations:"]
    ops = "\n".join(["- {}".format(str(op)) for op in self.operations])
    out.append(indent(ops, 2))
    if self.signers is not None:
        out.append("Signers:")
        sigs = "\n".join(["- {}".format(sig) for sig in self.signers])
        out.append(indent(sigs, 2))
    if self.account_identifier_signers is not None:
        out.append("Signers:")
        sigs = "\n".join(["- {}".format(sig) for sig in self.account_identifier_signers])
        out.append(indent(sigs, 2))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

ConstructionParseResponse.__str__ = str_ConstructionParseResponse

def str_SigningPayload(self : SigningPayload) -> str:
    out = []
    if self.address is not None:
        out.append("Address: {}".format(self.address))
    if self.account_identifier is not None:
        out.append("Account:")
        out.append(indent(str(self.account_identifier), 2))
    out.append("Hex Bytes: {}".format(self.hex_bytes))
    if self.signature_type is not None:
        out.append("Signature Type: {}".format(self.signature_type))
    return "\n".join(*out)

SigningPayload.__str__ = str_SigningPayload

def str_ConstructionPayloadsResposne(self : ConstructionPayloadsResponse) -> str:
    out = ["Unsigned Transaction: {}".format(self.unsigned_transaction)]
    out.append("Payloads:")
    ps = "\n".join(["- {}".format(str(payload)) for payload in self.payloads])
    out.append(indent(ps, 2))
    return "\n".join(*put)

ConstructionPayloadsResponse.__str__ = str_ConstructionPayloadsResposne

def str_ConstructionPreprocessResponse(self : ConstructionPreprocessResponse) -> str:
    out = []
    if self.options is not None:
        out.append("Options:")
        opts = "\n".join(["- {}: {}".format(key, val) for key, val in self.options.items()])
        out.append(indent(str(opts), 2))
    if self.required_public_keys is not None:
        out.append("Required Public Keys:")
        pub_keys = "\n".join(["- {}".format(str(act)) for act in self.required_public_keys])
    if out:
        return "\n".join(*out)
    return ""

ConstructionPreprocessResponse.__str__ = str_ConstructionPreprocessResponse

def str_BlockEvent(self : BlockEvent) -> str:
    out = ["Sequence: {}".format(self.sequence)]
    out.append("Block:")
    out.append(indent(str(self.block_identifier), 2))
    out.append("Type: {}".format(self.type))
    return "\n".join(*out)

BlockEvent.__str__ = str_BlockEvent

def str_EventsBlocksResponse(self : EventsBlocksResponse) -> str:
    out = ["Max Sequence: {}".format(self.max_sequence)]
    bes = "\n".join(["- {}".format(event) for event in self.events])
    out.append(indent(bes, 2))
    return "\n".join(*out)

EventsBlocksResponse.__str__ = str_EventsBlocksResponse

def str_BlockTransaction(self : BlockTransaction) -> str:
    out = ["Block:"]
    out.append(indent(str(self.block_identifier), 2))
    out.append("Transaction:")
    out.append(indent(str(self.transaction), 2))
    return "\n".join(*out)

BlockTransaction.__str__ = str_BlockTransaction

def str_SearchTransactionsResponse(self : SearchTransactionsResponse) -> str:
    out = ["Transactions:"]
    txs = "\n".join(["- {}".format(str(tx)) for tx in self.transactions])
    out.append(indent(txs, 2))
    out.append("Total Count: {}".format(self.total_count))
    if self.next_offset is not None:
        out.append("Next Offset: {}".format(self.next_offset))
    return "\n".join(*out)

SearchTransactionsResponse.__str__ = str_SearchTransactionsResponse
