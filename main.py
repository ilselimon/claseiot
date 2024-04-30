# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route("/")
def Hola_mundo():
  return "Esta API te ayudará a sumar, restar, multiplicar y dividr"

@app.route("Suma/<numerouno>/<numerodos>")
def Multiplicacion(numerouno, numerodos):
  Resultado=int(numerouno)*(numerodos)
  return f"El resultado es {Resultado}"

if __name__=="__main__":
  app.run()
