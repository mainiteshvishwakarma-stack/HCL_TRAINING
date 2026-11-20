
from flask import Flask, render_template, request

app = Flask(__name__)

# Restaurant Menu
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Sandwich": 100,
    "French Fries": 80,
    "Cold Coffee": 90,
    "Tea": 30,
    "Coke": 50,
    "Paneer Tikka": 200,
    "Dosa": 100
}

@app.route("/", methods=["GET", "POST"])
def home():
    bill_items = []
    subtotal = 0
    gst = 0
    grand_total = 0

    if request.method == "POST":

        for item, price in menu.items():

            quantity = request.form.get(item)

            if quantity:
                quantity = int(quantity)

                if quantity > 0:
                    total = price * quantity

                    bill_items.append({
                        "name": item,
                        "price": price,
                        "quantity": quantity,
                        "total": total
                    })

                    subtotal += total

        gst = subtotal * 0.05
        grand_total = subtotal + gst

    return render_template(
        "index.html",
        menu=menu,
        bill_items=bill_items,
        subtotal=subtotal,
        gst=gst,
        grand_total=grand_total
    )


if __name__ == "__main__":
    app.run(debug=True)
