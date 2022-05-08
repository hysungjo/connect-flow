from flask import render_template, url_for, flash, redirect, request, Blueprint

numbers = Blueprint('numbers', __name__)

@numbers.route('/numbers')
def frame(): 
    return render_template('numbers.html')