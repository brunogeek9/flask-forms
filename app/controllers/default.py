import os

from app import app
from app import db
from flask import render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models.tables import Book

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listbooks")
def listbooks():
    books = Book.query.all()
    app.jinja_env.filters['page_title'] = "listbooks"
    return render_template("listbooks.html",books=books)

@app.route("/cadbook",methods=["GET", "POST"])
def cadbook():
    if request.form:
        book = Book(
            title=request.form.get("title"),
            number_of_pages = request.form.get("numberpages"),
            rate = request.form.get("rate")
        )   
        db.session.add(book)
        db.session.commit()
        flash('Cadastro efetuado com sucesso')
        return redirect(url_for('cadbook'))

    return render_template("cadbook.html")

@app.route("/editbook", methods=["GET","POST"])
def editbook():
    try:
        newtitle=request.form.get("title")
        newnpages = request.form.get("numberpages")
        newrate = request.form.get("rate")
        id = request.form.get("id")
        book = Book.query.filter_by(id=id).first()
        print(newtitle)
        print(book.title)
        book.title = newtitle
        book.number_of_pages = newnpages
        book.rate = newrate
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")
    

@app.route("/modifybook", methods=["GET","POST"])
def modifybook():
    id = request.form.get("id")
    mode = request.form.get("mode")
    print(id)
    print(mode)
    book = Book.query.filter_by(id=id).first()
    if mode == "delete":
        flash('Livro ' +book.title+ ' deletado com sucesso')
        db.session.delete(book)
        db.session.commit()
        
        return redirect("/listbooks")
    else:
        return render_template("/cadbook.html",book=book)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
