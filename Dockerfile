FROM python:3.12

WORKDIR /app

COPY project/web /app/web/
COPY requirements_test.txt /app/requirements.txt
COPY project/main.py /app

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app/main.py"]