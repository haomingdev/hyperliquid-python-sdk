import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hyperliquid.utils import constants
import example_utils
from hyperliquid.exchange import Exchange
from hyperliquid.utils.signing import sign_spot_transfer_action, get_timestamp_ms

def main():
    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True, exchange_class=Exchange)

    print(f"Account address: {exchange.account_address}")
    print(f"Wallet address: {exchange.wallet.address}")
    
    if exchange.account_address != exchange.wallet.address:
        raise Exception("Agents do not have permission to perform internal transfers")

    destination = "0xA6a60992f9399f07778E6703A69D84350094483D"
    amount = 4.20
    token_name = "KOBE"
    token_id = "0x0d2556646326733d86c3fc4c2fa22ad4"

    transfer_result = exchange.spot_transfer(amount, destination, token_name, token_id)
    print(transfer_result)

if __name__ == "__main__":
    main()
