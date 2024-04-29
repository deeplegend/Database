import mysql.connector
import streamlit as st

conn =  mysql.connector.connect(host='localhost',username ="root",password = 'KJasdi@0924h',database = 'test')
my_cursor = conn.cursor()

name = st.text_input("Name",value=None)
pas = st.text_input("Password",value=None)
sub = st.button("Submit")

if sub:

    sqlFormula = "INSERT INTO user (name,password) VALUES (%s, %s)"
    student1 = (name,pas)

    my_cursor.execute(sqlFormula, student1)

    conn.commit()