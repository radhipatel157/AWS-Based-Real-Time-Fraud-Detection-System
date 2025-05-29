import os
import boto3

# Fetch credentials securely from system environment variables
aws_access_key = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_region = os.environ.get("AWS_REGION", "us-east-1")  # Default to us-east-1

# Initialize Fraud Detector client
fraud_detector = boto3.client(
    'frauddetector',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Sample transaction event
event_details = {
    "eventId": "sample-event-id-001",
    "eventTypeName": "frauddetection",
    "eventTimestamp": "2024-12-08T08:59:18Z",
    "entities": [
        {
            "entityType": "customer",
            "entityId": "customer-001"
        }
    ],
    "eventVariables": {
        "card_bin": "493339",
        "customer_name": "John Doe",
        "billing_street": "123 Main Street",
        "billing_city": "New York",
        "billing_state": "NY",
        "billing_zip": "10001",
        "billing_latitude": "40.7128",
        "billing_longitude": "-74.0060",
        "billing_country": "US",
        "customer_job": "Engineer",
        "ip_address": "192.168.0.1",
        "customer_email": "johndoe@example.com",
        "billing_phone": "123-456-7890",
        "user_agent": "Mozilla/5.0",
        "product_category": "electronics",
        "order_price": "199.99",
        "payment_currency": "USD",
        "merchant": "merchant_demo"
    }
}

# Get fraud prediction
response = fraud_detector.get_event_prediction(
    detectorId="frauddetector",
    eventId=event_details["eventId"],
    eventTypeName=event_details["eventTypeName"],
    eventTimestamp=event_details["eventTimestamp"],
    entities=event_details["entities"],
    eventVariables=event_details["eventVariables"]
)

print("Prediction Response:\n", response)
