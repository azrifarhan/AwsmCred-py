#Still Not Working (Have to check if DID is actually registered)

import asyncio
from hiero_sdk_python import (
    Client,
    AccountId,
    PrivateKey,
    Network,
)
from hiero_did_sdk_python import HederaDid
from test_client import client
import os
from dotenv import load_dotenv
load_dotenv()
operator_key = PrivateKey.from_string(os.getenv("OPERATOR_KEY"))
der_privkey = operator_key.to_string()
network = Network(network='testnet')
client = Client(network)
operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
client.set_operator(operator_id, operator_key)
e_did = "did:hedera:testnet:z23dtDSDE8E49gHsCrttG2GUWARpnoDR2aqVc5nL4KYuj_0.0.6922721"


async def resolvv():
    lmao = await did.resolve()
    did_document_dict = lmao.get_json_payload()
    print(did_document_dict)
asyncio.run(resolvv())
