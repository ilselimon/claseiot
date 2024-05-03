import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("Alumnos de Hogwarts.xlsx")

@app.route("/")
def Principal():
    return "Esta es una Api que te muestra alumnos de Hogwarts"

@app.route("/Por_Alumno/<Alumno>")
def PorAlumno(Alumno):
  resultados=base[base["Alumno"]==Alumno]
  resultados=str(resultados)
  return resultados

@app.route("/Por_Nacimiento/<Nacimiento>")
def PorNacimiento(Nacimiento):
  Nacimiento=int(Nacimiento)
  resultados=base[base["Nacimiento"]==Nacimiento]
  resultados=str(resultados)
  return resultados

@app.route("/Por_Apellido/<Apellido>")
def PorApellido(Apellido):
  resultados=base[base["Apellido"]==Apellido]
  resultados=str(resultados)
  return resultados

@app.route("/Por_Casa/<Casa>")
def PorCasa(Casa):
  resultados=base[base["Casa"]==Casa]
  resultados=str(resultados)
  return resultados

if __name__=="__main__":
  app.run()
