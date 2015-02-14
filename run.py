#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import g
from apps import app
import os

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.debug = True

base_path = os.path.abspath(os.path.dirname(__file__))


def connect_db():
    pass
    # return MySQLdb.connect(host='127.0.0.1', user='root', passwd='1qaz@WSX', db='journal', charset='utf8',
    #                        cursorclass=MySQLdb.cursors.DictCursor)


# def init_db():
#     with closing(connect_db()) as db:
#         for line in app.open_resource('schema.sql', mode='r'):
#             db.cursor().execute(line)
#         # with app.open_resource('schema.sql', mode='r') as f:
#         #     db.cursor().executescript(f.read())open('schema.sql', 'r')
#         db.commit()


@app.before_request
def before_request():
    pass
    #g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    #any exception, need close the db connect
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.after_request
def close_db(response):
    #finally, need close the db connect and return the response
    return response

if __name__ == '__main__':
    app.run()