"""Seed database with sample data from CSV Files."""

from app import db
from models import User

db.drop_all()
db.create_all()

# Add user
user1 = User.signup(
  username = 'rain',
  password = 'qwerty',
)

db.session.add(user1)
db.session.commit()
