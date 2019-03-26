'''
Author: @amitrajitbose
'''

class Caesar_Cipher:
    def __init__(self):
        pass

    def encrypt(self, password, key):
        key = key % 32
        password = list(password)
        new_password = []
        for i in password:
            new_password.append(chr(ord(i)+key))
        return ''.join(new_password)

    def decrypt(self, password, key):
        key = key % 32
        original_password = []
        password = list(password)
        for i in password:
            original_password.append(chr(ord(i)-key))
        return ''.join(original_password)

    def _debug(self, strr, k):
        if(self.decrypt(self.encrypt(strr,k),k) == strr):
            return True
        return False
