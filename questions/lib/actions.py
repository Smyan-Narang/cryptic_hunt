from datetime import datetime
import pytz

PUBLISH_DATE = datetime(year=2022, month=9, day=18, hour=0, minute=0, second=0)
DEACTIVATE_DATE = datetime(year=2022, month=10, day=3, hour=0, minute=0, second=0)
tz = pytz.timezone('Asia/Kolkata')
local_publish_date = tz.localize(PUBLISH_DATE)
local_deactivate_date = tz.localize(DEACTIVATE_DATE)
local_current_date = tz.localize(datetime.now())

def is_active_period():

    if ((local_current_date >= local_publish_date) and (local_current_date <= local_deactivate_date)):
        return True

    return False

def show_leaderboard():

    if local_current_date >= local_publish_date:
        return True

    return False
