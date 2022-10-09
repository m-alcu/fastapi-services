# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY . /code/
# https://github.com/vishnubob/wait-for-it
RUN chmod +x /code/wait-for-it.sh
RUN pipenv install --system --dev

EXPOSE 8000