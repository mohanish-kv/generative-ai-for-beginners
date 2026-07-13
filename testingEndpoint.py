from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the Microsoft Foundry Models variables
endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

print(endpoint)