FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.in .
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.in

COPY basic-flask-project/ basic-flask-project/

RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

CMD ["python", "basic-flask-project/app.py"]
