from hiero_sdk_python import (
    Client,
    AccountId,
    PrivateKey,
    PublicKey,
    Network,
)
import os
from dotenv import load_dotenv
load_dotenv()
operator_key = PrivateKey.from_string(os.getenv("OPERATOR_KEY"))
der_privkey = operator_key.to_string()
public_key = PublicKey.from_string(os.getenv("PUBLIC_KEY"))
der_pubkey = public_key.to_string()
network = Network(network='testnet')
client = Client(network)
operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
