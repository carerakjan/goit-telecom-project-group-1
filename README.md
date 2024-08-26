# Структура проекту

```commandline
project/
│
├── data/
│   ├── internet_service_churn_updated.csv       # набір даних
│   └── internet_service_churn.csv
│
├── notebooks/
│   ├── EDA.ipynb               # ноутбук для EDA
│   ├── Preprocessing.ipynb     # ноутбук для попередньої обробки даних
│   └── ...
│
├── src/
│   ├── data_preparation.py     # скрипт для обробки даних
│   ├── model_training.py       # скрипт для тренування моделі
│   ├── model_evaluation.py     # скрипт для оцінки моделі
│   └── ...
│
├── models/
│   ├── trained_model.pkl       # збережена модель
│   └── ...
│
├── Dockerfile                  # Dockerfile для створення образу
├── docker-compose.yml          # файл для Docker Compose
├── requirements.txt            # файли залежностей Python
└── README.md                   # документація проекту
```

## Версія Python 3.12.1

Відкрийте термінал або командний рядок і виконайте наступну команду для створення віртуального середовища. У цьому прикладі ми назвемо наше середовище `venv`:

команда `python -m venv .venv`

Наприклад 
`PS E:\work\repoGIt\goit-telecom-project-group-1> python -m venv .venv`

Активуйте віртуальне середовище:
`.venv\Scripts\activate`

Наприклад: 
`PS E:\work\repoGIt\goit-telecom-project-group-1> .venv\Scripts\activate`

Встановіть залежності з `requirements.txt`:
`pip install -r requirements.txt`

Наприклад:
`(.venv) PS E:\work\repoGIt\goit-telecom-project-group-1> pip install -r requirements.txt`



