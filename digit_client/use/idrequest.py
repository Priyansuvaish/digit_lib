from digit_client.services.idrequest import IdRequestService
from digit_client.models import IdRequest, IdRequestBuilder,Role,UserBuilder
from digit_client.request_config import RequestConfig, RequestInfo

def example_generate_id():
    # Initialize the IdRequest service
    id_request_service = IdRequestService()
    # Create user info
    roles = [
        Role(
            name="Employee",
            code="EMPLOYEE",
            tenant_id="LMN"
        ),
        Role(
            name="System user",
            code="SYSTEM",
            tenant_id="LMN"
        )
    ]
    
    auth_token = "0e9b955f-5e25-4809-b680-97ef37ccf53f"
    user_info = UserBuilder()\
        .with_id(181)\
        .with_user_name("TestEggMUSTAKIMNK")\
        .with_uuid("4f6cf5fa-bcb2-4a3a-9dff-9740c04e3a92")\
        .with_type("EMPLOYEE")\
        .with_name("mustak")\
        .with_mobile_number("1234567890")\
        .with_email("xyz@egovernments.org")\
        .with_roles(roles)\
        .with_tenant_id("LMN")\
        .build()
    
    # Initialize RequestConfig with user info
    RequestConfig.initialize(
        api_id="DIGIT-CLIENT",
        version="1.0.0",
        user_info=user_info.to_dict(),
        auth_token=auth_token
    )
    # Create an IdRequest object
    id_request = IdRequestBuilder()\
        .with_id_name("test_id_name")\
        .with_tenant_id("test_tenant_id")\
        .with_format("test_format")\
        .build()

    # Generate IDs
    result = id_request_service.generate_id(id_request)
    print(result)
        
if __name__ == "__main__":
    example_generate_id()

