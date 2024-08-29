import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib

df = pd.read_csv('project/data/internet_service_churn.csv')
target = 'churn' 
features = df.columns.drop(target)

# Модель
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model_path = 'project/models/decision_tree.pkl'
model = joblib.load(model_path)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Точність моделі: {accuracy:.2f}")

# Аналіз важливості параметрів

feature_importances = model.feature_importances_
sorted_idx = feature_importances.argsort()

plt.figure(figsize=(10, 6))
plt.barh(X.columns[sorted_idx], feature_importances[sorted_idx])
plt.xlabel("Важливість ознак")
plt.ylabel("Ознаки")
plt.title("Важливість ознак в Decision Tree")

st.pyplot(plt)

# Введення параметрів користувачем та прогнозування ймовірності відтоку
user_input = {}
for feature in features:
    value = st.number_input(f"Введіть значення для {feature}", value=0.0)
    user_input[feature] = value

if st.button("Розрахувати ймовірність відтоку"):
    input_df = pd.DataFrame([user_input])
    probability = model.predict_proba(input_df)[0][1]
    st.write(f"Ймовірність відтоку: {probability:.2f}")

# Завантаження CSV файлу для прогнозування
uploaded_file = st.file_uploader("Завантажте ваш файл CSV", type=["csv"])

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    
if all(col in user_data.columns for col in features):
    predictions = model.predict_proba(user_data)[:, 1]
    user_data['churn'] = predictions
    st.write("Результати прогнозування:")
    st.write(user_data)
