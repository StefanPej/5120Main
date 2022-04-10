import csv
import pprint
import json
from datetime import datetime, timezone

with open("verified-2019_tweets.json", "r") as f:
    raw_data = json.load(f)

#pprint.pprint(raw_data[50]['user']['created_at'])

def get_age(account):

    """
    Finds
    """
    date_format = "%a %b %d %H:%M:%S %z %Y"

    created = datetime.strptime(raw_data[50]['user']['created_at'], date_format)
    now = datetime.now(timezone.utc)

    delta = now - created

    print(delta.days)
