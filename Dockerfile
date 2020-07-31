FROM python:3
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD python -m src.dynamic_system
