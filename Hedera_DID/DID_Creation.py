from hiero_did_sdk_python import HederaDid
import asyncio

from hed_test.Client_set import (
    operator_id, 
    operator_key, 
    der_privkey, 
    der_pubkey,
    issuer_id,
    der_pubkey_issuer,
    der_privkey_issuer,
    issuer_key, 
    client)


client.set_operator(issuer_id, issuer_key)
did = HederaDid(client=client, private_key_der=der_privkey_issuer)

async def main():
    await did.register()
    print(f"✅ DID registered: {did.identifier}")
    """
sample result
    
{
  "message": {
    "timestamp": 1760460388.2378209,
    "operation": "create",
    "did": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254",
    "event": "eyJWZXJpZmljYXRpb25NZXRob2QiOiB7ImlkIjogImRpZDpoZWRlcmE6dGVzdG5ldDp6RzdMRHl5Q3JtVjNlRlNEVTVaNzZGa2hxZjF0VG1xaXlKY1VEaDM2VXBnZ3FfMC4wLjcwNTgyNTQja2V5LTEiLCAidHlwZSI6ICJFZDI1NTE5VmVyaWZpY2F0aW9uS2V5MjAxOCIsICJjb250cm9sbGVyIjogImRpZDpoZWRlcmE6dGVzdG5ldDp6RzdMRHl5Q3JtVjNlRlNEVTVaNzZGa2hxZjF0VG1xaXlKY1VEaDM2VXBnZ3FfMC4wLjcwNTgyNTQiLCAicHVibGljS2V5QmFzZTU4IjogIjIzZHREU0RFOEU0OWdIc0NydHRHMkdVV0FScG5vRFIyYXFWYzVuTDRLWXVqIn19"
  },
  "signature": "signature hash"}

  event decoded:

  {"DIDOwner": {
  "id": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254#did-root-key", 
  "type": "Ed25519VerificationKey2018", 
  "controller": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254", 
  "publicKeyBase58": "G7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq"}}      
    
    """


    await did.add_service(
        id_=f"{did.identifier}#service-1", service_type="LinkedDomains", service_endpoint="https://example.com/vcs"
    )

    """event decoded
    
    {"Service": {
    "id": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254#service-1", 
    "type": "LinkedDomains", 
    "serviceEndpoint": "https://example.com/vcs"}}
    
    """
    await did.add_verification_method(
        id_=f"{did.identifier}#key-1",controller=did.identifier,public_key_der=der_pubkey,type_="Ed25519VerificationKey2018")
    
    """
    event decoded
    {"VerificationMethod": {
    "id": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254#key-1", 
    "type": "Ed25519VerificationKey2018", "controller": "did:hedera:testnet:zG7LDyyCrmV3eFSDU5Z76Fkhqf1tTmqiyJcUDh36Upggq_0.0.7058254", 
    "publicKeyBase58": "23dtDSDE8E49gHsCrttG2GUWARpnoDR2aqVc5nL4KYuj"}}

    
    """

    await asyncio.sleep(20)


    print(did.topic_id)

asyncio.run(main())
