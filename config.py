import package.abis as abi
import package.network_chains as chains

TOKEN_ADDRESS = ""  # token to be notified of
WALLET_ADDRESS = ""  # change to your wallet address
NETWORK = chains.ROPSTEN


USE_MAC_VOICE = False
USE_PUSHSAFER = False
PUSHSAFER_KEY = ""


SLEEP_TIME_SECONDS = 1  # check only once per 120 seconds until we're closer to IDO
MAX_DECIMALS = 2  # 2 is more visually appealing than 16

TOKEN_ABI = abi.token_abi
INFURA_API_KEY = ""  # for ETH and ROPSTEN networks
