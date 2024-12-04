from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from app.routes.routes import employees

load_dotenv()

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = f'{os.getenv('DATABASE_URL')}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
  Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  app.session = Session()

  app.register_blueprint(employees)
  
  CORS(app)

  return app