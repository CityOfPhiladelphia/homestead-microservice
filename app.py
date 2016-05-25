import flask
import cx_Oracle
from config import DSN, STMT

app = flask.Flask(__name__)
db = cx_Oracle.connect(DSN)
c = db.cursor()
c.prepare(STMT)

@app.route('/account/<account>')
def is_exempt(account):
    c.execute(None, {'account': account})
    row = c.fetchone()

    if row is None:
        flask.abort(404)

    resp = {
        'account':  account,
        'exempt':   bool(row[0]),
    }
    return flask.jsonify(**resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
