FROM python:3.9
WORKDIR /web
COPY . /web
RUN pip install -r requirements.txt
CMD ["python", "portal/manage.py", "runserver", "0.0.0.0:8000"]
