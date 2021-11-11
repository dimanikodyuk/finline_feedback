from db.models import DeltaDB
from db.config import partner_conf
from resourses.requests import send_request

if __name__ == "__main__":
    res = DeltaDB().finline_feedback()

    for row in res:
        send_request(row['lead_id'], row['status_name'], partner_conf['api_key'], partner_conf['partner_url'])

