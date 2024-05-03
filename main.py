import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("prueba.xlsx")

@app.route("/")
def Principal():
    return "Esta es una Api que te muestra alumnos"

@app.route("/Por_Nombre/<Nombre>")
def PorNombre(Nombre):
  fila=base[base["Nombre"]==Nombre]
  resultados=str("El nombre del alumno es {fila.loc[:,'Nombre']}")
  return resultados

@app.route("/Por_Edad/<Edad>")
def PorEdad(Edad):
  Edad=int(Edad)
  resultados=base[base["Edad"]==Edad]
  resultados=str(resultados)
  return resultados

@app.route("/Por_Estado/<Estado>")
def PorEstado(Estado):
  resultados=base[base["Estado"]==Estado]
  resultados=str(resultados)
  return resultados

if __name__=="__main__":
  app.run()
