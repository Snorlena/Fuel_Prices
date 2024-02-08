FROM python:3.10

WORKDIR /app

RUN pip install flask requests

COPY . /app

ENTRYPOINT [ "python3" ]

CMD ["flask_app.py" ]
