import os
password = os.environ.get('POSTGRES_PASS')

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = f'postgresql://socialblogdb_user:{password}@dpg-d3a34bumcj7s73e3j11g-a/socialblogdb'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   #postgresql://postgres:{password}@localhost:5432/Social_Blog_db
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get('EMAIL_USER')
   MAIL_PASSWORD = os.environ.get('EMAIL_PASS')