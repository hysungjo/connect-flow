from flask import render_template, url_for, flash, redirect, request, Blueprint

ap = Blueprint('ap', __name__)

@ap.route('/ap')
def frame(): 
    return render_template('ap.html')
