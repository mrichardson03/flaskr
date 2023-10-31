from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr import db


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256), unique=True, nullable=False)
    password = Column(Text, nullable=False)

    post_relationship = relationship("Post", back_populates="user_relationship")

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def is_password_correct(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User: {self.username}>"


class Post(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    author_id = mapped_column(ForeignKey("user.id"))
    created = Column(DateTime(timezone=True), nullable=False)
    title = Column(Text, nullable=False)
    body = Column(Text, nullable=False)

    user_relationship = relationship("User", back_populates="post_relationship")

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created = datetime.now()

    def __repr__(self):
        return f"<Post: {self.title}>"
