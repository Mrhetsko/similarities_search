FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .





#EXPOSE 8000
# start server
#CMD python manage.py runserver 0.0.0.0:8000