from hiero_sdk_python import (
    PrivateKey,
    AccountCreateTransaction,
    ResponseCode,
)
import sys

def create_new_account(Creator_key, Creator_id, client):
    client.set_operator(Creator_id, Creator_key)

    # Generate keypair
    new_account_private_key = PrivateKey.generate("ed25519")
    new_account_public_key = new_account_private_key.public_key()

    # Build transaction
    transaction = (
        AccountCreateTransaction()
        .set_key(new_account_public_key)
        .set_initial_balance(1000000000)  # 1 HBAR in tinybars
        .set_account_memo("My new account")
        .freeze_with(client)
    )

    # Sign
    transaction.sign(Creator_key)

    try:
        receipt = transaction.execute(client)
        print(f"Transaction status: {receipt.status}")

        if receipt.status != ResponseCode.SUCCESS:
            status_message = ResponseCode(receipt.status).name
            raise Exception(f"Transaction failed with status: {status_message}")

        new_account_id = receipt.accountId #Have to use accountId instead of account_id as specified in Github for some reason
        if new_account_id is not None:
            print(f"Account creation successful. New Account ID: {new_account_id}")
            print(f"New Account Private Key: {new_account_private_key.to_string()}")
            print(f"New Account Public Key: {new_account_public_key.to_string()}")
        else:
            raise Exception("AccountID not found in receipt. Account may not have been created.")

    except Exception as e:
        print(f"Account creation failed: {str(e)}")
        sys.exit(1)

