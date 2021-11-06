#!/usr/bin/env python3
# Token Notifier
#     v1.2a
#        by Bogdan Vaida (contact@vaidabogdan.com)

# Checks wallet for token and pings you when it receives it

import sys
import config
from package import cmd_args as cmd_args
from package.web3_functions import connect, wait_for_token


def main(args):
    if len(args) == 1:
        network = config.network
        wallet_address = config.wallet_address
        token_address = config.token_address
        sleep_time_seconds = config.SLEEP_TIME_SECONDS
        max_decimals = config.MAX_DECIMALS
    else:
        network, wallet_address, token_address, sleep_time_seconds, max_decimals = cmd_args.get_arguments(args)
    token_abi = config.token_abi

    web3 = connect(network)
    wait_for_token(web3, wallet_address, token_address, token_abi, sleep_time_seconds, max_decimals)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\n[!] Interrupted")
        exit(0)
