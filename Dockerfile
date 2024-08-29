FROM python:3.12

WORKDIR /app

COPY project/src /app/src/
COPY requirements_test.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "project/src/main.py"]