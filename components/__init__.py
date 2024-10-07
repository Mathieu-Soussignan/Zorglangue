# app/components/__init__.py

def zorglangue(phrase: str) -> str:
    """
    Convertit une phrase en Zorglangue en inversant chaque mot tout en conservant l'ordre des mots.
    """
    return ' '.join([word[::-1] for word in phrase.split()])
