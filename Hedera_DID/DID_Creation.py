from hiero_did_sdk_python import HederaDid
from hiero_sdk_python import Network, Client, AccountId, PrivateKey
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
operator_key = PrivateKey.from_string(os.getenv("OPERATOR_KEY"))
der_privkey = operator_key.to_string()
network = Network(network='testnet')
client = Client(network)
operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
client.set_operator(operator_id, operator_key)
did = HederaDid(client=client, private_key_der=der_privkey)

async def main():
    await did.register()
    print(f"✅ DID registered: {did.identifier}")
    await did.add_service(
        id_=f"{did.identifier}#service-1", service_type="LinkedDomains", service_endpoint="https://example.com/vcs"
    )
asyncio.run(main())
