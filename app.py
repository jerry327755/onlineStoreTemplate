#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request, redirect, url_for, session
from core.session import Sessions

app = Flask(__name__)
app.secret_key = '\x14*\xbax&\x97\xe8\xa9\xd0\xa6-\xa3\xa6\xee\xc4\xebt\x9c\x9b\xce\xf1\xe2\xa9\xbf'
HOST, PORT = 'localhost', 8080
global username, products, db, sessions, logged_in
username = 'default'
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)


def log_out():
    global logged_in
    global username
    username = "default"
    logged_in = False


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

    if logged_in:
        return render_template('home.html', username=username, products=products, sessions=sessions)
    
    return render_template('index.html', username=username, products=products, sessions=sessions)


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
    session.pop('username', None)
    return redirect(url_for('index_page'))


@app.route('/dashboard')
def dashboard():
    """
    If the user is logged in, shows account dashboard. Otherwise, redirects to index.

    args:
        - None

    returns:
        - None
    """

    if logged_in:
        return render_template('dashboard.html', username=session['username'])
    else:
        print("Attempted to access account dashboard while not logged in, redirecting...")
        return redirect(url_for('index_page'))

@app.route('/dashboard', methods=['POST'])
def reset_password():
    """
    Handles reset password request.

    modifies:
        - passwords.txt: updates user password hash/salt
        - database: updates user password hash on success.
    """

    if not logged_in:
        print("Error, tried to reset password while not logged in.")
        return redirect(url_for('index_page'))
    else:
        username = session['username']
        old_password = request.form['prev-password']
        new_password = request.form['new-password']
        if login_pipeline(username, old_password):
            print(f"Updating password for user {username}")
            salt, key = hash_password(new_password)
            update_passwords(username, key, salt)
            db.set_password_hash(username, key)
            return render_template('dashboard.html', username=username, successful_reset=True)
        else:
            print("Error, tried to reset password, but gave incorrect current password.")
            return render_template('dashboard.html', username=username, failed_reset=True)

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
    session['username'] = username
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        logged_session()
        print(f"Logged in as user: {username}")
        return render_template('home.html', products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html')


def logged_session():
    global logged_in
    logged_in=True



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
    global username 
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
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
    user_session = sessions.get_session(username)
    if products == 0:
        user_session.empty_cart()
        print("we emptied cart")
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)
            db.set_item_stock(item['id'], item['stock'] - int(count))
            checkout_info.append({'item_name': item['item_name'], 'quantity': count, 'price': item['price'], 'total_price': item['price'] * int(count)})
        

    user_session.submit_cart()
    user_session.cart= user_session.empty_cart()


    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost, products=checkout_info)


@app.route('/home_filtered', methods=['POST'])
def filter_by_price():
    """
    Renders the home page when the user is at the '/' and '/home' endpoints, filters the products based on price.

    args:
        - None

    returns:
        - None
    """
    
    filtered_products = products    
    sort_order = request.form.get('sort')

    if sort_order == 'low_to_high':
        filtered_products.sort(key=lambda x: x['price'])
    elif sort_order == 'high_to_low':
        filtered_products.sort(key=lambda x: x['price'], reverse=True)
    if not logged_in:
        return render_template('index.html', username=username, products=filtered_products, sessions=sessions)
    else:
        return render_template('home.html', username=username, products=filtered_products, sessions=sessions)

@app.route('/Fruits')
def fruits_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    global products
    products=db.get_items_by_category('Fruit')
    if not logged_in:
        return render_template('index.html', username=username, products=products, sessions=sessions)
    else:
        return render_template('home.html', username=username, products=products, sessions=sessions)

@app.route('/Vegetables')
def vegetables_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    global products
    products=db.get_items_by_category('Vegetable')

    if not logged_in:
        return render_template('index.html', username=username, products=products, sessions=sessions)
    else:
        return render_template('home.html', username=username, products=products, sessions=sessions)
@app.route('/Seeds')
def seeds_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    global products
    products=db.get_items_by_category('Seeds')

    if not logged_in:
        return render_template('index.html', username=username, products=products, sessions=sessions)
    else:
        return render_template('home.html', username=username, products=products, sessions=sessions)
@app.route('/Dairy')
def dairy_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    global products
    products=db.get_items_by_category('Dairy')

    if not logged_in:
        return render_template('index.html', username=username, products=products, sessions=sessions)
    else:
        return render_template('home.html', username=username, products=products, sessions=sessions)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
