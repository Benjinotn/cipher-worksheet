from itertools import permutations
from cryptography.fernet import Fernet
import base64
class PasswordCracker:
    
    def crack_password(self, phrase_list):

        if len(phrase_list) != 4:
            print("The number of items in the list is invalid, you need 4!")
            return

        perm = permutations(phrase_list)

        k = Fernet(self.get_key())

        for p in perm:
            combo = ''.join(p)
            
            print(f"Trying the combination: {combo}\n")
            
            if bytes(combo, "UTF-8") == k.decrypt(b'gAAAAABkE0PVHNLuc8k1FJVWy36p11vRPrirluBgpHaK_p_1xAS9K-FlDf_LcrtzJ8lJG1JkLTk_66ffYARdcKa8CkSGZ3F_zeP5J7p_N-4fk50KclvM-GI='):
                print("Password Accepted, releasing secret key:")
                print(self.get_key())
                print("\n\n\n\n")
                return
            else:
                print("This combination was incorrect, try again.\n")
            
                  

    def get_key(self):
        f = open("DONOTOPEN.txt", "r")

        key = f.read()

        f.close()

        return bytes(key, 'UTF-8')




