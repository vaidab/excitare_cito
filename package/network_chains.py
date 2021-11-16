import json

import config
from package.definitions import ROOT_DIR
import os

# https://github.com/ethereum-lists/chains/blob/master/_data/chains/eip155-56.json
ETH = os.path.join(ROOT_DIR, "data/eip155-1.json")  # https://etherscan.io/gastracker
ROPSTEN = os.path.join(ROOT_DIR, "data/eip155-3.json")  #
BSC = os.path.join(ROOT_DIR, "data/eip155-56.json")  # https://bscscan.com/gastracker
POLYGON = os.path.join(ROOT_DIR, "data/eip155-137.json")  # https://polygonscan.com/gastracker

chain_list = [ETH, ROPSTEN, BSC, POLYGON]


def get_network_data(chain_file):
    f = open(chain_file)
    network_data = json.load(f)
    f.close()
    return network_data


def show_network_info(network_data):
    print(f"[+] Connected to: {get_name(network_data)}")
    print(f"[+] Symbol: {get_network_token_symbol(network_data)}")
    print(f"[+] ChainId: {network_data['chainId']}")
    print(f"[+] RPC: {get_rpc(network_data)}")
    return


def get_rpc(network_data):
    rpc = network_data['rpc'][0]
    if rpc.find("${INFURA_API_KEY}"):
        rpc = rpc.replace("${INFURA_API_KEY}", config.INFURA_API_KEY)
    return rpc


def get_name(network_data):
    rpc = network_data['name']
    return rpc


def get_network_token_symbol(network_data):
    symbol = network_data['nativeCurrency']['symbol']
    return symbol


def get_network_token_decimals(network_data):
    decimals = network_data['nativeCurrency']['decimals']
    return decimals
