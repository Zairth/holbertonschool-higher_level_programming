from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    with open('items.json', "r") as file:
        json_data = json.load(file)
    items = json_data.get('items')

    return render_template('items.html', items=items)

@app.route('/product_display')
def product_display():
    error_msg = ""

    source = request.args.get("source", None)
    target_id = request.args.get("id", None)

    if source is None or source != "json" and source != "csv":
        error_msg = "Wrong source"
        return render_template('product_display.html', error_msg=error_msg)

    if source == "json":
        try:
            with open("products.json", "r") as file:
                datas = json.load(file)

            if target_id is not None:
                for data in datas:
                    if data['id'] == int(target_id):
                        return render_template('product_display.html', data=data)
                error_msg = "Product not found"
                return render_template('product_display.html', error_msg=error_msg)

            return render_template('product_display.html', datas=datas)

        except Exception as e:
            exception = True
            return render_template('product_display.html', error_msg=str(e), exception=exception)

    elif source == "csv":
        try:
            file = open("products.csv", "r")
            datas = csv.DictReader(file)

            if target_id is not None:
                for data in datas:
                    if data['id'] == int(target_id):
                        return render_template('product_display.html', data=data, file=file)
                error_msg = "Product not found"
                return render_template('product_display.html', error_msg=error_msg, file=file)

            return render_template('product_display.html', datas=datas, file=file)

        except Exception as e:
            exception = True
            return render_template('product_display.html', error_msg=str(e), exception=exception, file=file)


if __name__ == '__main__':
    app.run(debug=True, port=5000)