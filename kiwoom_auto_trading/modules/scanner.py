from core.kiwoom import KiwoomWrapper
from utils.calculator import TradingCalculator
from database.repository import StockRepository
from config import STRATEGY

class Scanner:
    def __init__(self):
        self.kiwoom = KiwoomWrapper()
        self.repo = StockRepository()
        self.calc = TradingCalculator()

    def check_technical(self, code):
        df = self.kiwoom.get_ohlcv(code, "")
        if len(df) < 180: return False
        
        noise = self.calc.calculate_noise(df)
        if noise <= STRATEGY['noise_threshold']:
            current_p = self.kiwoom.get_current_price(code)
            # watch_list에 추가 (base_price는 현재가로 설정)
            self.repo.update_watch_list(code, current_p, current_p * 1.05, 0)
            return True
        return False