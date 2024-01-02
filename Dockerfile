FROM python:3.9-slim as base
WORKDIR /app

ENV MYSQL_DATABASE_URI="mysql://root:password@mysql/organizationdb"

RUN apt-get update
RUN apt-get install gcc pkg-config python3-dev default-libmysqlclient-dev  -y

COPY app /app
COPY poetry.lock pyproject.toml ./
RUN python -m pip install --upgrade pip
RUN pip install 'poetry==1.7.1'
RUN poetry install

CMD ["poetry", "run", "python", "-m", "flask", "--debug", "run", "--host=0.0.0.0"]