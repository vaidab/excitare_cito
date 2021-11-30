#!/usr/bin/env python3
# Token Notifier
#     v1.2a
#        by Bogdan Vaida (contact@vaidabogdan.com)

# Checks wallet for token and pings you when it receives it
import os
import sys
from getpass import getpass

import config as config
from package import cmd_args as cmd_args
from package.web3_functions import connect, wait_for_token, get_symbol
from package.pushsafer import alert


def main(args):
    if len(args) == 1:
        check_config()
        network = config.NETWORK
        wallet_address = config.WALLET_ADDRESS
        token_address = config.TOKEN_ADDRESS
        sleep_time_seconds = config.SLEEP_TIME_SECONDS
        max_decimals = config.MAX_DECIMALS
        use_pushsafer = config.USE_PUSHSAFER
        use_mac_voice = config.USE_MAC_VOICE
    else:
        network, wallet_address, token_address, sleep_time_seconds, \
            max_decimals, use_pushsafer, use_mac_voice = cmd_args.get_arguments(args)
    token_abi = config.TOKEN_ABI

    pushsafer_key = None
    if use_pushsafer:
        if config.PUSHSAFER_KEY:
            pushsafer_key = config.PUSHSAFER_KEY
        elif os.getenv('PUSHSAFER_KEY'):
            pushsafer_key = os.getenv('PUSHSAFER_KEY')
        else:
            pushsafer_key = getpass(prompt="[+] Input Pushsafer key: ")

    web3 = connect(network, sleep_time_seconds+10)
    wait_for_token(web3, wallet_address, token_address, token_abi, sleep_time_seconds, max_decimals)

    if use_pushsafer:
        alert(f"Token {get_symbol(web3, token_address, token_abi)} received", pushsafer_key)
    if use_mac_voice:
        os.system('say "Token received"')


def check_config():
    if len(config.WALLET_ADDRESS) != 42 and len(config.TOKEN_ADDRESS) != 42:
        print("Add a wallet address and a token address to the config file or use the command line arguments.")
        exit(1)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\n[!] Interrupted")
        exit(0)
