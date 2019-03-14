import os

from app import app
from flask import render_template, request, redirect, flash, url_for,session

from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from app.models.forms import InfoForm

@app.route("/", methods=['POST','GET'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        #colocando o dado na sessão para mostralo na flash message
        session['breed'] = form.breed.data
        ftext =  'you change your breed for '+session['breed']
        flash(ftext)
        return redirect(url_for("index"))
    return render_template("index.html",form=form)

#pagina padrão de erro para url inválida
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
