#!/usr/bin/env python3
"""The imported modules"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """The class definition"""

    def __init__(self) -> None:
        """init method"""
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """The session method"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """The add user method"""
        session = self._session
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            session.add(new_user)
            session.commit()
        except Exception:
            session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """The find user method"""
        attrs, vals = [], []
        for attr, val in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError()
            attrs.append(getattr(User, attr))
            vals.append(val)

        session = self._session
        query = session.query(User)
        user = query.filter(tuple_(*attrs).in_([tuple(vals)])).first()
        if not user:
            raise NoResultFound()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """The update method"""
        user = self.find_user_by(id=user_id)
        session = self._session
        for attr, val in kwargs.items():
            if not hasattr(User, attr):
                raise ValueError
            setattr(user, attr, val)
        session.commit()
