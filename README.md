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

## Версія Python 3.12

Відкрийте термінал або командний рядок і виконайте наступну команду для створення віртуального середовища. У цьому прикладі ми назвемо наше середовище `venv`:

команда `python -m venv .venv`

Наприклад 
`PS E:\work\repoGIt\goit-telecom-project-group-1> python -m venv .venv`

Активуйте віртуальне середовище:
`.venv\Scripts\activate`

Наприклад Win OS: 
`PS E:\work\repoGIt\goit-telecom-project-group-1> .venv\Scripts\activate`

Наприклад Mac OS: 
`PS E:\work\repoGIt\goit-telecom-project-group-1> source .venv/bin/activate`

Встановіть залежності з `requirements.txt`:
`pip install -r requirements.txt`

Наприклад:
`(.venv) PS E:\work\repoGIt\goit-telecom-project-group-1> pip install -r requirements.txt`

Запустити streamlit 
`streamlit run project/src/main.py`

Наприклад:
`(.venv) PS E:\work\repoGIt\goit-telecom-project-group-1> streamlit run project/src/main.py`



