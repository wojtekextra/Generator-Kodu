# Binary Serialization Generator

Projekt realizujący automatyczne generowanie kodu do serializacji i deserializacji danych binarnych przy użyciu systemu szablonów Jinja2 oraz komunikację między procesami przez TCP/IP.

## Struktura projektu
- `interface.json` - definicja struktury danych w formacie JSON.
- `template.j2` - szablon Jinja2 służący do generowania kodu klasy.
- `generator.py` - skrypt Pythona odpowiedzialny za odczyt schematu i generowanie kodu.
- `generated_code.py` - wygenerowany plik z klasą serializującą (automatycznie tworzony przez generator).
- `server.py` - serwer TCP nasłuchujący na połączenia.
- `client.py` - klient TCP wysyłający zserializowane dane.

## Wymagania
- Python 3.x
- `jinja2` (biblioteka do szablonów)

Instalacja zależności:
```bash
pip install jinja2