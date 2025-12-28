from database.connection import DBConnection

class StockRepository:
    def upsert_financial(self, data):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO financial_analysis (code, name, sector, roe, per, pbr, debt_ratio, total_score)
            VALUES (%(code)s, %(name)s, %(sector)s, %(roe)s, %(per)s, %(pbr)s, %(debt_ratio)s, %(total_score)s)
            ON DUPLICATE KEY UPDATE roe=%(roe)s, total_score=%(total_score)s, updated_at=NOW()
        """
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

    def update_watch_list(self, code, base_price, target_price, days):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO watch_list (code, base_price, target_price, consecutive_days, last_update)
            VALUES (%s, %s, %s, %s, CURDATE())
            ON DUPLICATE KEY UPDATE consecutive_days=%s, last_update=CURDATE()
        """
        cursor.execute(sql, (code, base_price, target_price, days, days))
        conn.commit()
        cursor.close()
        conn.close()

    def get_active_watch_items(self):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM watch_list WHERE status='MONITORING'")
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res