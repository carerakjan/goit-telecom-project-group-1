FROM python:3.12-slim

# Встановлюємо необхідні системні залежності
RUN apt-get update && apt-get install -y \
    build-essential

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо файли застосунку у контейнер
COPY . /app

# Встановлюємо залежності з requirements.txt
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Виставляємо порт
EXPOSE 8501

# Команда запуску Streamlit
CMD ["streamlit", "run", "project/main.py", "--server.port=8501", "--server.enableCORS=false"]