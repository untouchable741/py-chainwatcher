from web3 import Web3
from utils.config import INFURA_URL

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
wallet_address = Web3.to_checksum_address("0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be")
# wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

# === ETH Balance ===
eth_balance = w3.eth.get_balance(wallet_address)
eth_in_eth = w3.from_wei(eth_balance, 'ether')
print(f"[ETH] Balance: {eth_in_eth} ETH")

# === USDT (ERC20) Balance ===
ERC20_ABI = [{
    "constant": True,
    "inputs": [{"name": "_owner", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"name": "balance", "type": "uint256"}],
    "type": "function"
}]

USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # Mainnet USDT
usdt = w3.eth.contract(address=USDT_CONTRACT, abi=ERC20_ABI)

usdt_balance_raw = usdt.functions.balanceOf(wallet_address).call()
usdt_balance = usdt_balance_raw / (10 ** 6)
print(f"[USDT] Balance: {usdt_balance} USDT")