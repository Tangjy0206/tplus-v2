def generate_signal(df):

    close = df["收盘"]
    volume = df["成交量"]

    ma5 = close.rolling(5).mean().iloc[-1]
    ma10 = close.rolling(10).mean().iloc[-1]
    price = close.iloc[-1]

    if price > ma5 and volume.iloc[-1] > volume.mean() * 1.5:
        return {
            "price": round(price, 2),
            "ma5": round(ma5, 2),
            "ma10": round(ma10, 2),
            "signal": "🟢 LONG（可做T）"
        }

    elif price < ma10:
        return {
            "price": round(price, 2),
            "ma5": round(ma5, 2),
            "ma10": round(ma10, 2),
            "signal": "🔴 RISK（避免操作）"
        }

    else:
        return {
            "price": round(price, 2),
            "ma5": round(ma5, 2),
            "ma10": round(ma10, 2),
            "signal": "🟡 WAIT（观察）"
        }
      
