import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hyperliquid.utils import constants
import example_utils
from hyperliquid.exchange import Exchange
from hyperliquid.utils.signing import sign_spot_transfer_action, get_timestamp_ms

def spot_transfer(private_key, destination, amount, token_name, token_id):
    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, private_key=private_key, skip_ws=True, exchange_class=Exchange)

    print(f"Account address: {exchange.account_address}")
    print(f"Wallet address: {exchange.wallet.address}")
    
    if exchange.account_address != exchange.wallet.address:
        raise Exception("Agents do not have permission to perform internal transfers")

    transfer_result = exchange.spot_transfer(amount, destination, token_name, token_id)
    return transfer_result

def main():
    # Example usage
    private_key = "privatekey"
    destination = "receiveraddress"
    amount = 1.1
    token_name = "KOBE"
    token_id = "0x0d2556646326733d86c3fc4c2fa22ad4"

    result = spot_transfer(private_key, destination, amount, token_name, token_id)
    print(result)

if __name__ == "__main__":
    main()
