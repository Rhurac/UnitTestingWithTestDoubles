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
            db = MockDataStore()
            AuthenticationComponent(db)
            assert True
        except:
            assert False


# noinspection PyMethodMayBeStatic
class TestCreateUser(object):
    """ Unit tests for the create_user method """

    def setup(self):
        """ Performs actions common to TestCreateUser unit tests """
        db = MockDataStore()
        auth = AuthenticationComponent(db)
        return auth

    def test_new_user_created_if_name_not_in_data_store(self):
        """ Asserts that a new user is created if given a valid name that is not yet in the datastore """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            assert auth.login_user("a", "password") == True
        except:
            assert False

    def test_raises_if_username_already_exists(self):
        """ Asserts that a RuntimeError is raised if the username already exists """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.create_user("a", "password")
            assert False
        except RuntimeError:
            assert True
        except:
            assert False


# noinspection PyMethodMayBeStatic
class TestLoginUser(object):
    """ Unit tests for the login_user method """

    def setup(self):
        """ Performs actions common to TestLoginUser unit tests """
        db = MockDataStore()
        auth = AuthenticationComponent(db)
        return auth

    def test_returns_true_if_username_and_password_exist(self):
        """ Asserts that True is returned if given a matching username and password """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            assert auth.login_user("a", "password")
        except:
            assert False

    def test_raises_if_username_does_not_exist(self):
        """ Asserts that RuntimeError is raised if the given username that does not exist """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.login_user("b", "password")
            assert False
        except RuntimeError:
            assert True
        except:
            assert False

    def test_returns_false_if_password_does_not_match(self):
        """ Asserts that False is returned if the given password does not match the username """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            assert auth.login_user("a", "pw") == False
        except:
            assert False


# noinspection PyMethodMayBeStatic
class TestChangePassword(object):
    """ Unit tests for the change_password method """

    def setup(self):
        """ Performs actions common to TestChangePassword unit tests """
        db = MockDataStore()
        auth = AuthenticationComponent(db)
        return auth

    def test_returns_true_if_username_exists(self):
        """ Asserts that the username is updated to the new password if username exists """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.change_password("a", "new_password")
            assert auth.login_user("a", "new_password")
        except:
            assert False

    def test_raises_if_username_not_exists(self):
        """ Asserts that RuntimeError is raised if the given username does not exist """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.change_password("b", "new_password")
            assert False
        except RuntimeError:
            assert True
        except:
            assert False


# noinspection PyMethodMayBeStatic
class TestRenameUser(object):
    """ Unit tests for the rename_user method """

    def setup(self):
        """ Performs actions common to TestRenameUser unit tests """
        db = MockDataStore()
        auth = AuthenticationComponent(db)
        return auth

    def test_returns_true_if_user_exists_and_new_name_is_unique(self):
        """ Asserts that the username is changed to the new username if the user exists and the new name is unique"""
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.rename_user("a", "b")
            assert auth.login_user("b", "password")
        except:
            assert False

    def test_returns_false_if_new_username_is_not_unique(self):
        """ Asserts that False is returned if the new username already exists """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.create_user("b", "password")
            assert auth.rename_user("a", "b") == False
        except:
            assert False

    def test_raises_if_username_not_exists(self):
        """ Asserts that RuntimeError is raised if the given username does not exist in the datastore """
        try:
            auth = self.setup()
            auth.create_user("a", "password")
            auth.rename_user("b", "c")
            assert False
        except RuntimeError:
            assert True
        except:
            assert False


# noinspection PyMethodMayBeStatic
class MockDataStore(DataStore):

    def __init__(self):
        self.users = {}

    def create(self, name, value):
        # create a new entry that records the given name and value
        # return True if the entry was created; False, otherwise
        # each entry is unique in terms of the associated name
        assert isinstance(name, str)
        assert isinstance(value, str)
        if name in self.users:
            return False
        self.users[name] = value
        return True
        # assert isinstance(ret_val, bool)

    def read(self, name):
        # return the value of the existing entry corresponding to the name
        # raise RuntimeError exception if there is no entry with the name
        assert isinstance(name, str)
        if name not in self.users:
            raise RuntimeError
        return self.users[name]
        # assert isinstance(ret_val, str)

    def update(self, name, value):
        # update the value of the existing entry corresponding to the name
        # return True if the entry was updated; false, otherwise
        assert isinstance(name, str)
        assert isinstance(value, str)
        if name not in self.users:
            return False
        self.users[name] = value
        # assert isinstance(ret_val, bool)

    def delete(self, name):
        # delete the existing entry corresponding to the name
        # return True if the entry was deleted; false, otherwise
        assert isinstance(name, str)
        if name not in self.users:
            return False
        self.users.pop(name)
        return True
        # assert isinstance(ret_val, bool)







