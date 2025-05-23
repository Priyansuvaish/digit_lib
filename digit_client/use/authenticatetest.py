from digit_client import AuthenticationService, AuthenticationRequestBuilder

# Initialize the service
auth_service = AuthenticationService()

# Create authentication request using builder
auth_request = (AuthenticationRequestBuilder()
    .with_username("priyanshugupta753@gmail.com")
    .with_password("password")
    .with_tenant_id("LMN")
    # Optional: override defaults if needed
    # .with_grant_type("password")
    # .with_scope("read")
    # .with_user_type("EMPLOYEE")
    .build())

# Get authentication token
response = auth_service.get_auth_token(auth_request)
print(response)