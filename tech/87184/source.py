import binascii
from operator import le
import string
import hashlib


class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.user_id = self.id_validation(user_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)

    def set_new_password(self, password):
        if not self.password_validation(password):
            raise Exception("invalid password")

        self.password = self.hash_password(password)

    def username_validation(self, username):
        if username.count("_") != 1:
            raise Exception("invalid username")
        name, family = username.split("_")
        for i in name:
            if i not in string.ascii_letters:
                raise Exception("invalid username")
        for i in family:
            if i not in string.ascii_letters:
                raise Exception("invalid username")
        return username

    def password_validation(self, password):
        if len(password) < 8:
            raise Exception("invalid password")
        count_upper = count_lower = count_number = False
        for i in password:
            if i.islower():
                count_lower = True
            elif i.isupper():
                count_upper = True
            elif i.isnumeric():
                count_number = True
        if count_lower and count_upper and count_number:
            m = hashlib.sha256()
            m.update(password.encode("utf-8"))
            return binascii.hexlify(m.digest()).decode("ascii")
        else:
            raise Exception("invalid password")

    def id_validation(self, user_id):
        if len(user_id) != 10:
            raise Exception("invalid code meli")
        num = 0
        for i in range(9):
            num += (10-i) * (ord(user_id[i]) - ord('0'))
        m = num % 11
        if m < 2:
            if (ord(user_id[9]) - ord('0')) == m:
                return user_id
            else:
                raise Exception("invalid code melli")
        else:
            if (ord(user_id[9]) - ord("0")) == (11 - m):
                return user_id
            else:
                raise Exception("invalid code melli")

    def phone_validation(self, phone):
        if len(phone) == 13:
            if not phone.startswith("+989"):
                raise Exception("invalid phone number")
            else:
                return phone.replace("+989", "09")
        elif len(phone) == 11:
            if not phone.startswith("09"):
                raise Exception("invalid phone number")
            else:
                return phone
        else:
            raise Exception("invalid phone number")

    def email_validation(self, email):
        first, second = email.split("@")
        for i in first:
            if i not in (".-_" + string.ascii_letters + string.digits):
                raise Exception("invalid email")
        sec, third = second.split(".")

        for i in sec:
            if i not in (".-_" + string.ascii_letters + string.digits):
                raise Exception("invalid email")

        if len(third) > 5 or len(third) < 2:
            raise Exception("invalid email")

        for i in third:
            if i not in string.ascii_letters:
                raise Exception("invalid email")

        return email

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users = []
        self.active_users = []
        pass

    def show_users(self):
        pass

    def register(self, user):
        for u in self.register_users:
            if user.username == u.username:
                raise Exception("user already registered")

        self.register_users.append(user)
        return "register successful"

    def login(self, **kwargs):
        if "password" in kwargs:
            if "username" in kwargs:
                if "email" in kwargs:
                    for u in self.register_users:
                        if u.username == kwargs['username'] and u.email == kwargs['email'] and u.password == u.hash_password(kwargs['password']):
                            self.active_users.append(u)
                            return "login successful"
                else:
                    for u in self.register_users:
                        if u.username == kwargs['username'] and u.password == u.hash_password(kwargs['password']):
                            self.active_users.append(u)
                            return "login successful"
            elif "email" in kwargs:
                for u in self.register_users:
                    if u.email == kwargs['email'] and u.password == u.hash_password(kwargs['password']):
                        self.active_users.append(u)
                        return "login successful"

        return "invalid login"

    def logout(self, user):
        for u in self.active_users:
            if u.username == user.username:
                self.active_users.remove(u)
                return "logout successful"

        return "user is not logged in"

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


def show_welcome(function):
    def inner(username):
        usr = username.replace("_", " ").title()
        if len(usr) > 15:
            usr = usr[:15] + "..."
        return function(usr)


def verify_change_password(function):
    def inner(user, old_pass, new_pass):
        if user.password == user.hash_password(old_pass):
            user.set_new_password(new_pass)
            return function(user, old_pass, new_pass)


@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)


@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")


acc = Account("Ali_Babaei", "5Dj:xKBA", "0030376459",
              "09121212121", "SAliB_SAliB@gmail.com")
