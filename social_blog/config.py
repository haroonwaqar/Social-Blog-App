import os
password = os.environ.get('POSTGRES_PASS')

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{password}@localhost:5432/Social_Blog_db'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get('EMAIL_USER')
   MAIL_PASSWORD = os.environ.get('EMAIL_PASS')