FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN . .venv/bin/activate && pip3 install -r dev-requirements.txt

ENV PYTHONPATH=/app/src
CMD [ "python", "-m", "pytest", "tests"]
