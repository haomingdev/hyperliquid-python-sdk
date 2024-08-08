# from hyperliquid.utils import constants
# import example_utils


# def main():
#     address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)

#     if exchange.account_address != exchange.wallet.address:
#         raise Exception("Agents do not have permission to perform internal transfers")

#     # Transfer 1 usd to the zero address for demonstration purposes
#     transfer_result = exchange.usd_transfer(1.0, "0x7e6478bA06921A3f16fbFC2Ae7525dba6d1Fa8Fd")
#     print(transfer_result)


# if __name__ == "__main__":
#     main()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hyperliquid.utils import constants
import example_utils
from hyperliquid.exchange import Exchange

def basic_transfer(private_key, destination, amount):
    address, info, exchange = example_utils.setup(
        constants.MAINNET_API_URL, 
        private_key=private_key, 
        skip_ws=True, 
        exchange_class=Exchange
    )

    print(f"Account address: {exchange.account_address}")
    print(f"Wallet address: {exchange.wallet.address}")
    
    if exchange.account_address != exchange.wallet.address:
        raise Exception("Agents do not have permission to perform internal transfers")

    transfer_result = exchange.usd_transfer(amount, destination)
    return transfer_result

def main():
    # Example usage
    private_key = "privatekey"  
    destination = "receiveraddress"
    amount = 1.1

    result = basic_transfer(private_key, destination, amount)
    print(result)

if __name__ == "__main__":
    main()