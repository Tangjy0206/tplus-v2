# tplus-v2
flask
akshare
pandas
from flask import Flask, render_template, request
import akshare as ak
from core.signal import generate_signal

app = Flask(__name__)

def get_data(symbol):
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily", adjust="qfq")
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    symbol = None

    if request.method == "POST":
        symbol = request.form["symbol"]
        df = get_data(symbol)
        result = generate_signal(df)

    return render_template("index.html", result=result, symbol=symbol)

if __name__ == "__main__":
    app.run(debug=True)
    
