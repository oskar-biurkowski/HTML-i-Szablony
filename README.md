# Flask: szablony Jinja2, base.html, formularze

## Struktura folderów projektu:
flask-start/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── lista.html
    ├── szczegoly.html
    ├── dodaj.html
    └── szukaj.html

## Lista tras z przykładami:
- `/` - Strona główna
- `/czesc/<imie>` - np. `/czesc/Oskar`
- `/czesc/<imie>/<int:wiek>` - np. `/czesc/Oskar/18`
- `/dodaj/<int:a>/<int:b>` - np. `/dodaj/2/3`
- `/odejmij/<int:a>/<int:b>` - np. `/odejmij/5/2`
- `/pomnoz/<int:a>/<int:b>` - np. `/pomnoz/3/4`
- `/podziel/<int:a>/<int:b>` - np. `/podziel/7/0`
- `/potega/<int:a>/<int:b>` - np. `/potega/2/3`
- `/tabliczka/<int:n>` - np. `/tabliczka/5`
- `/lista` - Wyświetla listę produktów
- `/element/<int:id>` - np. `/element/1`
- `/szukaj` - np. `/szukaj?q=laptop`
- `/dodaj` - Formularz dodawania (GET/POST)
- `/start` - Przekierowanie na `/`