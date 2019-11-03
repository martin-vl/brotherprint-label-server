# app.py
from flask import Flask, request
from brotherprint import BrotherPrint
import socket

printerIP = '192.168.2.21'
app = Flask(__name__)

@app.route('/storagelabel')
def storagelabel():
  tempNumber = 1
  box = request.args.get('box')
  barcode = request.args.get('barcode')
  name = request.args.get('name')

  f_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  f_socket.connect((printerIP, 9100))
  printjob = BrotherPrint(f_socket)
  printjob.template_mode()
  printjob.template_init()
  printjob.choose_template(tempNumber)
  printjob.select_and_insert('box', box)
  printjob.select_and_insert('barcode', barcode)
  printjob.select_and_insert('name', name)
  printjob.template_print()

  return '''<h1>Printing storage label</h1>
            <p>Box: {}<br>
            Barcode: {}<br>
            Name: {}</p>'''.format(box,barcode,name)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
