class Security:
    def secure(self, info):
        if info is None:
            return None
        if len(info) == 0:
            return ""
        a = info.split()
        res = ""
        for i in a:
            if self.is_social_account_info(i):
                account_name = self.encrypt(i.split("/")[1])
                res += i.replace(str(i.split("/")[1]), str(account_name))
            else:
                res += i
            res += " "
        return res[:-1]

    def is_social_account_info(self, param):
        try:
            social = param.split(":")
            domain = social[1].split(".")
            domain = domain[1] + "." + domain[2].split('/')[0]
            account_name = param.split("/")[1]
        except:
            social = -1
        if social == -1 or social == 0:
            return False

        if social[0].islower():
            return False
        for d in domain:
            if not d.isnumeric():
                if not d.islower():
                    if not d.isalpha():
                        if d != '.':
                            return False
        for name in account_name:
            if not name.isnumeric():
                if not name.isascii():
                    if not name != "_":
                        return False
        return True

    def encrypt(self, s):
        if len(s) == 0:
            return ""
        base = s[0]
        count = 0
        encrypted = ""
        for i in s:
            if i != base:
                encrypted += str(ord(i) - 96)
                count = 1
            elif i == base:
                count += 1
                weight = ord(i) - 96
                result = weight * count
                encrypted += str(result)
            base = i
        return int(encrypted)


# def run():
#     s = Security()
#     print(s.secure(input()))


# run()
