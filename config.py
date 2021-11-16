import package.abis as abi
import package.network_chains as chains

token_abi = abi.token_abi

use_mac_voice = False
use_pushsafer = False
pushsafer_key = ""

SLEEP_TIME_SECONDS = 1  # check only once per 120 seconds until we're closer to IDO
MAX_DECIMALS = 2  # 2 is more visually appealing than 16

token_address = ""  # token to be notified of
wallet_address = ""  # change to your wallet address
network = chains.ROPSTEN
