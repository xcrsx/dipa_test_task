FROM python:3.9.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /usr/src/dipa_task

COPY pyproject.toml /usr/src/dipa_task/

RUN pip3 install poetry

RUN poetry config virtualenvs.create false \
&& poetry install

COPY . /usr/src/dipa_task/
