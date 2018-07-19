# Example

import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'([A-Z]\w\w\w\w\w)([A-Z]\w\w\w\w\w\w)([A-Z]\w\w\w\w\w\w\w)([A-Z]\w\w\w\w\w\w\w\w)([A-Z]\w\w\w\w\w\w\w\w\w)([A-Z]\w\w\w\w\w\w\w\w\w\w)([A-Z]\w\w\w\w\w\w\w\w\w\w\w)')
        self.password_regex = re.compile(r'([a-z][a-z][a-z][a-z][a-z][a-z])+')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            error1 = re.compile(r'(\A[a-z])')
            if error1.search(username) is not None:
                print("Username format error! Your username is ",username)
                return False
            else:
                print("Password length error! Your password length is",len(username))
                return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            error = re.compile(r'[A-Z]')
            if error.search(password) is not None:
                print("Password format error! Your password is ",password)
                return False
            else:
                print("Password length error! Your password length is ",len(password))
                return False        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")

username,password = input().split(',')
print("Welcome,",username)

# Construct a object of type AuthSystem
auth = AuthSystem()

# authenticate the user's credentials
auth.authenticate(username,password)
