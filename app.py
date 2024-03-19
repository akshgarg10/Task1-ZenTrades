from flask import Flask, render_template, send_file
from data_fetch import data_fetch

app = Flask(__name__)

@app.route('/')
def index():
    try:
        products = data_fetch()
        
        sorted_products = sorted(products, key=lambda x: int(x.get('popularity', 0)), reverse=True) #sortted decreasingly
        return render_template('index.html', products=sorted_products)
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)