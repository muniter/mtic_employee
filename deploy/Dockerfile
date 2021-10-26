### Builder

FROM python:3.10-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies, to be copied to target.
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

### Target

FROM python:3.10-alpine as target

WORKDIR /usr/src/app

# Get the wheels from builder.
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*
RUN apk add make

# Copy the rest of the app
COPY . .

EXPOSE 5000
ENV FLASK_APP app
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV production

# Init the database with test data everytime.
CMD [ "make", "prod-init", "prod-run" ]
