import hashlib
import hmac
import os
import re
import logging



def name_user(user: str, pattern_user= r"^(?=(?:.*[a-zA-Z]){3})[a-zA-Z0-9_-]{3,16}$"):
    """
    Vérifie si le nom est correct
    :param user:  nom d'utilisateur
    :param pattern_user:  Vérifie si le nom d'utilisateur compose des chiffres ou - ou _ et au moins 3 lettres,avec une longueur globale entre 3 et 16 caractères
    :return: True or False
    """
    if re.match(pattern_user, user):
        return True
    return False
def password_user(password: str, pattern_password = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"):
    """
    Verifie si le mot de pass est correcte
    :param password:
    :param pattern_password: Au moins 3 lettres au total, longueur globale entre 3 et 16 caractères
    :return: True or False
    """
    if re.match(pattern_password, password):
        return True
    return False


def hash_pwd(mot_de_pass):
    sel= os.urandom(16)
    h = hashlib.scrypt(mot_de_pass.encode("utf-8"), salt=sel, n=2**14, r=8, p=1)
    return f"scrypt${sel.hex()}${h.hex()}"
def verification(mot_de_passe, stocke):
    _, sel_hex, hash_hex = stocke.split("$")
    h = hashlib.scrypt(mot_de_passe.encode("utf-8"), salt=bytes.fromhex(sel_hex), n=2**14, r=8, p=1)
    return hmac.compare_digest(h, bytes.fromhex(hash_hex))






