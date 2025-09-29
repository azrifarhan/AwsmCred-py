import os
from dotenv import load_dotenv
from hiero_sdk_python import (
    Network,
    Client,
    AccountId,
    PrivateKey,
    CryptoGetAccountBalanceQuery,
)

load_dotenv()

def check_balance():
    network = Network(network='testnet')
    client = Client(network)

    operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    print(os.getenv('OPERATOR_ID'))
    print(os.getenv('OPERATOR_KEY'))
    operator_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    client.set_operator(operator_id, operator_key)

    # Check balance
    balance_query = CryptoGetAccountBalanceQuery().set_account_id(operator_id)
    balance = balance_query.execute(client)
    print(f"Initial balance of new account: {balance.hbars} hbars")

if __name__ == "__main__":
    check_balance()
