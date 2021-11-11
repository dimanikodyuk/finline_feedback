import requests
import json
from db.models import DeltaDB
from logs.logs import log_file_handler, logger_finline

def send_request(p_lead_id, p_status, p_api_key, p_url):
    try:
        # -- Відправка POST методом
        logger_finline.info("-------------------------------------------------")
        url = p_url+f"?leadId={p_lead_id}&status={p_status}&apikey={p_api_key}"
        response = requests.request("GET", url=url, verify=False)
        logger_finline.info("URL: "+str(url))
        response_json = json.loads(response.text)
        logger_finline.info("RESPONSE: "+str(response_json))
        if response_json.get('result') is None:
            status = response_json['data']['status']
            if status == "200":
                DeltaDB().update_feedback(p_lead_id, 'True')
        else:
            DeltaDB().update_feedback(p_lead_id, response_json['result'])

    except ValueError as err:
        logger_finline.error("Помилка даних request.py (send_request): " + str(err))
    except KeyError as err:
        logger_finline.error("Помилка ключа request.py (send_request): " + str(err))
