import streamlit as st


st.title("Power Calculator")
st.write("Enter a number to find out the square,cube and fifth power")

n=st.number_input("Enter an integer", value=1, step=1)

square = n**2
cube = n**3
fifth = n**5

st.write(f"the square of {n} is {square}")

st.write(f"the cube of {n} is {cube}")
st.write(f"the fifith of {n} is {fifth}")

