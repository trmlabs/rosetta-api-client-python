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
        out.append(indent("- {}".format(str(balance), 1))
    if self.metadata:
        out.append("Additional Metadata:")
        md = "\n".join(["- {}: {}".format(key, val) for key, val in self.metadata.items()])
        out.append(indent(md, 2))
    return "\n".join(*out)

AccountBalanceResponse.__str__ = str_AccountBalanceResponse

def str_Coin(self : Coin) -> str:
    return "Balance of {} on coin_id: {}".format(self.amount, self.coin_identifier.identifier)

Coin.__str__ = str_Coin