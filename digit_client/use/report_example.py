from digit_client.services.Report import ReportService
from digit_client.models.Report import (
    MetadataRequest,
    ReportRequest,
    SearchParam,
    MetadataRequestBuilder,
    ReportRequestBuilder,
    SearchParamBuilder
)
from digit_client.request_config import RequestInfo

def main():
    # Initialize the Report Service
    report_service = ReportService()

    # Example 1: Get Report Metadata
    # Create a metadata request using the builder pattern
    metadata_request = (
        MetadataRequestBuilder()
        .with_tenant_id("your_tenant_id")
        .with_report_name("your_report_name")
        .build()
    )

    # Get metadata for a report
    metadata_response = report_service.create_v1_metadata(
        module_name="your_module",
        version="v1",
        request=metadata_request,
        request_info=RequestInfo(
        api_id="org.egov.indexer",
        ver="1.0",
        ts=1234567890,
        action="POST",
        did="some-did",
        key="some-key",
        msg_id="some-msg-id",
        requester_id="some-requester-id",
        auth_token="some-auth-token"
    )
    )
    print("Metadata Response:", metadata_response)

    # Example 2: Get Report Data
    # Create a search parameter
    search_param = (
        SearchParamBuilder()
        .with_input({"key": "value"})  # Replace with your actual search criteria
        .build()
    )

    # Create a report request using the builder pattern
    report_request = (
        ReportRequestBuilder()
        .with_tenant_id("your_tenant_id")
        .with_report_name("your_report_name")
        .add_search_param(search_param)
        .build()
    )

    # Get report data
    report_data = report_service.get_report_data_v1(
        module_name="your_module",
        version="v1",
        request=report_request,
        request_info=RequestInfo(
        api_id="org.egov.indexer",
        ver="1.0",
        ts=1234567890,
        action="POST",
        did="some-did",
        key="some-key",
        msg_id="some-msg-id",
        requester_id="some-requester-id",
        auth_token="some-auth-token"
    )
    )
    print("Report Data:", report_data)

if __name__ == "__main__":
    main() 