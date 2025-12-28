class TradingCalculator:
    @staticmethod
    def calculate_noise(df):
        recent_25 = df.head(25)
        high = recent_25['고가'].max()
        low = recent_25['저가'].min()
        return (high - low) / low

    @staticmethod
    def get_volume_ratio(df):
        current_vol = df.iloc[0]['거래량']
        avg_vol_20 = df['거래량'].iloc[1:21].mean()
        return current_vol / avg_vol_20 if avg_vol_20 > 0 else 0