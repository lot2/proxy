#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/')
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("index.html", title='Home')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html", title='Login')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/session')
def get_all_session():
    return  render_template("get_sessions.html")


@app.route('/outdate')
def outdate():
    return  render_template("outdate.html")


@app.route('/login2')
def login2():
    return  render_template("login2.html")