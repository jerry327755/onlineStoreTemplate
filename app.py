#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request, redirect, url_for
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global USERNAME, PRODUCTS, DB, SESSIONS, LOGGED_IN
USERNAME = 'default'
DB = Database('database/store_records.db')
PRODUCTS = DB.get_full_inventory()
SESSIONS = Sessions()
SESSIONS.add_new_session(USERNAME, DB)

def log_out():
    LOGGED_IN = False

log_out()

@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """


    return render_template('index.html', username=USERNAME, products=PRODUCTS, sessions=SESSIONS)

@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')

@app.route('/logout')
def logout_page():
    """
    Logs out the user, then redirects to index.

    args:
        - None

    returns:
        - None
    """
    log_out()
    return redirect(url_for('index_page'))

@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        SESSIONS.add_new_session(username, DB)
        logged_session()
        return render_template('home.html', products=PRODUCTS, sessions=SESSIONS)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html')

def logged_session():
    LOGGED_IN=True

@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    DB.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    checkout_info = []
    user_session = SESSIONS.get_session(USERNAME)
    for item in PRODUCTS:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)
            DB.set_item_stock(item['id'], item['stock'] - int(count))
            checkout_info.append({'item_name': item['item_name'], 'quantity': count, 'price': item['price'], 'total_price': item['price'] * int(count)})
        

    user_session.submit_cart()
    

    return render_template('checkout.html', order=order, sessions=SESSIONS, total_cost=user_session.total_cost, products=checkout_info)

@app.route('/home_filtered', methods=['POST'])
def filter_by_price():
    """
    Renders the home page when the user is at the '/' and '/home' endpoints, filters the products based on price.

    args:
        - None

    returns:
        - None
    """
    
    filtered_products = PRODUCTS    
    sort_order = request.form.get('sort')

    if sort_order == 'low_to_high':
        filtered_products.sort(key=lambda x: x['price'])
    elif sort_order == 'high_to_low':
        filtered_products.sort(key=lambda x: x['price'], reverse=True)
    if not LOGGED_IN:
        return render_template('index.html', username=USERNAME, products=filtered_products, sessions=SESSIONS)
    else:
        return render_template('home.html', username=USERNAME, products=filtered_products, sessions=SESSIONS)

@app.route('/Fruits')
def fruits_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    products=DB.get_items_by_category('Fruit')
    if not LOGGED_IN:
        return render_template('index.html', username=USERNAME, products=products, sessions=SESSIONS)
    else:
        return render_template('home.html', username=USERNAME, products=products, sessions=SESSIONS)
@app.route('/Vegetables')
def vegetables_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    products=DB.get_items_by_category('Vegetable')

    if not LOGGED_IN:
        return render_template('index.html', username=USERNAME, products=products, sessions=SESSIONS)
    else:
        return render_template('home.html', username=USERNAME, products=products, sessions=SESSIONS)
@app.route('/Seeds')
def seeds_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    PRODUCTS=DB.get_items_by_category('Seeds')

    if not LOGGED_IN:
        return render_template('index.html', username=USERNAME, products=PRODUCTS, sessions=SESSIONS)
    else:
        return render_template('home.html', username=USERNAME, products=PRODUCTS, sessions=SESSIONS)
@app.route('/Dairy')
def dairy_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    PRODUCTS=DB.get_items_by_category('Dairy')

    if not LOGGED_IN:
        return render_template('index.html', username=USERNAME, products=PRODUCTS, sessions=SESSIONS)
    else:
        return render_template('home.html', username=USERNAME, products=PRODUCTS, sessions=SESSIONS)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
