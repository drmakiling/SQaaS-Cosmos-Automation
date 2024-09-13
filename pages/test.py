from dotenv import load_dotenv
import os

# Use the absolute path to the .env file
env_file_path = '/home/kgirard-admin/Downloads/learning-Automation-RT-master/environments/Dev/.env'

# Print the path to verify
print(f"Loading environment variables from: {env_file_path}")

# Load environment variables
load_dotenv(dotenv_path=env_file_path)

# Print loaded environment variables
print("STUDYBA1_ACCOUNT:", os.getenv('STUDYBA1_ACCOUNT'))
print("STUDYBA1_PASSWORD:", os.getenv('STUDYBA1_PASSWORD'))
print("STUDYBA2_ACCOUNT:", os.getenv('STUDYBA2_ACCOUNT'))
print("STUDYBA2_PASSWORD:", os.getenv('STUDYBA2_PASSWORD'))
print("CONTENTMANAGER1_ACCOUNT:", os.getenv('CONTENTMANAGER1_ACCOUNT'))
print("CONTENTMANAGER1_PASSWORD:", os.getenv('CONTENTMANAGER1_PASSWORD'))
print("CONTENTMANAGER2_ACCOUNT:", os.getenv('CONTENTMANAGER2_ACCOUNT'))
print("CONTENTMANAGER2_PASSWORD:", os.getenv('CONTENTMANAGER2_PASSWORD'))
print("IMPLELEAD1_ACCOUNT:", os.getenv('IMPLELEAD1_ACCOUNT'))
print("IMPLELEAD1_PASSWORD:", os.getenv('IMPLELEAD1_PASSWORD'))
print("IMPLELEAD2_ACCOUNT:", os.getenv('IMPLELEAD2_ACCOUNT'))
print("IMPLELEAD2_PASSWORD:", os.getenv('IMPLELEAD2_PASSWORD'))
print("STUDYPM1_ACCOUNT:", os.getenv('STUDYPM1_ACCOUNT'))
print("STUDYPM1_PASSWORD:", os.getenv('STUDYPM1_PASSWORD'))
print("STUDYPM2_ACCOUNT:", os.getenv('STUDYPM2_ACCOUNT'))
print("STUDYPM2_PASSWORD:", os.getenv('STUDYPM2_PASSWORD'))
print("CONFIGENGINEER1_ACCOUNT:", os.getenv('CONFIGENGINEER1_ACCOUNT'))
print("CONFIGENGINEER1_PASSWORD:", os.getenv('CONFIGENGINEER1_PASSWORD'))
print("CONFIGENGINEER2_ACCOUNT:", os.getenv('CONFIGENGINEER2_ACCOUNT'))
print("CONFIGENGINEER2_PASSWORD:", os.getenv('CONFIGENGINEER2_PASSWORD'))
print("TESTLEAD1_ACCOUNT:", os.getenv('TESTLEAD1_ACCOUNT'))
print("TESTLEAD1_PASSWORD:", os.getenv('TESTLEAD1_PASSWORD'))
print("TESTLEAD2_ACCOUNT:", os.getenv('TESTLEAD2_ACCOUNT'))
print("TESTLEAD2_PASSWORD:", os.getenv('TESTLEAD2_PASSWORD'))
