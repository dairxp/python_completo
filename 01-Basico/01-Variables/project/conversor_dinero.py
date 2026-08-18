#1. ingresar cantidad doalres
#2 Reazlair formula matematioca para convertir  a euros
#3 Imprimir el resutlado en consola

import streamlit as st
st.title("Conversor de dolares a euros")

dolares=st.number_input("ingrese cantidad de doalres")

euros=dolares*2
euros=str(euros)
st.button("Procesar", on_click=print("Aqui se imprimira el resultado: " + euros))