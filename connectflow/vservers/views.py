from flask import render_template, url_for, flash, redirect, request, Blueprint

vservers = Blueprint('vservers', __name__)

@vservers.route('/vservers')
def find(): 
    return '<h1>vservers</h1>'