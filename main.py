import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.reas_excel("BasePokemon.xlsx")

@app.route("/")
def Principal():
    return "Esta es una Api que te muestra pokemons"

@app.route("/Por_Numero/<Numero>")
def PorNumero(Numero):
  Numero=int(Numero)
  fila=base[base["Numero"]==Numero]
  respuesta=f"El pokemon {Numero} es {fila.loc}"
  return respuesta

print (PorNumero(3))

@app.route("/Por_Tipo/<Tipo>")
def PorTipo(Tipo):
  resultados=base[base["Tipo"]==Tipo]
  resultados=str(resultados)
  return resultados

print (PorTipo(Planta))

@app.route("/Por_Peso/<Peso1>/<Peso2>")
def PorPeso(Peso1,Peso2):
  Peso1=float(Peso1)
  Peso2=float(Peso2)
  resultados=base[base["Peso"]<Peso]
  resultados=str(resultados)
  return resultados

print (PorPeso(30))
