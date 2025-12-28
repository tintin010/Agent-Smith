from config import STRATEGY
from utils.calculator import TradingCalculator

class Trader:
    def __init__(self, repo, kiwoom):
        self.repo = repo
        self.kiwoom = kiwoom
        self.calc = TradingCalculator()

    def run_daily_trade_logic(self):
        items = self.repo.get_active_watch_items()
        for item in items:
            code = item['code']
            curr_p = self.kiwoom.get_current_price(code)
            df = self.kiwoom.get_ohlcv(code, "")
            v_ratio = self.calc.get_volume_ratio(df)

            # 가격 +5% 돌파 및 거래량 200% 확인
            if curr_p >= item['target_price'] and v_ratio >= STRATEGY['volume_ratio']:
                new_days = item['consecutive_days'] + 1
                if new_days >= STRATEGY['consecutive_days']:
                    print(f"🚀 {code} 최종 신호 발생! 매수 집행 루틴 실행")
                    # 여기에 실제 주문 및 portfolio 테이블 Insert 로직 추가
                else:
                    self.repo.update_watch_list(code, item['base_price'], item['target_price'], new_days)
            else:
                # 조건 이탈 시 카운트 리셋
                self.repo.update_watch_list(code, item['base_price'], item['target_price'], 0)