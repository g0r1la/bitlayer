# General settings
SHUFFLE_WALLETS = False
USE_PROXY = False

RETRY_COUNT = 1

SLEEP_BETWEEN_WALLETS = [10, 20]
SLEEP_BETWEEN_ACTIONS = [10, 20]

# If balance falls under this value, the wallet will be skipped
MIN_BTC_BALANCE = 0.000006

# WRAP BTC module
WRAP_VALUE = [0.0000001, 0.000001]
WRAP_TX_COUNT = [5, 10]

# BITCOW module
SWAP_VALUES = [0.000008, 0.000023]  # $0.5 - $1.5
SWAP_BACK_VALUES = [95, 99]  # e.g. 95-99%

# Avalon & LayerBank
DEPOSIT_VALUE = [0.0000001, 0.000001]
