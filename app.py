from flask import Flask, render_template, url_for, jsonify, redirect
from dotenv import load_dotenv
import os
import stripe

load_dotenv()
app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY', 'Public key not found')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY', 'Secret key not found')
price_key = os.getenv('STRIPE_PRICE_KEY', 'Price key not found')

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')


@app.route("/create-checkout-session", methods=['POST'])
def create_checkout_session():
    try:
        # Create new Checkout Session for the order
        checkout_session = stripe.checkout.Session.create(
            success_url=url_for('success', _external=True),
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": price_key,
                    "quantity": 1,
                }
            ]
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 403



@app.route('/config')
def get_publishable_key():
    stripe_config = {"publicKey": app.config['STRIPE_PUBLIC_KEY']}
    return jsonify(stripe_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
