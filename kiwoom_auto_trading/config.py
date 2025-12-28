import os

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'stock_db',
    'pool_name': 'trading_pool',
    'pool_size': 5
}

STRATEGY = {
    'initial_weight': 0.10,      # 1단계 10%
    'second_weight': 0.07,       # 2단계 7%
    'additional_weight': 0.03,   # 3단계 이후 3%
    'noise_threshold': 0.05,     # 25일 노이즈 5% 이내
    'breakout_threshold': 1.05,  # 기준가 대비 +5%
    'volume_ratio': 2.0,         # 최근 20일 평균 대비 200%
    'consecutive_days': 3,       # 3거래일 확인
    'trailing_stop': 0.95        # 최고가 대비 -5% 시 매도
}

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)