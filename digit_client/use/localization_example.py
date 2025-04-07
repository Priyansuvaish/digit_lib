from digit_client.services.localization import LocalizationService
from digit_client.models.localization import (
    Message, CreateMessagesRequest, UpdateMessageRequest,
    DeleteMessagesRequest, LocaleRequest, UpdateMessage,
    MessageBuilder, UpdateMessageBuilder, DeleteMessageBuilder,
    CreateMessagesRequestBuilder, UpdateMessageRequestBuilder,
    DeleteMessagesRequestBuilder, LocaleRequestBuilder
)
from digit_client.request_config import RequestConfig
from datetime import datetime

def main():
    
    RequestConfig.initialize(
        api_id="DIGIT-CLIENT",
        version="1.0.0",
        ts=datetime.now().timestamp(),
        action="create"
    )
    # Initialize the localization service
    localization_service = LocalizationService()

    # Example 1: Create new messages
    print("\nExample 1: Creating new messages")
    message1 = MessageBuilder() \
        .with_code("welcome.message") \
        .with_message("Welcome to our application!") \
        .with_module("common") \
        .with_locale("en_IN") \
        .build()

    message2 = MessageBuilder() \
        .with_code("error.not_found") \
        .with_message("The requested resource was not found") \
        .with_module("common") \
        .with_locale("en_IN") \
        .build()

    create_request = CreateMessagesRequestBuilder() \
        .with_tenant_id("pb.amritsar") \
        .add_message(message1) \
        .add_message(message2) \
        .build()

    create_response = localization_service.create_messages(create_request)
    print("Create response:", create_response)

    # Example 2: Search messages
    print("\nExample 2: Searching messages")
    search_request = LocaleRequestBuilder()\
        .with_locale("punjab")\
        .with_tenant_id("SETUP")\
        .with_module("BankKB_ALPHA")\
        .with_codes(["code1"])\
        .build()
    search_response = localization_service.search_messages(search_request)
    print("Search request:", search_request.to_dict())
    print("Search response:", search_response)

    # Example 3: Update messages
    print("\nExample 3: Updating messages")
    update_message = UpdateMessageBuilder() \
        .with_code("welcome.message") \
        .with_message("Welcome to our amazing application!") \
        .build()

    update_request = UpdateMessageRequestBuilder() \
        .with_tenant_id("pb.amritsar") \
        .with_locale("en_IN") \
        .with_module("common") \
        .add_message(update_message) \
        .build()

    update_response = localization_service.update_messages(update_request)
    print("Update response:", update_response)

    # Example 4: Delete messages
    print("\nExample 4: Deleting messages")
    delete_message = DeleteMessageBuilder() \
        .with_code("error.not_found") \
        .with_module("common") \
        .with_locale("en_IN") \
        .build()

    delete_request = DeleteMessagesRequestBuilder() \
        .with_tenant_id("pb.amritsar") \
        .add_message(delete_message) \
        .build()

    delete_response = localization_service.delete_messages(delete_request)
    print("Delete response:", delete_response)

    # Example 5: Upsert messages (create or update)
    print("\nExample 5: Upserting messages")
    upsert_message = MessageBuilder() \
        .with_code("new.feature") \
        .with_message("Check out our new feature!") \
        .with_module("common") \
        .with_locale("en_IN") \
        .build()

    upsert_request = CreateMessagesRequestBuilder() \
        .with_tenant_id("pb.amritsar") \
        .add_message(upsert_message) \
        .build()

    upsert_response = localization_service.upsert_messages(upsert_request)
    print("Upsert response:", upsert_response)

if __name__ == "__main__":
    main() 