from digit_client.services.ServiceRequest import ServiceRequestService
from digit_client.models.ServiceRequest import (
    ServiceDefinition, ServiceDefinitionCriteria,
    Service, ServiceCriteria, Pagination,
    AttributeDefinition, DataTypeEnum, OrderEnum,
    AttributeValue, AuditDetails
)
from digit_client.request_config import RequestConfig

def create_service_definition_example():
    """
    Example showing how to create a service definition
    """
    # Initialize the service
    service = ServiceRequestService()
    
    # Create attribute definitions
    attribute1 = AttributeDefinition(
        code="name",
        data_type=DataTypeEnum.STRING,
        required=True,
        regex="^[a-zA-Z ]{3,50}$"
    )
    
    attribute2 = AttributeDefinition(
        code="age",
        data_type=DataTypeEnum.NUMBER,
        required=True
    )
    
    # Create service definition
    service_definition = ServiceDefinition(
        code="birth_registration",
        tenant_id="pb",
        attributes=[attribute1, attribute2],
        is_active=True
    )
    
    RequestConfig.initialize(
        api_id="DIGIT-CLIENT",
        version="1.0.0",
    )
    
    # Create the service definition
    response = service.create_service_definition(
        definition=service_definition,
    )
    
    print("Created Service Definition:", response)
    return response

def search_service_definitions_example():
    """
    Example showing how to search service definitions
    """
    # Initialize the service
    service = ServiceRequestService()
    
    # Create search criteria
    criteria = ServiceDefinitionCriteria(
        tenant_id="pb",
        codes=["birth_registration"]
    )
    
    # Create pagination
    pagination = Pagination(
        limit=10,
        offset=0,
        sort_by="code",
        order=OrderEnum.ASC
    )
    
    # Create request info
    request_info = RequestConfig.get_request_info()
    
    # Search service definitions
    response = service.search_service_definitions(
        criteria=criteria,
        pagination=pagination,
        request_info=request_info
    )
    
    print("Search Service Definitions Result:", response)
    return response

def create_service_request_example():
    """
    Example showing how to create a service request
    """
    # Initialize the service
    service = ServiceRequestService()
    
    # Create attribute values
    attribute1 = AttributeValue(
        attribute_code="name",
        value="John Doe"
    )
    
    attribute2 = AttributeValue(
        attribute_code="age",
        value=25
    )
    
    # Create service request
    service_request = Service(
        tenant_id="pb",
        service_def_id="birth_registration",  # Use the ID from created service definition
        account_id="account123",
        attributes=[attribute1, attribute2]
    )
    
    # Create request info
    request_info = RequestConfig.get_request_info()
    
    # Create the service request
    response = service.create_service(
        service=service_request,
        request_info=request_info
    )
    
    print("Created Service Request:", response)
    return response

def search_service_requests_example():
    """
    Example showing how to search service requests
    """
    # Initialize the service
    service = ServiceRequestService()
    
    # Create search criteria
    criteria = ServiceCriteria(
        tenant_id="pb",
        service_def_ids=["birth_registration"]
    )
    
    # Create pagination
    pagination = Pagination(
        limit=10,
        offset=0,
        sort_by="createdTime",
        order=OrderEnum.DESC
    )
    
    # Create request info
    request_info = RequestConfig.get_request_info()
    
    # Search service requests
    response = service.search_services(
        criteria=criteria,
        pagination=pagination,
        request_info=request_info
    )
    
    print("Search Service Requests Result:", response)
    return response

if __name__ == "__main__":
    # Run examples
    print("Creating Service Definition...")
    service_def = create_service_definition_example()
    
    print("\nSearching Service Definitions...")
    search_service_definitions_example()
    
    print("\nCreating Service Request...")
    service_req = create_service_request_example()
    
    print("\nSearching Service Requests...")
    search_service_requests_example() 