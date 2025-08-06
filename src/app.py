# importar librerias

import streamlit as st  # manejo interactivo de pagina web 
from pickle import load 
import sklearn
import pandas as pd


st.title("Conjuto de datos con el cual se entreno el modelo ")
url = "https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv"
df = pd.read_csv(url)
st.dataframe(df)


# Cargar el modelo
"""
Esta función específica lee el flujo de bytes del objeto
 file (que debe ser un objeto de archivo abierto en modo
   binario de lectura, "rb") y lo transforma de nuevo en 
   su forma original, un objeto Python. 
"""
model = load(open("/workspaces/ml-streamlit/models/modelo.pkl", "rb"))

# hacer una lista con las categorias del target
class_dict = {
    "0": "Es probable que no tengas Diabetes :)",
    "1": "Creo que si tienes Diabetes mandate a revisar :("
}


# Colocar las variables por el usuario usando diferentes formas de input
st.title("¿Quisieras saber si tienes Diabetes? ")
st.subheader("Llena el siguiente formulario ")
#var1 = st.slider('Numero de Embarazos', min_value=0.0, max_value=15.0, step=1.0)
var1 = st.number_input('Número de embarazos', min_value=0, max_value=15, step=1)

var2 = st.text_input('Glucosa dos horas después de comer (mg/dL)', value="120")
var2 = float(var2) if var2 else 0.0

var3 = st.slider('Presión arterial diastólica (mm Hg)', 0.0, 150.0, 70.0, step=0.5)

var4 = st.number_input('Grosor del pliegue cutáneo en el tríceps (mm)', min_value=0.0, max_value=100.0, step=1.0)

var5 = st.text_input('Insulina sérica (mu U/ml)', value="80")
var5 = float(var5) if var5 else 0.0

var6 = st.slider('Indice de masa corporal [Peso(kg)/Estatura(m)**2]', min_value=0.0, max_value=80.0, step=0.1)


var7 = st.slider('¿Cuantos familiares con diabetes tienes?: 0-4 pon "0", 5-7 pon "0.5", 8 o más "1"', min_value=0.0, max_value=1.0, step=0.5)


var8 = st.radio("¿En qué rango de edad estás?", options=["21-35", "36-50", "51-65", "66+"])
edad_dict = {
    "21-35": 30,
    "36-50": 45,
    "51-65": 58,
    "66+": 70
}
var8 = edad_dict[var8]

# Cargar el modelo
if st.button("Realice Predicción"):
    prediction = str(model.predict([[var1, var2, var3, var4, var5, var6, var7, var8]])[0])
    pred_class = class_dict[prediction]
    st.success("Resultado para el modelo de regresión lineal:")
    st.write("Prediction:", pred_class)
    #
    # la precision del resultado 
    # resultados para otro 