class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6352061770"
    sudo_users = "6352061770", "6176582997"
    GROUP_ID = -1002079194692
    TOKEN = "7047990843:AAFxAKHcnF5JHCHoy9UG03e612-_aDCXgAs"
    mongo_url = "mongodb+srv://riyu:riyu@cluster0.kduyo99.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "https://t.me/riyadori"
    UPDATE_CHAT = "https://t.me/animetubeworld"
    BOT_USERNAME = "doreriyabot"
    CHARA_CHANNEL_ID = "-1002079194692"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
