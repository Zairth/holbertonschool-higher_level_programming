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

@app.route('/products')
def products():
    error_msg = ""

    source = request.args.get("source", None)
    target_id = request.args.get("id", None)

    if source is None or source != "json" and source != "csv":
        return render_template('product_display.html', error_msg="Wrong source")

    if source == "json":
        try:
            with open("products.json", "r") as file:
                datas = json.load(file)

            if target_id is not None:
                for data in datas:
                    if data['id'] == int(target_id):
                        return render_template('product_display.html', datas=[data])
                return render_template('product_display.html', error_msg="Product not found")

            return render_template('product_display.html', datas=datas)

        except Exception as e:
            return render_template('product_display.html', error_msg=str(e))

    elif source == "csv":
        try:
            datas = []
            with open("products.csv", "r") as file:
                csv_datas = csv.DictReader(file)
                for row in csv_datas:
                    # row = {key.strip(): value.strip() for key, value in row.items()}  # 🔥 Nettoie les espaces
                    datas.append(row)

            if target_id is not None:
                for data in datas:
                    if data[' id'] == f" {target_id}":
                        return render_template('product_display.html', datas=[data])
                return render_template('product_display.html', error_msg="Product not found")

            return render_template('product_display.html', datas=datas, file=file)

        except Exception as e:
            return render_template('product_display.html', error_msg=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=5000)