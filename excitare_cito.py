#!/usr/bin/env python3
# Token Notifier
#     v1.2a
#        by Bogdan Vaida (contact@vaidabogdan.com)

# Checks wallet for token and pings you when it receives it
import os
import sys
from getpass import getpass

import config
from package import cmd_args as cmd_args
from package.web3_functions import connect, wait_for_token
from package.pushsafer import alert


def main(args):
    if len(args) == 1:
        network = config.network
        wallet_address = config.wallet_address
        token_address = config.token_address
        sleep_time_seconds = config.SLEEP_TIME_SECONDS
        max_decimals = config.MAX_DECIMALS
        use_pushsafer = config.use_pushsafer
    else:
        network, wallet_address, token_address, sleep_time_seconds, \
            max_decimals, use_pushsafer = cmd_args.get_arguments(args)
    token_abi = config.token_abi

    pushsafer_key = None
    if use_pushsafer:
        if config.pushsafer_key:
            pushsafer_key = config.pushsafer_key
        else:
            pushsafer_key = getpass(prompt="[+] Input Pushsafer key: ")

    web3 = connect(network)
    wait_for_token(web3, wallet_address, token_address, token_abi, sleep_time_seconds, max_decimals)

    os.system('say "Token received"')
    if use_pushsafer:
        alert(f"Token {token_address} received", pushsafer_key)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\n[!] Interrupted")
        exit(0)
