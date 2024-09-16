import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22526551"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4eb7c5fd1c3c3fb63d9b40f1a90eec98")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb://rohitgolu836:<db_hzJU3ACjWbfuTAyZ>@<hostname>/?ssl=true&replicaSet=atlas-ia5bdj-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
