from finline_feedback.db.config import db
import pymssql
import datetime

class ConnectDB:
    def __init__(self, db_host, db_user, db_pass, db_name):
        self._db_host = db['host']
        self._db_user = db['user']
        self._db_pass = db['password']
        self._db_name = db['database']

    def __enter__(self):
        self._connect = pymssql.connect(self._db_host,
                                        self._db_user,
                                        self._db_pass,
                                        self._db_name,
                                        as_dict=True,
                                        )
        return self._connect

    def __exit__(self, exc_type, exc_val, ext_tb):
        self._connect.commit()
        self._connect.close()
        if exc_type:
            raise exc_type(exc_val)


class DeltaDB:
    def __init__(self):
        self._db_host = db['host']
        self._db_user = db['user']
        self._db_pass = db['password']
        self._db_name = db['database']

        # Оновлення токену

    def finline_feedback(self):
        now = datetime.datetime.now()
        p_dt = now.strftime("%Y-%m-%d")
        with ConnectDB(self._db_host, self._db_user, self._db_pass, self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC crm..feedback_finline %s;', p_dt)
            res = cursor.fetchall()
            return res

    def update_feedback(self, p_lead_id, p_status):
        with ConnectDB(self._db_host, self._db_user, self._db_pass, self._db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""update crm..partner_feedback set sended=1, dt_send=getdate(), dt_mod=getdate(),
                                partner_response='{p_status}' where lead_id = {p_lead_id} and sended=0;""")
            conn.commit()


