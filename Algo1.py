'''
Follow this format for making contributions to encryption algorithms
'''
import itertools
class Algo1:
        def __init__(self):
                pass
        def encrypt(self,orig_word,key):
                modified_word=arr[key%length]
                arr[key%length]=orig_word
                return modified_word
	  
        def decrypt(self,modified_word,key):
                orig_word=arr[key%length]
                arr[key%length]=modified_word
                return orig_word

Original_password=input('Enter a password')
arr=["".join(perm) for perm in itertools.permutations(Original_password)]
length=len(arr)
obj=Algo1()
X=obj.encrypt(Original_password,10)
print("Encrypted Password:",X)
print("Decrypted Password:",obj.decrypt(X,10))

	
