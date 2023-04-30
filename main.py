
from flask import Flask
import cx_Oracle
from flask import request, escape

my_db = cx_Oracle.connect('sys/oracle@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)
app = Flask(__name__)
 
# Creating connection object
@app.route("/recomandari")
def recomandari():
    recomanadri = "Fara recomandari"
    with my_db.cursor() as my_cursor:
        my_cursor.execute("select * from recomandari_st")
        recomanadri = str(my_cursor.fetchall())
    return recomanadri

@app.route("/saloane")
def saloane():
    recomanadri = "Fara recomandari"
    with my_db.cursor() as my_cursor:
        my_cursor.execute("select * from saloane_st")
        recomanadri = str(my_cursor.fetchall())
    return recomanadri

@app.route("/")
def get_salon_from_judet():
    judet = str(escape(request.args.get("judet", "")))
    return ("""<form action="" method="get">
                <input type="text" name="judet">
                <input type="submit" value="Submit">
              </form>""" + judet + get_saloane(judet))


def get_saloane(judet):
    recomanadri = "Fara recomandari"
    with my_db.cursor() as my_cursor:
        qr = "select * from saloane_st where judet='" +judet+"'"
        my_cursor.execute(qr)
        print("hi")
        recomanadri = str(my_cursor.fetchall())
        print(recomanadri)
    return recomanadri


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)