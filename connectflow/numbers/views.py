from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from connectflow import db

numbers = Blueprint('numbers', __name__)