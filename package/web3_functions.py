import os
import time

from web3 import Web3
import package.network_chains as chains

def connect(network):
    network_data = chains.get_network_data(network)
    network_rpc = chains.get_rpc(network_data)
    web3 = Web3(Web3.HTTPProvider(network_rpc))

    if not web3.isConnected():
        raise Exception(f"[?] Not connected to {chains.get_name(network_data)}")
    else:
        print(f"[+] Connected to {chains.get_name(network_data)}")

    return web3


def wait_for_token(web3, wallet_address, token_address, token_abi, sleep_time_seconds, max_decimals):
    token_address = web3.toChecksumAddress(token_address)
    token_contract = web3.eth.contract(token_address, abi=token_abi)
    token_symbol = token_contract.functions.symbol().call()
    # tokenDecimals = tokenContract.functions.decimals().call()

    token_initial_balance_full = token_contract.functions.balanceOf(wallet_address).call()
    token_initial_balance = web3.fromWei(token_initial_balance_full, 'ether')

    print(f"[+] Current {token_symbol} balance: {round(token_initial_balance, max_decimals)} ")
    print(f"[+] Watching {wallet_address} for token {token_address} ({token_symbol}) every {sleep_time_seconds}s\n")

    new_balance_full = token_initial_balance_full
    start_time = time.time()
    while new_balance_full <= token_initial_balance_full:
        time.sleep(sleep_time_seconds)
        new_balance_full = token_contract.functions.balanceOf(wallet_address).call()

    end_time = int(time.time() - start_time)
    os.system('say "Token received"')

    final_balance_full = new_balance_full - token_initial_balance_full
    final_balance = web3.fromWei(final_balance_full, 'ether')

    print(f"[+] {round(final_balance, max_decimals)} {token_symbol} arrived in the account.")
    print(f"[!] New {token_symbol} balance: {round(web3.fromWei(new_balance_full, 'ether'), max_decimals)} ")
    print('[+] Elapsed time: {:02d}:{:02d}:{:02d}'.
          format(end_time // 3600, (end_time % 3600 // 60), end_time % 60))
    return