#Still Not Working (Have to check if DID is actually registered)

import asyncio
from hiero_sdk_python import (
    Client,
    AccountId,
    PrivateKey,
    TopicUpdateTransaction,
    Network,
    TopicCreateTransaction,
    ResponseCode
)
from hiero_did_sdk_python import HederaDid, HederaDidResolver
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
did_test = os.getenv("DID_NUM")
e_did = "did:hedera:testnet:z23dtDSDE8E49gHsCrttG2GUWARpnoDR2aqVc5nL4KYuj_0.0.6922721"
resolver = HederaDidResolver(client)

async def resolvv():
    resolution_result = await resolver.resolve(e_did)
    print(resolution_result)
asyncio.run(resolvv())
