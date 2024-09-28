import json
from sys import stderr

from loguru import logger

logger.remove()
logger.add(
    stderr,
    format="<white>{time:HH:mm:ss}</white> | <level>{message}</level>",
)


CHAIN_DATA = {
    "ethereum": {
        "rpc": "https://rpc.ankr.com/eth",
        "explorer": "https://etherscan.io",
        "token": "ETH",
        "chain_id": 1,
    },
    "linea": {
        "rpc": "https://rpc.linea.build",
        "explorer": "https://lineascan.build",
        "token": "ETH",
        "chain_id": 59144,
    },
    "arbitrum": {
        "rpc": "https://rpc.ankr.com/arbitrum",
        "explorer": "https://arbiscan.io",
        "token": "ETH",
        "chain_id": 42161,
    },
    "bitlayer": {
        # "rpc": "https://rpc.bitlayer.org",
        "rpc": "https://rpc.ankr.com/bitlayer",
        "explorer": "https://www.btrscan.com",
        "token": "BTC",
        "chain_id": 200901,
    },
}


WBTC = "0xff204e2681a6fa0e2c3fade68a1b28fb90e4fc5f"
OWLTO = "0xa9d27096bae2f47caa03ae6a1692119c7d19b4b0"
BITLAYER_LOTTERY = "0xe0908344daf16c3d44a4c1a65af40a7fc115ecc0"


with open("data/abi/ERC20.json") as f:
    ERC20_ABI = json.load(f)
