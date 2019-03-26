'''
Author: @amitrajitbose
'''

class Caesar_Cipher:
    def __init__(self):
        pass

    def _ensure_range(self, n):
        if(n%127 < 32):
            return 32 + (n%127)
        if(n < 32):
            return 127-(32-n)
        return n % 127

    def encrypt(self, password, key):
        key = key % 32
        password = list(password)
        new_password = []
        for i in password:
            new_password.append(chr(self._ensure_range(ord(i)+key)))
        return ''.join(new_password)

    def decrypt(self, password, key):
        key = key % 32
        original_password = []
        password = list(password)
        for i in password:
            original_password.append(chr(self._ensure_range(ord(i)-key)))
        return ''.join(original_password)

    def debug(self, str, k):
        if(self.decrypt(self.encrypt(str,k),k)):
            return True
        return False

obj = Caesar_Cipher()
print(obj.encrypt('RAJAT',267532))
print(obj.encrypt('rajA~',267532))
print(obj.debug('jhjFKVJ8763 87#57)(&^5~',72343946))