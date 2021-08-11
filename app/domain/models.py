from typing import List


class Post:
    id: str
    name: str
    content: str
    user_id: str


class User:
    id: str
    name: str
    password: str
    posts: List[Post] = []

    def add_post(self, post: Post) -> None:
        self.posts.append(post)
