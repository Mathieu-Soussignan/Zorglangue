import sys
import os
import string

# Ajout du chemin vers dossier parent de 'app' au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.components import zorglangue

def zorglangue(phrase):
    def reverse_word(word):
        # Si le mot contient de la ponctuation à la fin, on la sépare
        if word[-1] in string.punctuation:
            return word[:-1][::-1] + word[-1]
        return word[::-1]
    
    mots_inverses = [reverse_word(mot) for mot in phrase.split()]
    return ' '.join(mots_inverses)


def test_zorglangue():
    assert zorglangue("Bonjour") == "ruojnoB"
    assert zorglangue("Vive Zorglub !") == "eviV bulgroZ !"
    assert zorglangue("Ceci est un message secret") == "iceC tse nu egassem terces"

# print(zorglangue("Ma phrase ici"))