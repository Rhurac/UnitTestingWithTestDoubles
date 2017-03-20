""" Class: CIS640 ZA
    Assignment: Unit Testing With Test Doubles
    Author: Zachary Cleary """

from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent


class TestConstructor(object):
    """ Unit tests for the constructor method __init__ """

    def test_raises_if_invalid_data_store(self):
        """ Asserts that a TypeError is raised if the given datastore is not type DataStore """
        try:
            db = "DataStore"
            AuthenticationComponent(db)
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_passes_if_valid_data_store(self):
        """ Asserts that no errors are raised if the given datastore is a valid DataStore """
        try:
            db = DataStore()
            AuthenticationComponent(db)
            assert True
        except:
            assert False


class TestCreateUser(object):
    """ Unit tests for the create_user method """

    def test_new_user_created_given_valid_input(self):
        """ Asserts that a new user is created if both username and password are valid """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.login_user("a", "password") == True
        except:
            assert False

    def test_false_if_username_already_exists(self):
        """ Asserts that a False is returned if the username already exists """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.create_user("a", "password") == False
        except:
            assert False


class TestLoginUser(object):
    """ Unit tests for the login_user method """

    def test_returns_true_if_username_and_password_exist(self):
        """ Asserts that True is returned if given a matching username and password """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.login_user("a", "password")
        except:
            assert False

    def test_returns_false_if_username_does_not_exist(self):
        """ Asserts that False is returned if given a username that does not exist """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.login_user("b", "password") == False
        except:
            assert False

    def test_returns_false_if_password_does_not_match(self):
        """ Asserts that False is returned if the given password does not match the username """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.login_user("a", "pw") == False
        except:
            assert False


class TestChangePassword(object):
    """ Unit tests for the change_password method """

    def test_returns_true_if_username_exists_and_password_unique(self):
        """ Asserts that the username is updated to the new password if username exists and password is different """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            auth.change_password("a", "new_password")
            assert auth.login_user("a", "new_password")
        except:
            assert False

    def test_returns_false_if_username_not_exists(self):
        """ Asserts that False is returned if the given username does not exist """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.change_password("b", "new_password") == False
        except:
            assert False

    def test_returns_false_if_new_password_matches_old(self):
        """ Asserts that False is returned if the new password is the same as the old password """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.change_password("a", "password")
        except:
            assert False


class TestRenameUser(object):
    """ Unit tests for the rename_user method """

    def test_returns_true_if_user_exists_and_new_name_is_unique(self):
        """ Asserts that the username is changed to the new username if the user exists and the new name is unique"""
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            auth.rename_user("a", "b")
            assert auth.login_user("b", "password")
        except:
            assert False

    def test_returns_false_if_new_username_matches_old_username(self):
        """ Asserts that False is returned if the new username given matches the current username """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            assert auth.rename_user("a", "a") == False
        except:
            assert False

    def test_returns_false_if_new_username_is_not_unique(self):
        """ Asserts that False is returned if the new username already exists """
        try:
            db = DataStore()
            auth = AuthenticationComponent(db)
            auth.create_user("a", "password")
            auth.create_user("b", "password")
            assert auth.rename_user("a", "b") == False
        except:
            assert False







