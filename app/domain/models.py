from typing import List


class Post:
    id: str
    title: str
    content: str
    user_id: str

    def __init__(self, id: str, title: str, content: str) -> None:
        self.id = id
        self.title = title
        self.content = content


class User:
    id: str
    name: str
    password: str
    posts: List[Post] = []

    def __init__(self, id: str, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password

    def add_post(self, post: Post) -> None:
        self.posts.append(post)
