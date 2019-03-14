import os

from app import app
from flask import render_template, request, redirect, flash, url_for

from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from app.models.forms import InfoForm

@app.route("/")
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        return redirect(url_for("index"))
    return render_template("index.html",form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
