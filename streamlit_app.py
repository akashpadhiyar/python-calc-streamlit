import streamlit as st
st.title("calculator")

n1 = st.number_input("Enter n1")
n2 = st.number_input("Enter n2")
col1, col2,col3,col4 = st.columns(4)

with col1:
    Sum = st.button("Sum")
with col1:
    Sub = st.button("Sub")
with col1:
    Mul = st.button("Mul")
with col1:
    Div = st.button("Div")

if Sum:
    ans = n1+n2
    st.text("Sum is {}.".format(ans))
if Sub:
    ans = n1-n2
    st.text("Sub is {}.".format(ans))
if Mul:
    ans = n1*n2
    st.text("Mul is {}.".format(ans))
if Div:
    ans = n1/n2

    st.text("Div is {}.".format(ans))
