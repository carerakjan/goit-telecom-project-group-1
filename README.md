# Структура проекту

```commandline
project/
│
├── data/
│   ├── internet_service_churn_updated.csv             # набір даних
│   ├── internet_service_churn.csv
│   └── ...
│
├── models/
│   ├── decision_tree.pkl                              # модель
│   ├── logistic_regression_model.pkl                  # модель
│   └── ...
│
├── notebooks/
│   ├── decision_tree.ipynb                            # ноутбук для decision_tree
│   ├── EDA.ipynb                                      # ноутбук для EDA
│   └── ...
│
├── web
│   ├── resources                                      # ресурси
│       ├── docs                                       # документи
│           └── Instructions_for_the_User.txt          # інструкція користувача
│       └── images                                     # зображення
│           └── logo.png                               # зображення лого
│   ├── tab                                            # кнопки
│       ├── multi_tab.py                               # прогнозування для множини
│       └── single_tab.py                              # одиночне прогнозування
│   ├── utils                                          # утіліти
│       ├── business_logic_for_processing_data.py      # бізнес-логіка
│       ├── load_model.py                              # загрузка моделей
│       └── ...                                        # скрипт для оцінки моделі
│   ├── app.py                                         # запуску Streamlit
│   ├── init_state.py                                  # керування сессією
│   └── ...
│
├── main.py                                            # стартовий файл
│
Dockerfile                                             # Dockerfile для створення образу
docker-compose.yml                                     # файл для Docker Compose
requirements.txt                                       # файли залежностей Python
README.md                                              # документація проекту
```

### Вимоги до версії Python: 3.12

Інструкція по запуску додатку:
* Створення віртуального оточення:<br>
`python -m venv .venv`

* Активація віртуального оточення:<br>
`.venv\Scripts\activate`
    * Windows:<br>
    `.venv\Scripts\activate`
    * Windows PowerShell:<br>
    `.\.venv\Scripts\Activate.ps1`
    * Mac OS:<br>
    `source .venv/bin/activate`

* Встановлення залежностей:<br>
`pip install -r requirements.txt`

* Запуск streamlit:<br>
`streamlit run project/src/main.py`



