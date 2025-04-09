from digit_client import RequestConfig, UserService, CitizenUserBuilder, RoleBuilder, UserBuilder
from pprint import pprint

def main():
    try:
        # Initialize with default auth token
        auth_token = "ba5e5f01-dbb5-4c94-95cf-5fa52ffae078"
        roles=[
            (RoleBuilder()
                .with_code("CITIZEN")
                .with_name("Citizen")
                .with_tenant_id("pg")
                .build()),
            (RoleBuilder()
                .with_code("EMPLOYEE")
                .with_name("Employee")
                .with_tenant_id("pg")
                .build()),
            (RoleBuilder()
                .with_code("ADMIN") 
                .with_name("Administrator")
                .with_tenant_id("pg")
                .build())
        ]
        userinfo = (UserBuilder()
            .with_id(1)
            .with_user_name("priyanhugupta753@gmail.com")
            .with_tenant_id("pg")
            .with_type("CITIZEN")
            .with_roles(roles)
            .with_mobile_number("9353822214")
            .with_email("priyanhugupta753@gmail.com")
            .with_name("Priyanhu Gupta")
            .with_uuid("1234567890")
            .build())
        
        
        # First initialize with basic config
        RequestConfig.initialize(
            api_id="DIGIT-CLIENT",
            version="1.0.0",
            user_info=userinfo.to_dict(),
            auth_token=auth_token
        )

        
        # Create user service
        user_service = UserService()

        # Example 1: Create a basic citizen user with minimum required fields
        basic_citizen = (CitizenUserBuilder()
            .with_user_name("9353822214")  # Using mobile number as username for OTP-based login
            .with_password("Must@123NK")
            .with_name("mustak")
            .with_gender("MALE")
            .with_mobile_number("9353822214")
            .with_tenant_id("POM")
            .build())  # Will automatically add CITIZEN role

        # Example 2: Create a detailed citizen user with all fields
        detailed_citizen = (CitizenUserBuilder()
            .with_user_name("93538222114")
            .with_password("Must@123NK")
            .with_salutation("Ms")
            .with_name("mustak")
            .with_gender("MALE")
            .with_mobile_number("9353822214")
            .with_email("xyz@egovernments.org")
            .with_alt_contact_number("")
            .with_pan("VFGGC5624P")
            .with_aadhaar("96a70")
            .with_permanent_address("Dawakhana")
            .with_permanent_city("Kaikoo")
            .with_permanent_pincode("111111")
            .with_correspondence_city("banglore")
            .with_correspondence_pincode("123456")
            .with_correspondence_address("correAddress")
            .with_active(True)
            .with_dob("08/08/1999")
            .with_locale("en_IN")
            .with_type("CITIZEN")
            .with_signature("")
            .with_account_locked(False)
            .with_father_or_husband_name("Palash")
            .with_blood_group("O_POSITIVE")
            .with_identification_mark("Wears spects")
            .with_photo("a8a6cf1e-c84d-4a0c-b2d5-57ec8711ba25")
            .with_otp_reference("14856")
            .with_tenant_id("POM")
            .with_roles(roles)
            .build())


        # Create citizen user
        response = user_service.create_user_no_validate(detailed_citizen)
        print("\nCreate Response:", response)

        # Update user
        update_response = user_service.update_user_no_validate(detailed_citizen)
        print("\nUpdate Response:")
        pprint(update_response)

    except ValueError as ve:
        print(f"Validation error: {str(ve)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()