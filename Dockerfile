FROM python:3.9-alpine
RUN apk --no-cache add musl-dev g++

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /Clarivate

WORKDIR /Clarivate
ENV PYTHONPATH="/Clarivate"
CMD ["python", "assignment/app.py"]
