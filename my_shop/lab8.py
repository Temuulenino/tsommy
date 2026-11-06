from flask import Flask, render_template, abort

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Классик цамц", "price": 45000, "image": "shirt.svg", "description": "Өдөр тутмын өмсгөлд тохирох зөөлөн даавуун цамц. Размер: S, M, L, XL."},
    {"id": 2, "name": "Даавуун цүнх", "price": 28000, "image": "bag.svg", "description": "Ном, дэвтэр болон өдөр тутмын хэрэгслээ авч явах дахин ашиглах цүнх."},
    {"id": 3, "name": "Кофены аяга", "price": 22000, "image": "cup.svg", "description": "350 мл багтаамжтай керамик аяга. Халуун болон хүйтэн ундаанд тохиромжтой."},
]

@app.template_filter("money")
def money(value):
    return f"{value:,} ₮"

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/store")
def store():
    return render_template("store.html", products=PRODUCTS)

@app.route("/product")
@app.route("/product/<int:product_id>")
def product_detail(product_id=1):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template("product_detail.html", product=product)

@app.route("/cart")
def cart():
    # Удирдамжийн дагуу сагсны харагдах загвар: хадгалалт/төлбөргүй.
    return render_template("cart.html", product=PRODUCTS[0])

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
