import os
import pymongo

from dotenv import load_dotenv


load_dotenv()


TOKEN = os.environ.get("DISCORD_TOKEN")
GOOGLE_CUSTOM_SEARCH_URI = os.environ.get("GOOGLE_CUSTOM_SEARCH_URI")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")
client = pymongo.MongoClient(
    "mongodb+srv://{user}:{password}@{cluster}/{db}?retryWrites=true&w=majority".format(
        user=os.environ.get("MONGO_USER"),
        password=os.environ.get("MONGO_PASSWORD"),
        cluster=os.environ.get("CLUSTER_URL"),
        db=os.environ.get("DB_NAME"),
    )
)
db = client[os.environ.get("DB_NAME")]
