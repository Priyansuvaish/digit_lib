from digit_client.services.Encrypts import EncryptsService
from digit_client.models.Encrypts import (
    EncReqObject, EncReqObjectBuilder,
    SignRequest, SignRequestBuilder,
    VerifyRequest, VerifyRequestBuilder,
    RotateKeyRequest, RotateKeyRequestBuilder,
    Signature
)

def main():
    # Initialize the encryption service
    encrypts_service = EncryptsService()

    # Example 1: Encrypt data
    print("\n=== Example 1: Encrypting Data ===")
    encryption_request = (
        EncReqObjectBuilder()
        .with_tenant_id("pb.amritsar")
        .with_type("PLAIN")
        .with_value("Sensitive data to encrypt")
        .build()
    )
    
    try:
        encrypted_response = encrypts_service.encrypt_data([encryption_request])
        print("Encrypted Response:", encrypted_response)
    except Exception as e:
        print("Encryption failed:", str(e))

    # Example 2: Create digital signature
    print("\n=== Example 2: Creating Digital Signature ===")
    sign_request = (
        SignRequestBuilder()
        .with_tenant_id("pb.amritsar")
        .with_value("Data to be signed")
        .build()
    )
    
    try:
        signature = encrypts_service.create_digital_signature(sign_request)
        print("Generated Signature:", signature)
    except Exception as e:
        print("Signature creation failed:", str(e))

    # Example 3: Verify signature
    print("\n=== Example 3: Verifying Signature ===")
    verify_request = (
        VerifyRequestBuilder()
        .with_value("Data to be signed")
        .with_signature(Signature("123|signature").to_dict())
        .build()
    )
    
    try:
        is_valid = encrypts_service.verify_signature(verify_request)
        print("Signature is valid:", is_valid)
    except Exception as e:
        print("Signature verification failed:", str(e))

    # Example 4: Rotate keys
    print("\n=== Example 4: Rotating Keys ===")
    rotate_request = (
        RotateKeyRequestBuilder()
        .with_tenant_id("pb.amritsar")
        .build()
    )
    
    try:
        rotation_result = encrypts_service.rotate_all_keys(rotate_request)
        print("Key rotation result:", rotation_result)
    except Exception as e:
        print("Key rotation failed:", str(e))

if __name__ == "__main__":
    main()