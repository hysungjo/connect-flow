from flask import render_template, url_for, flash, redirect, request, Blueprint

partners = Blueprint('partners', __name__)

@partners.route('/partners')
def find(): 
    return '<h1>partners</h1>'