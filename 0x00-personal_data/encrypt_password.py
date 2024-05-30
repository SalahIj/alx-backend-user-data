#!/usr/bin/env python3
""" The imported modules """
import bcrypt


def hash_password(password: str) -> bytes:
    """The hash method"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """The valid method"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
