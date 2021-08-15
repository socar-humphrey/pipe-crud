from typing import List
import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"

    id: str = sa.Column(sa.String(), primary_key=True)
    title: str = sa.Column(sa.String())
    content: str = sa.Column(sa.String())
    user_id: str = sa.Column(sa.String(), sa.ForeignKey("users.id"))

    def __init__(self, id: str, title: str, content: str) -> None:
        self.id = id
        self.title = title
        self.content = content


class User(Base):
    __tablename__ = "users"

    id: str = sa.Column(sa.String(), primary_key=True)
    name: str = sa.Column(sa.String())
    password: str = sa.Column(sa.String())
    posts: List[Post] = sa.orm.relationship("Post")

    def __init__(self, id: str, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password

    def add_post(self, post: Post) -> None:
        self.posts.append(post)
