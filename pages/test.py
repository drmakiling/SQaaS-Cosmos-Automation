from dotenv import load_dotenv
import os

# Use the absolute path to the .env file
env_file_path = '/home/kgirard-admin/Downloads/learning-Automation-RT-master/environments/Dev/.env'

# Print the path to verify
print(f"Loading environment variables from: {env_file_path}")

# Load environment variables
load_dotenv(dotenv_path=env_file_path)

# Print loaded environment variables
print("USER1_ACCOUNT:", os.getenv('USER1_ACCOUNT'))
print("USER1_PASSWORD:", os.getenv('USER1_PASSWORD'))
