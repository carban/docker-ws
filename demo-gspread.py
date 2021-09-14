import gspread
from flask import Flask, request, jsonify

app = Flask(__name__)
gc = gspread.service_account(filename="/workdir/key.json")
sh = gc.open("PGE-Flask-Docker")

@app.route("/")
def A1():
  if request.json:
    print(request.json['saludo'])
  return sh.sheet1.cell(1,1).value

@app.route("/obtenervalor",methods=['POST'])
def obtenervalor():
  row = request.json['row']
  col = request.json['col']
  return sh.sheet1.cell(row, col).value + "\n"

@app.route("/ponervalor", methods=['POST'])
def setvalue():
  row = request.json['row']
  col = request.json['col']
  val = request.json['val']
  sh.sheet1.update_cell(row, col, val)
  return "Updated cell ("+str(row)+","+str(col)+")" + "\n"

if  __name__ == '__main__':
  app.run(host='0.0.0.0')
