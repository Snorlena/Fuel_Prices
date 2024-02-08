FROM python:3.8-alpine

WORKDIR /app

RUN pip install flask

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["flask_app.py" ]
