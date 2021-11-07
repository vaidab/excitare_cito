import time

from web3 import Web3

import package.network_chains as chains
from package import units
from package.utils import timeit


def connect(network):
    network_data = chains.get_network_data(network)
    network_rpc = chains.get_rpc(network_data)
    web3 = Web3(Web3.HTTPProvider(network_rpc))

    if not web3.isConnected():
        raise Exception(f"[?] Not connected to {chains.get_name(network_data)}")
    else:
        print(f"[+] Connected to {chains.get_name(network_data)}")

    return web3


@timeit
def wait_for_token(web3, wallet_address, token_address, token_abi, sleep_time_seconds, max_decimals):
    token_address = web3.toChecksumAddress(token_address)
    token_contract = web3.eth.contract(token_address, abi=token_abi)
    token_symbol = token_contract.functions.symbol().call()
    token_decimals = token_contract.functions.decimals().call()
    token_units = units.get_unit(token_decimals)

    token_initial_balance_full = token_contract.functions.balanceOf(wallet_address).call()
    token_initial_balance = web3.fromWei(token_initial_balance_full, token_units)

    print(f"[+] Current {token_symbol} balance: {round(token_initial_balance, max_decimals)} ")
    print(f"[+] Watching {wallet_address} for token {token_address} ({token_symbol}) every {sleep_time_seconds}s")

    new_balance_full = token_initial_balance_full
    while new_balance_full <= token_initial_balance_full:
        time.sleep(sleep_time_seconds)
        new_balance_full = token_contract.functions.balanceOf(wallet_address).call()

    final_balance_full = new_balance_full - token_initial_balance_full
    final_balance = web3.fromWei(final_balance_full, token_units)

    print(f"[+] {round(final_balance, max_decimals)} {token_symbol} arrived in the account.")
    print(f"[!] New {token_symbol} balance: {round(web3.fromWei(new_balance_full, token_units), max_decimals)} ")
    return
