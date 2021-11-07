# excitare_cito
#### v2.0 by Bogdan Vaida (contact@vaidabogdan.com)

Announces when a web3 wallet receives a token.

# Usage
You can use it by modifying config.py (without arguments) or using commandline arguments.
```
excitare_cito.py -n 1-4 -w wallet -t token [-s seconds] [-d decimals] [-vk]

If there are no arguments it will take the values from announcer_config.py

Usage:
        -n network is one of these numbers: 1. ETH, 2. ROPSTEN, 3. BSC, 4. POLYGON
        -s sleep time between queries, in seconds (default 1)
        -d is the decimals number to display when showing values (default 2, max 16)
        -v uses Mac's voice system for alert
        -k uses Pushsafer for remote alerts
```
