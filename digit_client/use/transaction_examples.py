from decimal import Decimal
from digit_client.services.Transaction import TransactionService
from digit_client.models.Transactions import (
    Transaction, TransactionCriteria, TxnStatusEnum,
    TaxAndPayment, TransactionBuilder, TransactionCriteriaBuilder,
    TaxAndPaymentBuilder
)
from digit_client.models import User, UserBuilder, Role
from digit_client.models.mdms_v2 import AuditDetails
from digit_client.request_config import RequestConfig, RequestInfo

def create_transaction_example():
    
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
    # Create tax payment details
    tax_payment = (TaxAndPaymentBuilder()
        .with_tax_amount(Decimal("1000.00"))
        .with_amount_paid(Decimal("1000.00"))
        .with_bill_id("BILL123")
        .build())
    
    # Create a transaction using the builder pattern
    transaction = (TransactionBuilder()
        .with_tenant_id("pb")
        .with_txn_amount("1000.00")
        .with_bill_id("BILL123")
        .with_consumer_code("CONSUMER123")
        .with_product_info("Property Tax")
        .with_gateway("PAYTM")
        .with_callback_url("https://example.com/callback")
        .with_user(user_info)
        .with_module("PT")
        .add_tax_payment(tax_payment)
        .build())

    # Add tax payment to transaction
    transaction.tax_and_payments.append(tax_payment)

    # Initialize transaction service
    transaction_service = TransactionService()

    # Create transaction
    response = transaction_service.create_transaction(transaction)
    print("Created Transaction:", response)

def search_transactions_example():
    # Create search criteria using builder pattern
    criteria = (TransactionCriteriaBuilder()
        .with_tenant_id("pb")
        .with_txn_status(TxnStatusEnum.SUCCESS)
        .with_limit(10)
        .with_offset(0)
        .build())

    # Initialize transaction service
    transaction_service = TransactionService()

    # Search transactions
    response = transaction_service.search_transactions(criteria)
    print("Search Results:", response)

def update_transaction_example():
    # Initialize transaction service
    transaction_service = TransactionService()

    # Update transaction status
    update_params = {
        "txnId": "TXN123",
        "txnStatus": TxnStatusEnum.SUCCESS.value,
        "txnStatusMsg": "Payment successful"
    }

    response = transaction_service.update_transaction(update_params)
    print("Updated Transaction:", response)

def search_gateway_transactions_example():
    # Initialize transaction service
    transaction_service = TransactionService()

    # Search gateway transactions
    response = transaction_service.search_gateway_transactions()
    print("Gateway Transactions:", response)

def main():
    print("=== Transaction Service Examples ===")
    
    print("\n1. Creating a Transaction")
    create_transaction_example()
    
    print("\n2. Searching Transactions")
    search_transactions_example()
    
    print("\n3. Updating a Transaction")
    update_transaction_example()
    
    print("\n4. Searching Gateway Transactions")
    search_gateway_transactions_example()

if __name__ == "__main__":
    main() 