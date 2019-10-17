from flask import Flask
import functools
import dusk.settings as settings


app = Flask(__name__)

class DuskApp:
    @staticmethod
    def authenticate(email, password):
        

class Visitor:
    def __init__(self, label="Guest", role="Guest", logged_in=False):
        self.label = label
        self.role = role
        self.logged_in = logged_in

    def authenticate(self):
        ldap_mgr = lambda: True
        lux_empl = lambda: True
        global app

        try:
            assert(ldap_mgr())
        except AssertionError:
            try:
                assert(lux_empl())
            except AssertionError:


def current_user(function):
    """ Checks whether the current route has a
        user assigned to it; otherwise, it flags
        the function for processing a "guest"
        visitor and reroutes to the login page."""
    cookie = {}
    def wrapper(*args, **kwargs):
        

@app.route('/')
def hey():
    return "<h1>Hello World<h1>"
