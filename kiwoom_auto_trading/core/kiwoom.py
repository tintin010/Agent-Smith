from pykiwoom.kiwoom import Kiwoom
import time

class KiwoomWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.kiwoom = Kiwoom()
            cls._instance.kiwoom.CommConnect(block=True)
        return cls._instance

    def get_ohlcv(self, code, start_date):
        """일봉 데이터 가져오기"""
        df = self.kiwoom.block_request("opt10081", 
                                      종목코드=code, 
                                      기준일자=start_date, 
                                      수정주가구분=1, 
                                      output="주식일봉차트조회")
        # 데이터 전처리: 현재가, 고가, 저가 등을 양수로 변환
        cols = ['현재가', '고가', '저가', '거래량']
        df[cols] = df[cols].abs()
        return df

    def get_current_price(self, code):
        return abs(int(self.kiwoom.get_current_price(code)))