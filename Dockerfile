FROM python:3

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
CMD ["python", "manage.py", "collectstatic", "--noinput", "&&", "gunicorn", "test_stripe.wsgi"]