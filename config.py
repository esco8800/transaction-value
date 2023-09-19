import json
from pathlib import Path

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open("accounts.txt", "r") as file:
    all_accounts = [row.strip() for row in file]
    ACCOUNTS = list(filter(lambda item: not item.startswith("//"), all_accounts))

with open("proxy.txt", "r") as file:
    all_proxies = [row.strip() for row in file]
    PROXIES = list(filter(lambda item: not item.startswith("//"), all_proxies))

with open('data/abi/zksync/bridge.json') as file:
    ZKSYNC_BRIDGE_ABI = json.load(file)

CONTRACT_PATH = Path("data/deploy/Token.json")
