import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

PG_HOST=os.getenv("PG_HOST")
PG_DB=os.getenv("PG_DB")
PG_USER=os.getenv("PG_USER")
PG_PASSWORD=os.getenv("PG_PASSWORD")

BQ_PROJECT=os.getenv("BQ_PROJECT")
