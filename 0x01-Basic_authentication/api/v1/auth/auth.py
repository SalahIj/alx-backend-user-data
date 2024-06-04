#!/usr/bin/env python3
"""
Module for authentication
"""
from typing import List, TypeVar

from flask import request


class Auth():
    """the class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The path definition"""
        if not path:
            return True
        if not excluded_paths:
            return True
        path = path.rstrip("/")
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and \
                    path.startswith(excluded_path[:-1]):
                return False
            elif path == excluded_path.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """the function"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """the current function"""
        return None
