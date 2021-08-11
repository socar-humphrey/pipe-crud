from app.domain.models import User, Post


def test_user_add_post():
    user = User(id="TEST", name="humphrey", password="password")
    user.add_post(post=Post(id="TEST", title="TITLE", content="123124214124124"))

    assert "TEST" in [post.id for post in user.posts]
