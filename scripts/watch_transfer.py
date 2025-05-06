import time
from web3 import Web3
from utils.config import INFURA_URL
import json

# USDT contract example
ERC20_CONTRACT_ADDRESS = Web3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7")
TRANSFER_EVENT_SIGNATURE =  Web3.keccak(text="Transfer(address,address,uint256)").hex()
if not TRANSFER_EVENT_SIGNATURE.startswith("0x"):
    TRANSFER_EVENT_SIGNATURE = f"0x{TRANSFER_EVENT_SIGNATURE}"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def main():
    print("Listening for ERC20 Transfer events ...")
    latest_block = w3.eth.block_number
    max_rounds = 10
    rounds = 0
    found = False

    while rounds < max_rounds:        
        watched_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        topic_address = f"0x{watched_address.lower()[2:].rjust(64, '0')}"
        logs = w3.eth.get_logs({
            "fromBlock": latest_block,
            "toBlock": "latest",
            "address": ERC20_CONTRACT_ADDRESS,
            "topics": [
                TRANSFER_EVENT_SIGNATURE,
                # topic_address
            ]
        })

        # logs_to = w3.eth.get_logs({
        #     "fromBlock": latest_block,
        #     "toBlock": latest_block + 4,
        #     "address": ERC20_CONTRACT_ADDRESS,
        #     "topics": [
        #         TRANSFER_EVENT_SIGNATURE,
        #         None,
        #         topic_address
        #     ]
        # })

        # logs = logs_from + logs_to
        for log in logs:
            found = True
            from_address = '0x' + log['topics'][1].hex()[-40:]
            to_address = '0x' + log['topics'][2].hex()[-40:]
            amount = int.from_bytes(log['data'], byteorder='big') / (10 ** 6)  # USDT decimals = 6
            print(f"[+] Transfer: {amount} USDT from {from_address} to {to_address}")
        if found:
            break
        else:
            latest_block += 5
            rounds += 1
            time.sleep(1)
        w3.middleware_onion.clear()

if __name__ == "__main__":
    main()
 