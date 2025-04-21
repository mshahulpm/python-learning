from database import SessionLocal
from models import User, Post, Comment
import logging

logging.getLogger("sqlalchemy").setLevel(logging.ERROR)


def main():
    db = SessionLocal()

    # db.query(User).delete()
    # db.query(Post).delete()

    user = User(name="Alice")
    db.add(user)
    db.commit()
    db.refresh(user)

    post = Post(title="First Post", content="Hello SQLAlchemy", user=user)
    db.add(post)
    db.commit()

    comment = Comment(content="New Comment 2", post_id=1, user_id=1)
    db.add(comment)
    db.commit()
    print(comment)

    db.query(Comment).filter(
        Comment.id == "fe4d9967-8bec-4525-a047-3fc7b66ef934"
    ).delete()
    db.commit()

    # Read posts
    posts = db.query(Post).limit(10)
    for p in posts:
        print(p.content)


if __name__ == "__main__":
    main()
