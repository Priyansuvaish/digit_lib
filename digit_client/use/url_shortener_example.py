from digit_client import ShortenRequestService, ShortenRequestBuilder
from digit_client.config import Config
from digit_client.request_config import RequestConfig, RequestInfoBuilder

def main():
    # Configure the API endpoint
    Config.set_api_endpoint("https://scaler-demo.digit.org")  # Replace with your actual API endpoint
    
    # Set up request info
    
    RequestConfig.initialize(api_id="DIGIT-CLIENT", version="1.0.0", action="CREATE")
    
    # Create the service instance
    url_service = ShortenRequestService()

    try:
        # Example 1: Shorten a URL
        shorten_request = (
                ShortenRequestBuilder()
                .with_url("https://example.com/long-url-to-shorten")
                .with_valid_from(1672531200)  # Unix timestamp for validity start
                .with_valid_till(1672617600)  # Unix timestamp for validity end
                .build()
            )
        response = url_service.shorten_url(shorten_request)
        print("Shortened URL response:", response)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 