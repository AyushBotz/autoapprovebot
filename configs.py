from os import path, getenv

SUDO = "5822067254"

class Config:
    API_ID = int(getenv("API_ID", "24107399"))
    API_HASH = getenv("API_HASH", "80f574edc63f57434f788dddf3f350c1")
    BOT_TOKEN = getenv("BOT_TOKEN", "6173491393:AAFkL95vVKPKBIwZz8li31XaP0Yoz-xObb8")
    FSUB = getenv("FSUB", "assemblechat")
    CHID = int(getenv("CHID", "-1001631522563"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://seyam8267:5HQ6NC2FIxbbp9oV@cluster0.niwc9bl.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
