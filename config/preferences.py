from dotenv import load_dotenv
import os

load_dotenv()

class Preferences:
    def __init__(self):
        # Load the environment variables into the object
        self.time_slot = os.getenv("START_TIME" , 12.0) # Default to 12 pm if START_TIME is not set
        self.category_value = int(os.getenv("CATEGORY_VALUE", 0))  # Default to 0 if CATEGORY_VALUE is not set
        self.profile_path = os.getenv("PROFILE_PATH", "")
        self.public_name = os.getenv("PUBLIC_NAME", "GUEST")
        self.ucf_id = os.getenv("UCF_ID", "")
    
    def __repr__(self):
        return f"Preferences(time_slot={self.time_slot}, category_value={self.category_value})"
    
    def get_time_slot(self):
        return float(self.time_slot)

    def get_category_value(self):
        return self.category_value
    def get_profiile_path(self):
        return self.profile_path
    def get_public_name(self):
        return self.public_name
    def get_ucf_id(self):
        return str(self.get_ucf_id)

