from datetime import datetime

from models.wallet import Wallet
from modules.config import OWLTO
from modules.utils import check_min_balance


class Owlto(Wallet):
    def __init__(self, private_key, counter):
        super().__init__(private_key, counter)
        self.label += "Owlto |"
        contract_abi = [
            {
                "type": "function",
                "name": "checkIn",
                "inputs": [{"name": "date", "type": "uint256"}],
            }
        ]
        self.contract = self.get_contract(OWLTO, abi=contract_abi)

    @check_min_balance
    def check_in(self):
        date = int(datetime.now().strftime("%Y%m%d"))

        tx_data = self.get_tx_data()
        contract_tx = self.contract.functions.checkIn(date).build_transaction(tx_data)

        return self.send_tx(
            contract_tx,
            tx_label=f"{self.label} check-in [{self.tx_count}]",
        )
