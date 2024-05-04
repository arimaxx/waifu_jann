class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6352061770"
    sudo_users = "6352061770", "6176582997"
    GROUP_ID = -1001939131996
    TOKEN = "7159220855:AAF8SMfMDgI3IQU0i1vObY5-mCNu42v_CGY"
    mongo_url = "mongodb+srv://sagar121:sagar121@sagar1.ql1togl.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "https://t.me/friendsgroupworld"
    UPDATE_CHAT = "https://t.me/animetubeworld"
    BOT_USERNAME = "gojosatoruriyabot"
    CHARA_CHANNEL_ID = "-1001939131996"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
