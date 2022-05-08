from flask import render_template, url_for, flash, redirect, request, Blueprint

partners = Blueprint('partners', __name__)

@partners.route('/partners')
def frame(): 
    return render_template('partners.html')