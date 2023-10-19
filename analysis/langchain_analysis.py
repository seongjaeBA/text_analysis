import os
from dotenv import load_dotenv
import langchain

load_dotenv(dotenv_path='./env/.env')

scenario_gpt_secure = os.environ.get('ScenarioGpt')
scenario_llama_secure = os.environ.get('ScenarioLlama')
