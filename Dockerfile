FROM python:3.12-slim
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
