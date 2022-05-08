from flask import render_template, url_for, flash, redirect, request, Blueprint

pservers = Blueprint('pservers', __name__)

@pservers.route('/pservers')
def frame(): 
    return render_template('pservers.html')