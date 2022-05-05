from flask import render_template, url_for, flash, redirect, request, Blueprint

pservers = Blueprint('pservers', __name__)

@pservers.route('/pservers')
def find(): 
    return '<h1>pservers</h1>'