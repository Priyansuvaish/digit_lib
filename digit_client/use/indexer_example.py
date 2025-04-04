from digit_client.services.Indexer import IndexerService
from digit_client.request_config import RequestConfig, RequestInfo
from digit_client.models.Indexer import (
    LegacyIndexRequestBuilder,
    ReindexRequestBuilder,
    APIDetailsBuilder,
    PaginationDetailsBuilder
)

def main():
    # Initialize the service
    indexer_service = IndexerService()

    # Example 1: Legacy Indexing
    print("\nExample 1: Legacy Indexing")
    legacy_index_example(indexer_service)

    # Example 2: Index to Topic
    print("\nExample 2: Index to Topic")
    index_to_topic_example(indexer_service)

    # Example 3: Reindex Data
    print("\nExample 3: Reindex Data")
    reindex_data_example(indexer_service)

def legacy_index_example(service: IndexerService):
    # Create RequestInfo
    request_info = RequestInfo(
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

    # Create PaginationDetails
    pagination_details = PaginationDetailsBuilder() \
        .with_offset_key("offset") \
        .with_size_key("size") \
        .with_max_page_size(100) \
        .with_starting_offset(0) \
        .with_max_records(1000) \
        .build()

    # Create APIDetails
    api_details = APIDetailsBuilder() \
        .with_uri("https://api.example.com/data") \
        .with_pagination_details(pagination_details) \
        .with_response_json_path("$.data") \
        .with_request({"param1": "value1"}) \
        .with_tenant_id_for_open_search("tenant1") \
        .with_custom_query_param("custom=value") \
        .build()

    # Create LegacyIndexRequest
    legacy_request = LegacyIndexRequestBuilder() \
        .with_request_info(request_info) \
        .with_api_details(api_details) \
        .with_legacy_index_topic("finance-adoption-topic") \
        .with_tenant_id("tenant1") \
        .with_job_id("job-123") \
        .with_start_time(1234567890) \
        .with_total_records(1000) \
        .build()

    # Execute legacy index
    try:
        response = service.legacy_index(legacy_request,request_info)
        print("Legacy Index Response:", response)
    except Exception as e:
        print("Error in legacy index:", str(e))

def index_to_topic_example(service: IndexerService):
    # Create RequestInfo
    request_info = RequestInfo(
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

    # Example index data
    index_data = {
        "id": "123",
        "name": "Example Document",
        "type": "document",
        "content": "This is an example document content",
        "metadata": {
            "created": "2024-01-01",
            "modified": "2024-01-02"
        }
    }

    # Execute index to topic
    try:
        response = service.index_to_topic(
            topic="finance-adoption-topic",
            index_data=index_data,
            request_info=request_info
        )
        print("Index to Topic Response:", response)
    except Exception as e:
        print("Error in index to topic:", str(e))

def reindex_data_example(service: IndexerService):
    # Create RequestInfo
    request_info = RequestInfo(
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

    # Create ReindexRequest
    reindex_request = ReindexRequestBuilder() \
        .with_request_info(request_info) \
        .with_index("old-index") \
        .with_type("document") \
        .with_reindex_topic("finance-adoption-topic") \
        .with_tenant_id("tenant1") \
        .with_batch_size(100) \
        .with_job_id("reindex-job-123") \
        .with_start_time(1234567890) \
        .with_total_records(1000) \
        .build()

    # Execute reindex
    try:
        response = service.reindex_data(reindex_request,request_info)
        print("Reindex Response:", response)
    except Exception as e:
        print("Error in reindex:", str(e))

if __name__ == "__main__":
    main() 