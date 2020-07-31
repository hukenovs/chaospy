FROM python:3
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r app/requirements.txt

ENTRYPOINT ["/bin/bash"]
CMD python -m app.src.dynamic_system.py
