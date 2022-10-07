import random
from datetime import datetime
from pytz import timezone

class BasicFunctions:
    def __init__(self):
        self.none = ""

    def todays_date(self):
        central_tz = timezone('US/Central')
        loc_dt = datetime.today().astimezone(central_tz)
        today = loc_dt.strftime("%m/%d/%y")

        return today

    def form_at_user(self, user_id):
        at_user = "<@" + str(user_id) + ">"
        return at_user
