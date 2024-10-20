from dotenv import load_dotenv
import os

load_dotenv('.env')

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
if __name__ == "__main__":
    print(API_HASH)
    print(API_ID)
