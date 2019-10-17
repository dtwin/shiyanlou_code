# File Name?db.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)


class User(Base):  
    __tablename__ = 'user'  
    id = Column(Integer, primary_key=True) 
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


if __name__ == '__main__':
    # ??????? metadata ??? create_all ????????
    Base.metadata.create_all()
