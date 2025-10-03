from flask import Flask, render_template, url_for, jsonify
from dotenv import load_dotenv
import os
import stripe

load_dotenv()
app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY', 'Public key not found')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY', 'Secret key not found')

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"

    try:
        # Create new Checkout Session for the order
        checkout_session = stripe.checkout.Session.create(
            success_url=url_for('index', _external=True) + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=url_for('index', _external=True) + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": "price_1SEG2aJxpAHTvEfEOjiAomRd",
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403



@app.route('/config')
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
