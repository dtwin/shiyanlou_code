# File Name: create_data.py

from sqlalchemy.orm import sessionmaker
from faker import Faker
from db import Base, engine, User, Course

session = sessionmaker(engine)()
fake = Faker('zh-cn')

def create_users():
    for i in range(10):
        # ?? 10 ? User ?????? name ? email
        user = User(name=fake.name(), email=fake.email())
        # ?????? session ????????????
        # ?????? user ???? id ???
        # ??????????? 1 ???????? session ?????????
        session.add(user)

def create_courses():
    # session ?? query ??????????????????
    # all ??????????????????
    # user ??????? create_users ?? user ??
    for user in session.query(User).all():
        # ????????????????
        for i in range(2):
            # ???????name ??? 8 ?????
            course = Course(name=''.join(fake.words(4)), user_id=user.id)
            session.add(course)

def main():
    # ????????????session ??????????
    create_users()
    create_courses()
    # ?? session ? commit ?????????????????
    session.commit()

if __name__ == '__main__':
    main()
