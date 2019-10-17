from flask import Flask
import functools
import dusk.settings as settings
import sqlite3
import collections
import datetime

# The global app instance:
app = Flask(__name__)

class LoginException(Exception):
    def __init__(self, error):
        self.error = error
    def __raise__(self):
        global app
        print(self)
        return app.route('/login')
    def __str__(self):
        return self.error

# A namespace of immutable user-data:
class Operative:
    """Operative"""
    _params = ["email", "password", "first",
            "last", "phone_primary",
            "phone_secondary", "isManager"]

    @classmethod
    def __session__(cls, db_response):
        try:
            # Should always fail the first assertion
            # with valid fields. This test checks for
            # empty lists '[]' as the return.
            assert len(db_response > 0)
            try:
                db_response = db_response[0]
                return Operative.__factory__(*db_response)
            except TypeError:
                raise(TypeError, "Something horribly wrong has happened. What did you even do?")
        except AssertionError:
            # Return a 'Guest' user
            return cls.__factory__(['None', 'None', 'Guest', '', 'None', 'None', 'False'])


    @classmethod
    def __factory__(cls, *db_response):
        try:
            
        try:
            assert len(field == len(cls._params))
            operative_dict = {}
            for slice_no in range(len(cls._params)):
                operative_dict[cls._params[slice_no]] = db_response[slice_no]
            return cls.__init__(**operative_dict)

        except AssertionError:
            loginexc = LoginException("\
                    The LDAP server did not respond\
                    before timing out. Re-routing \
                    back to the home page.")
            return raise(loginexc)
    
    def __init__(self, **kwargs):
        """ """
        self.email = None
        self.password = None
        self.first = None
        self.last = None
        self.phone_primary = None
        self.phone_secondary = None
        self.isManager = None
        self._login_time = datetime.datetime.now()
        self.__dict__.update(kwargs)

    def __fields__(self):
        """ Returns a tuple of the self's fields """
        return tuple([self.__dict__[_] for _,__ in self.__dict__.items()])

    @property
    def session_token(self):
        """ """
        flds = self.__fields__()
        tokenator = lambda F: f"#{hash(*F):02x}"
        return tokenator(flds)

        operative = collections.namedtuple(
    'Operative',
    [
        'email',
        'password',
        'first',
        'last',
        'phone_primary',
        'phone_secondary',
        'isManager'
    ]
)

class DuskApp:
    """app.DuskApp: A module for low-security authentication
    
    METHODS
    -------
    DuskApp.authenticate(email, password) -> Operative(...)

    """
    @staticmethod
    def authenticate(email="None", password="None"):
        """app.DuskApp.authenticate(route_function) -> 
        Operative(email, password, first, last,phone_primary, phone_secondary, isManager)
        
        This function authenticates against a SQLite database,
        should probably not be called directly,
        and should also probably not exist for longer than 6 months.
        Ideally, another decorator from the DuskApp module should 
        wrap around an `app.route('/path')` call and be stored as
        a backend-server cookie.
        """
   	    def login_logic():
            db = sqlite3.connect("auth_demo.db")
            query = db.execute(f'SELECT * FROM operative WHERE email="{email}" AND password="{password}";')
            db_response = query.fetchall()
            db_response = login_logic()
            try:
                # Should always fail the first assertion
                # with valid fields. This test checks for
                # empty lists '[]' as the return.
                assert len(db_response > 0)
                try:
                    db_response = db_response[0]
                    return operative(*db_response)
                except TypeError:
                    raise(TypeError, "Something horribly wrong has happened. What did you even do?")
            except AssertionError:
                # Return a 'Guest' user
                return operative('None', 'None', 'Guest', '', 'None', 'None', 'False')
        return login_logic()
	
    @staticmethod
    def session(function):
        """DOCSTRING"""
        user_sessions = {}

        @functools.wraps(function)
        def wrapper(*args, email="None", password="None", **kwargs):
            nonlocal user_sessions
            route_call = (args, tuple(kwargs.items()))
            


	

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
