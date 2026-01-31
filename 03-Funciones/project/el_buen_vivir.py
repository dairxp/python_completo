import streamlit as st
import pandas as pd

def calcular_sub_total(nombre,precio,cantidad):
    subtotal=float(precio)*float(cantidad)

    nueva_fila={
        "producto":nombre, 
        "precio":precio, 
        "cantidad":cantidad, 
        "subtotal":subtotal}
    
    st.session_state.table_data=pd.concat(
            [st.session_state.table_data, pd.DataFrame([nueva_fila])],
            ignore_index=True
        )

if "table_data" not in st.session_state:
    st.session_state.table_data=pd.DataFrame(columns=["producto","precio","cantidad","subtotal"])

st.title("Supermercado El buen VIVIR")

with st.form("producto_form"):
    producto_nombre=st.text_input("Ingrese el nombre del producto")
    producto_precio=st.number_input("Ingrese precio del producto")
    producto_cantidad=st.number_input("Ingrese la cantidad del producto")

    subtotal_button=st.form_submit_button("Comprar Producto")

if subtotal_button:
    calcular_sub_total(producto_nombre, producto_precio, producto_cantidad)

st.dataframe(st.session_state.table_data)

if st.button("Calcular Total"):
    total=(st.session_state.table_data["precio"]*st.session_state.table_data["cantidad"]).sum()

    st.subheader("El precio total")
    st.write(f"El precio total es {total}")