import streamlit as st
from pickle import load
import sklearn

# Cargar el modelo
model = load(open("../models/modelo.pkl", "rb"))

# Clases
class_dict = {
    "0": "Es probable que no tengas Diabetes ",
    "1": "Creo que si tienes Diabetes ( 0 _ 0 )"
}


# Colocar las variables por el usuario
st.title("¿Tienes Diabetes? Dame la siguiente información :)")

var1 = st.slider('Numero de Embarazos', min_value=0.0, max_value=15.0, step=1.0)

var2 = st.slider('Glucosa dos horas despues de comer', min_value=0.0, max_value=300.0, step=0.1)

var3 = st.slider('Presion arterial. *Es el numero de abajo*', min_value=0.0, max_value=150.0, step=0.1)

var4 = st.slider('Grosor de la piel en el tricep. *Puedes inventarlo* (ㆆ _ ㆆ)', min_value=0.0, max_value=100.0, step=1.0)

var5 = st.slider('Insulina serica', min_value=0.0, max_value=900.0, step=1.0)

var6 = st.slider('Indice de masa corporal [Peso(kg)/Estatura(m)**2]', min_value=0.0, max_value=80.0, step=0.1)

var7 = st.slider('¿Cuantos familiares con diabetes tienes?: 0-4 pon "0", 5-7 pon "0.5", 8 o más "1"', min_value=0.0, max_value=1.0, step=0.5)

var8 = st.slider('Cual es tu edad', min_value=21, max_value=90, step=1)

# Cargar el modelo
if st.button("Predicción"):
    prediction = str(model.predict([[var1, var2, var3, var4, var5, var6, var7, var8]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)