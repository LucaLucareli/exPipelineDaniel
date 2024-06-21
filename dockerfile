FROM python:latest
WORKDIR /exDaniel
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]