
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pandas as pd
import json

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    df = pd.read_csv('BTC_Prices.csv').drop(['Open', 'Adj Close','Volume'], axis=1).round(2)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)