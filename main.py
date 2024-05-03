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
  respuesta=f"El nombre del alumno es {fila.loc[:,'Nombre']}"
  return respuesta

print (PorNombre())

@app.route("/Por_Edad/<Edad>")
def PorEdad(Edad):
  resultados=base[base["Edad"]==Edad]
  Edad=int(Edad)
  resultados=str(resultados)
  return resultados

print (PorEdad())

@app.route("/Por_Estado/<Estado>")
def PorEstado(Estado):
  resultados=base[base["Estado"]==Estado]
  resultados=str(resultados)
  return resultados

print (PorEstado())

if __name__=="__main__":
  app.run()
