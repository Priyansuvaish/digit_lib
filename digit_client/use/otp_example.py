from digit_client.models.Otp import Otp, UserOtp, OtpBuilder, UserOtpBuilder, OtpRequestType
from digit_client.services.otp import UserOtpService, EgovOtpService
from digit_client.request_config import RequestConfig

def main():
    RequestConfig.initialize(
        api_id="DIGIT-CLIENT",
        version="1.0.0",
    )
    # Initialize the OTP service
    otp_service = UserOtpService()

    # Example 1: Send OTP to a user
    print("\nExample 1: Sending OTP to user")
    user_otp = UserOtpBuilder() \
        .with_mobile_number("9876543210") \
        .with_tenant_id("pb") \
        .with_type(OtpRequestType.LOGIN.value) \
        .with_user_type("CITIZEN") \
        .build()

    # Send OTP
    send_response = otp_service.user_send_otp(user_otp)
    print(f"OTP sent response: {send_response}")

    otp_service = EgovOtpService()

    # Example 2: Create OTP
    print("\nExample 2: Creating OTP")
    otp = OtpBuilder() \
        .with_identity("9876543210") \
        .with_tenant_id("pb") \
        .build()

    create_response = otp_service.create_otp(otp)
    print(f"OTP creation response: {create_response}")

    # Example 3: Validate OTP
    print("\nExample 3: Validating OTP")
    # Assuming we got the UUID from create_otp response
    validation_otp = OtpBuilder() \
        .with_otp("123456") \
        .with_uuid(create_response.get("otp", {}).get("UUID")) \
        .with_identity("9876543210") \
        .with_tenant_id("pb") \
        .build()

    validate_response = otp_service.validate_otp(validation_otp)
    print(f"OTP validation response: {validate_response}")

    # Example 4: Search OTP status
    print("\nExample 4: Searching OTP status")
    search_otp = OtpBuilder() \
        .with_uuid(create_response.get("otp", {}).get("UUID")) \
        .with_tenant_id("pb") \
        .build()

    search_response = otp_service.search_otp(search_otp)
    print(f"OTP search response: {search_response}")

if __name__ == "__main__":
    main() 