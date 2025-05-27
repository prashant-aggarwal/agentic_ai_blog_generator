import os
from crewai import LLM
from dotenv import load_dotenv

class LLMInitializer:
    def __init__(self):
        load_dotenv()
        self.model_id = os.getenv("MODEL_ID")
        self.region = os.getenv("AWS_REGION_NAME")
        self.access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    def get_llm(self):
        return LLM(
            model=self.model_id,
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_region_name=self.region
        )
