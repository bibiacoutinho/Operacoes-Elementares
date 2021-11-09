from flask import Flask
from flask import render_template
from flask import request
from operacao import diferenca
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/soma', methods=['POST'])
def soma():
  n1 = float(request.form.get('n1'))
  n2 = float(request.form.get('n2'))
  return str(n1 + n2)

@app.route('/subt', methods=['POST'])
def subt():
  n1 = float(request.form.get('n1'))
  n2 = float(request.form.get('n2'))
  return str(diferenca(n1, n2))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5002)
