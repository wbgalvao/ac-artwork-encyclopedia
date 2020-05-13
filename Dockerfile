FROM python:3.6.10-alpine3.10 AS builder

RUN apk add --no-cache \
            --upgrade \
            gcc \
            musl-dev \
            postgresql-dev

WORKDIR /wheels
COPY ./requirements.txt /wheels/requirements.txt
RUN pip install -U pip \
   && pip wheel -r ./requirements.txt


FROM python:3.6.10-alpine3.10 AS final

RUN apk add --no-cache \
            --upgrade \
            gcc \
            musl-dev \
            postgresql-dev

COPY --from=builder /wheels /wheels
RUN pip install -U pip \
       && pip install -r /wheels/requirements.txt \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/* 

COPY . /app/
