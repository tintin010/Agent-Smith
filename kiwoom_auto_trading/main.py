import sys
from PyQt5.QtWidgets import QApplication
from core.kiwoom import KiwoomWrapper
from modules.scanner import Scanner
from modules.trader import Trader
from database.repository import StockRepository

def main():
    app = QApplication(sys.argv)
    
    # 싱글톤 API 연결
    kiwoom = KiwoomWrapper()
    repo = StockRepository()
    
    # 모듈 초기화
    scanner = Scanner()
    trader = Trader(repo, kiwoom)

    # 예시 실행: 기술적 필터링 후 감시
    # scanner.check_technical("005930")
    # trader.run_daily_trade_logic()

    print("시스템이 정상적으로 시작되었습니다.")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()