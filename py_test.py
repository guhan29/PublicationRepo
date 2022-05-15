import email
import functools
import pytest

from flask.testing import FlaskClient
from repository import app, db
from repository.models import User

# To Run: pytest -v
# To run specific testcase: pytest py_tets.py::<function_name>

def force_login(email=None):
    def inner(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if email:
                for key, val in kwargs.items():
                    if isinstance(val, FlaskClient):
                        with val:
                            with val.session_transaction() as sess:
                                sess['_user_id'] = User.query.filter_by(email=email).first().id
                            return f(*args, **kwargs)
            return f(*args, **kwargs)

        return wrapper

    return inner

def force_logout(email=None):
    def inner(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if email:
                for key, val in kwargs.items():
                    if isinstance(val, FlaskClient):
                        with val:
                            with val.session_transaction() as sess:
                                sess['_user_id'] = sess['_user_id']
                            return f(*args, **kwargs)
            return f(*args, **kwargs)

        return wrapper

    return inner

# @pytest.fixture(scope='session')
@pytest.fixture()
def flask_app():
    # app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        yield app


# @pytest.fixture(scope='session')
@pytest.fixture()
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    return app.test_client()

# PK - TestLogin
def test_login(client):
    res = client.post(
        '/users/login',
        data = dict(email="PKPRAVEENKUMAR0128@GMAIL.COM", password="praveen123"),
        follow_redirects=True
    )
    assert b'Sucessfully logged in', res.data
# PK - Endtesting


# Lavanya - ChangePassword
@force_login(email="balanishabalasubramaniam@gmail.com")
def test_change_password(client):
    res = client.post('/users/change-password',
        data=dict(old_password='bala@123', new_password='bala@1234', new_confirm_password='bala@1234'),
        follow_redirects=True
    )
    assert b'Password has been Updated!' in res.data

@force_login(email="balanishabalasubramaniam@gmail.com")
def test_revert_change_password(client):
    res = client.post('/users/change-password',
        data=dict(old_password='bala@1234', new_password='bala@123', new_confirm_password='bala@123'),
        follow_redirects=True
    )
    assert b'Password has been Updated!' in res.data
# Lavanya - Endtesting


# Balanisha - SignUp Form
# @force_logout(email=None)
# def test_register(client):
#     res = client.post('/users/register',
#         data=dict(fname='Test', lname='BB', email='testbb@example.com', role='faculty',
#             institution='1', password='test@123',
#             confirm_password='test@123'
#         ),
#         follow_redirects=True
#     )
#     assert b'Your account has been created! You are now able to log in' in res.data

#     db.session.delete(User.query.filter_by(email='testbb@example.com').first())
#     db.session.commit()

#     assert User.query.filter_by(email='testbb@example.com').first() == None
# Balanisha - Endtesting

# if __name__ == '__main__':
#     import xmlrunner
#     runner = xmlrunner.XMLTestRunner(output='test-reports')
#     pytest.main(testRunner=runner)
