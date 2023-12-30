FROM python:3.11 as python-base
WORKDIR /app

ENV MYSQL_DATABASE_URI="mysql://root:password@mysql/organizationdb"

COPY app /app
COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip
RUN pip install 'poetry==1.7.1'
RUN poetry install

CMD ["poetry", "run", "python", "-m", "flask", "--debug", "run", "--host=0.0.0.0"]