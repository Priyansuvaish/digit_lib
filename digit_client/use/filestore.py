from digit_client.services.filestore import FileStoreService
from digit_client.models.filestore import (
    FileUploadRequestBuilder,
    FileRetrieveByIdRequestBuilder,
    FileRetrieveByTagRequestBuilder,
    FileRetrieveByUrlRequestBuilder
)
from digit_client.request_config import RequestConfig, RequestInfo
from digit_client.models import Role, UserBuilder
import os
import tempfile

def create_test_file(content="Test content", extension=".txt"):
    """Create a temporary test file for upload"""
    temp = tempfile.NamedTemporaryFile(suffix=extension, delete=False, mode='w')
    temp.write(content)
    temp.close()
    return temp.name

def example_file_upload():
    # Initialize the FileStore service
    filestore_service = FileStoreService()
    
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
    
    try:
        # Create test files
        test_file1 = create_test_file(content="Test document 1", extension=".txt")
        test_file2 = create_test_file(content="Test document 2", extension=".pdf")
        
        # Create file upload request
        file_upload_request = FileUploadRequestBuilder()\
            .with_tenant_id("LMN")\
            .with_module("PT")\
            .with_tag("document")\
            .with_files([test_file1, test_file2])\
            .build()
        
        # Upload files
        result = filestore_service.upload_files(
            file_upload_request=file_upload_request
        )
        
        print("Upload Result:", result)
        
        # Clean up test files
        os.unlink(test_file1)
        os.unlink(test_file2)
        
        return result
    except Exception as e:
        print(f"Error during file upload: {str(e)}")
        return None

def example_get_file_by_id():
    # Initialize the FileStore service
    filestore_service = FileStoreService()
    
    try:
        # Create file retrieve request
        file_retrieve_request = FileRetrieveByIdRequestBuilder()\
            .with_tenant_id("LMN")\
            .with_file_store_id("file-store-id")\
            .build()
        
        # Get file content
        result = filestore_service.get_file_by_id(
            file_retrieve_by_id_request=file_retrieve_request
        )
        
        print("File Content Length:", len(result) if result else 0, "bytes")
        return result
    except Exception as e:
        print(f"Error retrieving file: {str(e)}")
        return None

def example_get_file_metadata():
    # Initialize the FileStore service
    filestore_service = FileStoreService()
    
    try:
        # Create file retrieve request
        file_retrieve_request = FileRetrieveByIdRequestBuilder()\
            .with_tenant_id("LMN")\
            .with_file_store_id("file-store-id")\
            .build()
        
        # Get file metadata
        result = filestore_service.get_file_metadata(
            file_retrieve_by__request=file_retrieve_request
        )
        
        print("File Metadata:", result)
        return result
    except Exception as e:
        print(f"Error retrieving metadata: {str(e)}")
        return None

def example_get_file_urls():
    # Initialize the FileStore service
    filestore_service = FileStoreService()
    
    try:
        # Create file URL request
        file_url_request = FileRetrieveByUrlRequestBuilder()\
            .with_tenant_id("LMN")\
            .with_file_store_ids(["file-store-id-1", "file-store-id-2"])\
            .build()
        
        # Get file URLs
        result = filestore_service.get_file_urls(
            file_retrieve_by_url_request=file_url_request
        )
        
        print("File URLs:", result)
        return result
    except Exception as e:
        print(f"Error retrieving URLs: {str(e)}")
        return None

def example_get_files_by_tag():
    # Initialize the FileStore service
    filestore_service = FileStoreService()
    
    try:
        # Create tag request
        tag_request = FileRetrieveByTagRequestBuilder()\
            .with_tenant_id("LMN")\
            .with_tag("document")\
            .build()
        
        # Get files by tag
        result = filestore_service.get_files_by_tag(
            file_retrieve_by_tag_request=tag_request
        )
        
        print("Files by Tag:", result)
        return result
    except Exception as e:
        print(f"Error retrieving files by tag: {str(e)}")
        return None

if __name__ == "__main__":
    # Example 1: Upload files
    print("\n=== Example 1: Upload Files ===")
    upload_result = example_file_upload()
    
    if upload_result and 'fileStoreIds' in upload_result:
        file_store_id = upload_result['fileStoreIds'][0]
        
        # Example 2: Get file by ID
        print("\n=== Example 2: Get File by ID ===")
        file_content = example_get_file_by_id()
        
        # Example 3: Get file metadata
        print("\n=== Example 3: Get File Metadata ===")
        metadata = example_get_file_metadata()
        
        # Example 4: Get file URLs
        print("\n=== Example 4: Get File URLs ===")
        urls = example_get_file_urls()
        
        # Example 5: Get files by tag
        print("\n=== Example 5: Get Files by Tag ===")
        tagged_files = example_get_files_by_tag()
    else:
        print("Skipping remaining examples as file upload was not successful") 