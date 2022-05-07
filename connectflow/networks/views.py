from flask import render_template, url_for, flash, redirect, request, Blueprint

networks = Blueprint('networks', __name__)

@networks.route('/networks')
def find(): 
    return '<h1>networks</h1>'