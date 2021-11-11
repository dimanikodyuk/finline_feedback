from db.models import DeltaDB
from db.config import partner_conf
from resourses.requests import send_request
from logs.logs import logger_finline

if __name__ == "__main__":
    try:
        res = DeltaDB().finline_feedback()

        for row in res:
            send_request(row['lead_id'], row['status_name'], partner_conf['api_key'], partner_conf['partner_url'])

    except ValueError as err:
        logger_finline.error("Помилка даних main.py: " + str(err))
    except Exception as err:
        logger_finline.error("Помилка: " + str(err))
