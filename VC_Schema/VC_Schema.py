import json
from datetime import date

normal_schema = {
    "@context": [
        "https://www.w3.org/ns/credentials/v2",
        "https://www.w3.org/ns/credentials/examples/v2"
    ],
    "type": ["VerifiableCredential", "AgeCred"],
    "issuer": {
        "id": issuer_did,
        "name": "AwsmCred"
    },
    "credentialSubject": {
        "id": holder_did,
        "name": "Holder Name",
        "birthDate": "date"   # Example date in YYYY-MM-DD format
    },
    "proof": {
        "type": "DataIntegrityProof",
        "cryptosuite": "eddsa-rdfc-2022",
        "verificationMethod": ,
        "proofValue": "BASE58_OR_JWS_SIGNATURE"
    }
}
}


with open("vc_schema.json", "w") as f:
    json.dump(vc_schema, f, indent=2)


