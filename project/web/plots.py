import streamlit as st
import matplotlib.pyplot as plt

# Функція для кругової діаграми
def plot_pie_chart(data):
    # Розрахунок кількості елементів кожної категорії
    category_counts = data['Категорія'].value_counts()

    # Створення кругової діаграми
    plt.figure(figsize=(8, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Розподіл за категоріями')
    plt.axis('equal')  # Забезпечуємо, що кругова діаграма буде круглою
    st.pyplot()  # Відображення діаграми у Streamlit

def setData(data):
    st.header('Передбачення')
    print (data)