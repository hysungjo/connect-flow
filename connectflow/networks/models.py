from flask import render_template, url_for, flash, redirect, request, Blueprint

netowrks = Blueprint('netowrks', __name__)

@netowrks.route('/netowrks')
def find(): 
    return '<h1>netowrks</h1>'