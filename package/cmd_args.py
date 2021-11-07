import getopt
import sys

from package import network_chains
import config

options = "n:t:w:s:d:kvh"
long_options = ["network =", "wallet =", "token =", "seconds =", "decimals =", "key", "voice", "help"]


def get_arguments(args):
    argument_list = args[1:]

    token_address = None
    wallet_address = None
    network = None
    sleep_time_seconds = config.SLEEP_TIME_SECONDS
    max_decimals = config.MAX_DECIMALS
    use_pushsafer = False
    use_mac_voice = False

    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)

        if len(sys.argv) < 6:
            show_usage()
            exit(1)
        for current_argument, current_value in arguments:
            if current_argument in ("-n", "--network"):
                network_number = int(current_value) - 1
                network = network_chains.chain_list[network_number]
            elif current_argument in ("-w", "--wallet"):
                wallet_address = current_value
            elif current_argument in ("-t", "--contract"):
                token_address = current_value
            elif current_argument in ("-s", "--seconds"):
                sleep_time_seconds = int(current_value)
            elif current_argument in ("-d", "--decimals"):
                max_decimals = int(current_value)
            elif current_argument in ("-k", "--key"):
                use_pushsafer = True
            elif current_argument in ("-v", "--voice"):
                use_mac_voice = True

    except getopt.error as err:
        print(str(err) + "\n")
        show_usage()
        exit(1)

    if not network or not wallet_address or not token_address:
        show_usage()
        exit(1)

    return network, wallet_address, token_address, sleep_time_seconds, max_decimals, use_pushsafer, use_mac_voice


def show_usage():
    print("excitare_cito.py -n 1-4 -w wallet -t token [-s seconds] [-d decimals] [-vk]\n")
    print("If there are no arguments it will take the values from announcer_config.py\n")
    print("Usage:")
    print("\t-n network is one of these numbers: 1. ETH, 2. ROPSTEN, 3. BSC, 4. POLYGON")
    print("\t-s sleep time between queries, in seconds (default 1)")
    print("\t-d is the decimals number to display when showing values (default 2, max 16)")
    print("\t-v uses Mac's voice system for alert")
    print("\t-k uses Pushsafer for remote alerts")
    return


def show_arguments(network, wallet_address, token_address, sleep_time_seconds,
                   max_decimals, use_pushsafer, use_mac_voice):
    print("[+] Network: " + network)
    print("[+] Wallet: " + wallet_address)
    print("[+] Token: " + token_address)
    print("[+] Sleep: " + str(sleep_time_seconds))
    print("[+] Decimals: " + str(max_decimals))
    print("[+] Use Pushsafer: " + use_pushsafer)
    print("[+] Use Mac voice: " + use_mac_voice)
    return


def main(args):
    network, wallet_address, token_address, sleep_time_seconds, \
        max_decimals, use_pushsafer, use_mac_voice = get_arguments(args)
    show_arguments(network, wallet_address, token_address,
                   sleep_time_seconds, max_decimals, use_pushsafer, use_mac_voice)


if __name__ == "__main__":
    main(sys.argv)
