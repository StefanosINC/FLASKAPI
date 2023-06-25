from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def view_home():
    return render_template("index.html")

@home_blueprint.route('/contacts')
def view_contacts():
    return render_template("contacts.html")

@home_blueprint.route('/features')
def view_features():
    return render_template("features.html")

@home_blueprint.route('/integrations')
def view_integrations():
    return render_template("integrations.html")

@home_blueprint.route('/pricing')
def view_pricing():
    return render_template("pricing.html")

