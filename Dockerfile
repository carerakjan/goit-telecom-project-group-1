FROM python:3.12

WORKDIR /app

COPY /project .
COPY requirements_test.txt /app/requirements.txt
COPY /project/web/resources/images/logo.png /app/project/web/resources/images/logo.png
COPY /project/web/resources/docs/Instructions_for_the_User.txt /app/project/web/resources/docs/Instructions_for_the_User.txt

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py"]