from models.wallet import Wallet
from modules.config import WBTC, logger


class Wrapper(Wallet):
    def __init__(self, private_key, counter):
        super().__init__(private_key, counter)
        self.label += "WBTC |"
        contract_abi = [
            {"type": "function", "name": "deposit", "inputs": []},
            {
                "type": "function",
                "name": "withdraw",
                "inputs": [{"name": "amount", "type": "uint256"}],
            },
        ]
        self.contract = self.get_contract(WBTC, abi=contract_abi)

    def deposit(self, amount):
        amount_wei = self.web3.to_wei(amount, "ether")

        contract_tx = self.contract.functions.deposit().build_transaction(
            self.get_tx_data(value=amount_wei)
        )

        return self.send_tx(
            contract_tx,
            tx_label=f"{self.label} wrap {amount:.8f} BTC [{self.tx_count}]",
        )

    def withdraw(self):
        balance, decimals, symbol = self.get_token(WBTC)

        if not balance:
            logger.warning(f"{self.label} no {symbol} balance to withdraw \n")
            return

        contract_tx = self.contract.functions.withdraw(balance).build_transaction(
            self.get_tx_data()
        )

        return self.send_tx(
            contract_tx,
            tx_label=f"{self.label} unwrap {balance / 10 ** decimals:.8f} {symbol} [{self.tx_count}]",
        )
