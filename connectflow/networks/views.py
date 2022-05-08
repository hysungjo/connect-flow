from flask import render_template, url_for, flash, redirect, request, Blueprint

networks = Blueprint('networks', __name__)

@networks.route('/networks')
def frame(): 
    return render_template('networks.html')