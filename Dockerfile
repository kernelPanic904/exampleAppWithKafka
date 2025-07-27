FROM python:3-alpine3.22

WORKDIR /project

ENV PYTHONPATH=/project/src

RUN apk upgrade --no-cache
RUN apk add build-base
RUN apk add zlib-dev

RUN pip install --upgrade pip

COPY . /project

RUN pip install .

ENTRYPOINT ["uvicorn", "--factory", "src.cli:get_application", "--host" "0.0.0.0" "--port" "8000" "--reload"]
