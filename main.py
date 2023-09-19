from starknet_py.contract import Contract
from starknet_py.net.gateway_client import GatewayClient


def main():
    contract = Contract.from_address_sync(
        address="0x06689f1bf69af5b8e94e5ab9778c885b37c593d1156234eb423967621f596e73",
        client=GatewayClient("testnet"),
    )
    (value,) = contract.functions["get_balance"].call_sync()
    print(f'Value: {value}')


if __name__ == "__main__":
    main()
