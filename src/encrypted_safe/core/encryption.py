import random
import string

class MyCrypt:
    """
    A class to handle encryption of strings using a custom algorithm.
    """

    def encrypt(self, mdp: str) -> str:
        """
        Encrypts a password using a dynamically generated salt and key.

        Args:
            password (str) : The password to encrypt.

        Returns: str : the encrypted password.
        """
        from src.encrypted_safe.utils.encrypted_safe_utils import gen_random_tuple, gen_random_string
        sel = gen_random_string(len(mdp))
        cle = gen_random_tuple(len(mdp) + len(sel))
        combo = mdp + sel

        carac_chiffres = []


        for i, char in enumerate(combo):
            code_chiffres = (ord(char) + cle[i]) % 128
            carac_chiffres.append(chr(code_chiffres))

        return ''.join(carac_chiffres)