#!/usr/bin/env python3
from ansible.errors import AnsibleFilterError
from passlib.hash import bcrypt


class FilterModule(object):

    def filters(self):
        return {
            "opensearch_bcrypt" : FilterModule.opensearch_bcrypt
        }

    @staticmethod
    def opensearch_bcrypt(password: str):
        if not isinstance(password, str):
            raise AnsibleFilterError("Input needs to be string but got:'{password}' with type:'{type(password)}'")
        return bcrypt.using(ident="2a", rounds=12).hash(password)

