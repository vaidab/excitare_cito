import package.abis as abi
import package.network_chains as chains

token_abi = abi.token_abi
use_pushsafer = True
pushsafer_key = ""

SLEEP_TIME_SECONDS = 1  # check only once per 120 seconds until we're closer to IDO
MAX_DECIMALS = 2  # 2 is more visually appealing than 16

token_address = "0xc778417e063141139fce010982780140aa0cd5ab"  # token to be notified of
wallet_address = "0x1F53592C3aA6b827C64C4a3174523182c52Ece84"  # change to your wallet address
network = chains.ROPSTEN
