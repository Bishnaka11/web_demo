import streamlit as st
st.title("welcome to Bishanka Electric")
st.header('Creat your home smart')
st.subheader("Contact :- 8617636499")
st.markdown('House & bulding wiring, Repairing & maintainced')
st.markdown('We provide all types of electric service')
Name = st.text_input("Enter Your Name: ")
Mobile = st.text_input("Enter Your Mobile no: ")
address = st.text_input("Enter Your Address ")
Problem = st.text_area("Enter Your Text: ")
Type_of_work = st.selectbox("Types of work", ('Select one', 'repairing', 'wiring', 'Bouth' ))
Button = st.button("Submit")
if Button :
    st.markdown(f"""
        Name : {Name} 
        Mobile : {Mobile} 
        address : {address} 
        Problem : {Problem} 
        Type : {Type_of_work}""")
