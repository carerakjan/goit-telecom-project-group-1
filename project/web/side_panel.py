import streamlit as st

@st.dialog("Instruction", width="large")         
def inst():
    with open('project/web/resources/docs/Instructions_for_the_User.txt', 'r', encoding='utf-8') as file:
      instructions = file.read()
      st.write(instructions)

def base():
    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Повернутися на головну 🏠"):
        pass
     # Кнопка "Повернутися на головну"
    if st.sidebar.button("Інструкція користування 📄"):
        inst()

    # Кнопка "Оновити"
    if st.sidebar.button("Оновити 🔄"):
       
        pass


