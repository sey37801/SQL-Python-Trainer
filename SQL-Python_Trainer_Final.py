import tkinter as tk
from tkinter import messagebox
import json
import os
import re

PROGRESS_FILE = "progress.json"


def build_tasks():
    tasks = []

    # ---------------- Aufgabe 1 – Fenster & Start-GUI ----------------
    levels_1 = [
        {
            "description": (
                "Aufgabe 1 – Level 1\n\n"
                "Ziel: Schreibe eine Funktion create_window(), die ein Tkinter-Fenster erstellt und startet.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du baust einen minimalen Tkinter-Programmstart.\n"
                "- Der Code soll in einer Funktion stehen, die am Ende aufgerufen wird.\n\n"
                "Anforderungen:\n"
                "- import tkinter as tk\n"
                "- def create_window():\n"
                "- root = tk.Tk()\n"
                "- root.mainloop()\n"
                "- Am Ende: create_window() aufrufen.\n\n"
                "Einrückung:\n"
                "- Der Code innerhalb der Funktion ist um 4 Leerzeichen eingerückt.\n"
            ),
            "concept": "einen einfachen Tkinter-Programmstart mit Funktion und mainloop",
            "hints": [
                "Hinweis 1 (Struktur):\n\n"
                "Du brauchst zuerst den Import:\n"
                "    import tkinter as tk\n\n"
                "Dann definierst du eine Funktion:\n"
                "    def create_window():\n"
                "        root = tk.Tk()\n"
                "        root.mainloop()\n\n"
                "Achte darauf, dass root = tk.Tk() und root.mainloop() eingerückt sind.",
                "Hinweis 2 (Aufruf):\n\n"
                "Ganz unten im Code musst du die Funktion aufrufen:\n"
                "    create_window()\n\n"
                "Die Einrückung innerhalb der Funktion bleibt immer gleich (4 Leerzeichen).",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def create_window():\n"
                "    root = tk.Tk()\n"
                "    root.mainloop()\n\n"
                "create_window()\n"
            ],
            "required": [
                "import tkinter as tk",
                "def create_window",
                "tk.Tk(",
                "root.mainloop",
                "create_window("
            ]
        },
        {
            "description": (
                "Aufgabe 1 – Level 2\n\n"
                "Ziel: Erweitere create_window(), sodass das Fenster einen Titel 'Lerntrainer' hat.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du ergänzt deine bestehende Funktion um eine Zeile.\n"
                "- Der Fenstertitel soll gesetzt werden.\n\n"
                "Anforderungen:\n"
                "- In create_window(): root.title('Lerntrainer') setzen.\n"
                "Einrückung:\n"
                "- root.title('Lerntrainer') steht eingerückt innerhalb der Funktion.\n"
            ),
            "concept": "Fenstertitel mit root.title('...') setzen",
            "hints": [
                "Hinweis 1:\n\n"
                "In deiner Funktion create_window() hast du root = tk.Tk().\n"
                "Direkt danach kannst du schreiben:\n"
                "    root.title('Lerntrainer')\n\n"
                "Die Zeile ist genauso eingerückt wie root = tk.Tk().",
                "Hinweis 2:\n\n"
                "Achte darauf, dass du genau 'Lerntrainer' verwendest:\n"
                "    root.title('Lerntrainer')",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def create_window():\n"
                "    root = tk.Tk()\n"
                "    root.title('Lerntrainer')\n"
                "    root.mainloop()\n\n"
                "create_window()\n"
            ],
            "required": [
                "root.title('Lerntrainer')"
            ]
        },
        {
            "description": (
                "Aufgabe 1 – Level 3\n\n"
                "Ziel: Setze die Fenstergröße auf 400x300 Pixel.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du ergänzt deine Funktion um eine weitere Eigenschaft.\n"
                "- Die Fenstergröße wird über geometry() gesetzt.\n\n"
                "Anforderungen:\n"
                "- In create_window(): root.geometry('400x300') aufrufen.\n"
                "Einrückung:\n"
                "- Die geometry-Zeile ist wie die anderen Funktionszeilen eingerückt.\n"
            ),
            "concept": "Fenstergröße mit root.geometry('BreitexHöhe') setzen",
            "hints": [
                "Hinweis 1:\n\n"
                "Nach root = tk.Tk() kannst du schreiben:\n"
                "    root.geometry('400x300')",
                "Hinweis 2:\n\n"
                "Die Zeichenfolge muss genau so aussehen:\n"
                "    '400x300'\n"
                "Also:\n"
                "    root.geometry('400x300')",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def create_window():\n"
                "    root = tk.Tk()\n"
                "    root.title('Lerntrainer')\n"
                "    root.geometry('400x300')\n"
                "    root.mainloop()\n\n"
                "create_window()\n"
            ],
            "required": [
                "root.geometry('400x300')"
            ]
        },
        {
            "description": (
                "Aufgabe 1 – Level 4\n\n"
                "Ziel: Füge ein Label mit dem Text 'Willkommen' hinzu.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du fügst ein neues Widget (Label) hinzu.\n"
                "- Das Label soll im Fenster sichtbar sein.\n\n"
                "Anforderungen:\n"
                "- label = tk.Label(root, text='Willkommen')\n"
                "- label.pack()\n"
                "Einrückung:\n"
                "- Beide Zeilen sind innerhalb der Funktion eingerückt.\n"
            ),
            "concept": "ein Label-Widget erstellen und mit pack() anzeigen",
            "hints": [
                "Hinweis 1:\n\n"
                "Erstelle ein Label:\n"
                "    label = tk.Label(root, text='Willkommen')",
                "Hinweis 2:\n\n"
                "Damit das Label sichtbar wird, musst du es packen:\n"
                "    label.pack()",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def create_window():\n"
                "    root = tk.Tk()\n"
                "    root.title('Lerntrainer')\n"
                "    root.geometry('400x300')\n"
                "    label = tk.Label(root, text='Willkommen')\n"
                "    label.pack()\n"
                "    root.mainloop()\n\n"
                "create_window()\n"
            ],
            "required": [
                "Label(",
                "text='Willkommen'",
                "label.pack("
            ]
        },
        {
            "description": (
                "Aufgabe 1 – Level 5\n\n"
                "Ziel: Füge einen Button mit der Aufschrift 'Start' hinzu, der beim Klick 'Los gehts!' ausgibt.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du definierst eine innere Funktion on_click().\n"
                "- Ein Button ruft diese Funktion über command=... auf.\n\n"
                "Anforderungen:\n"
                "- Eine innere Funktion on_click() mit print('Los gehts!')\n"
                "- button = tk.Button(root, text='Start', command=on_click)\n"
                "- button.pack()\n"
                "Einrückung:\n"
                "- on_click() ist innerhalb von create_window() eingerückt.\n"
                "- Der Inhalt von on_click() ist nochmals eingerückt.\n"
            ),
            "concept": "einen Button mit Callback-Funktion (command=...) erstellen",
            "hints": [
                "Hinweis 1:\n\n"
                "Definiere in create_window() eine Funktion:\n"
                "    def on_click():\n"
                "        print('Los gehts!')\n\n"
                "Achte auf die Einrückung:\n"
                "- def on_click(): ist wie die anderen Zeilen in create_window() eingerückt.\n"
                "- print('Los gehts!') ist um 4 weitere Leerzeichen eingerückt.",
                "Hinweis 2:\n\n"
                "Erstelle den Button:\n"
                "    button = tk.Button(root, text='Start', command=on_click)\n"
                "    button.pack()",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def create_window():\n"
                "    def on_click():\n"
                "        print('Los gehts!')\n\n"
                "    root = tk.Tk()\n"
                "    root.title('Lerntrainer')\n"
                "    root.geometry('400x300')\n"
                "    label = tk.Label(root, text='Willkommen')\n"
                "    label.pack()\n"
                "    button = tk.Button(root, text='Start', command=on_click)\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "create_window()\n"
            ],
            "required": [
                "def on_click",
                "print('Los gehts!')",
                "Button(",
                "text='Start'",
                "command=on_click"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 1 – Fenster & Start-GUI", "levels": levels_1})

    # ---------------- Aufgabe 2 – Eingabe & Ausgabe ----------------
    levels_2 = [
        {
            "description": (
                "Aufgabe 2 – Level 1\n\n"
                "Ziel: Schreibe eine Funktion input_app(), die ein Fenster mit einem Entry-Feld und einem Button erstellt.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du baust eine kleine Eingabeoberfläche.\n"
                "- Ein Entry-Feld und ein Button sollen im Fenster erscheinen.\n\n"
                "Anforderungen:\n"
                "- import tkinter as tk\n"
                "- def input_app():\n"
                "- root = tk.Tk()\n"
                "- entry = tk.Entry(root)\n"
                "- button = tk.Button(root, text='OK')\n"
                "- entry.pack(), button.pack(), root.mainloop()\n"
                "Einrückung:\n"
                "- Alles innerhalb von input_app() ist um 4 Leerzeichen eingerückt.\n"
            ),
            "concept": "ein Eingabefeld (Entry) und einen einfachen Button erstellen",
            "hints": [
                "Hinweis 1 (Struktur):\n\n"
                "    import tkinter as tk\n\n"
                "    def input_app():\n"
                "        root = tk.Tk()\n"
                "        entry = tk.Entry(root)\n"
                "        entry.pack()\n"
                "        button = tk.Button(root, text='OK')\n"
                "        button.pack()\n"
                "        root.mainloop()\n\n"
                "    input_app()",
                "Hinweis 2 (Einrückung):\n\n"
                "Achte darauf, dass alle Zeilen innerhalb von input_app() gleich eingerückt sind.",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def input_app():\n"
                "    root = tk.Tk()\n"
                "    entry = tk.Entry(root)\n"
                "    entry.pack()\n"
                "    button = tk.Button(root, text='OK')\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "input_app()\n"
            ],
            "required": [
                "import tkinter as tk",
                "def input_app",
                "tk.Tk(",
                "Entry(",
                "Button(",
                "text='OK'",
                "input_app("
            ]
        },
        {
            "description": (
                "Aufgabe 2 – Level 2\n\n"
                "Ziel: Der Button soll beim Klick den Inhalt des Entry-Feldes in der Konsole ausgeben.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du ergänzt eine innere Funktion on_click().\n"
                "- Diese liest den Text aus dem Entry und gibt ihn aus.\n\n"
                "Anforderungen:\n"
                "- Eine innere Funktion on_click()\n"
                "- text = entry.get()\n"
                "- print(text)\n"
                "- Button mit command=on_click\n"
                "Einrückung:\n"
                "- on_click() ist innerhalb von input_app() eingerückt.\n"
                "- Der Inhalt von on_click() ist nochmals eingerückt.\n"
            ),
            "concept": "Entry-Inhalt mit entry.get() auslesen und ausgeben",
            "hints": [
                "Hinweis 1:\n\n"
                "Definiere in input_app() eine Funktion:\n"
                "    def on_click():\n"
                "        text = entry.get()\n"
                "        print(text)",
                "Hinweis 2:\n\n"
                "Button:\n"
                "    button = tk.Button(root, text='OK', command=on_click)",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def input_app():\n"
                "    def on_click():\n"
                "        text = entry.get()\n"
                "        print(text)\n\n"
                "    root = tk.Tk()\n"
                "    entry = tk.Entry(root)\n"
                "    entry.pack()\n"
                "    button = tk.Button(root, text='OK', command=on_click)\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "input_app()\n"
            ],
            "required": [
                "def on_click",
                "entry.get(",
                "print(",
                "command=on_click"
            ]
        },
        {
            "description": (
                "Aufgabe 2 – Level 3\n\n"
                "Ziel: Füge ein Label hinzu, das den zuletzt eingegebenen Text anzeigt.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du erweiterst die Oberfläche um ein Label.\n"
                "- Das Label zeigt den zuletzt eingegebenen Text an.\n\n"
                "Anforderungen:\n"
                "- label = tk.Label(root, text='Noch nichts eingegeben')\n"
                "- label.pack()\n"
                "- In on_click(): label.config(text=text)\n"
            ),
            "concept": "Label dynamisch mit label.config(text=...) aktualisieren",
            "hints": [
                "Hinweis 1:\n\n"
                "Erstelle ein Label vor dem Button:\n"
                "    label = tk.Label(root, text='Noch nichts eingegeben')\n"
                "    label.pack()",
                "Hinweis 2:\n\n"
                "In on_click():\n"
                "    label.config(text=text)",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def input_app():\n"
                "    def on_click():\n"
                "        text = entry.get()\n"
                "        print(text)\n"
                "        label.config(text=text)\n\n"
                "    root = tk.Tk()\n"
                "    entry = tk.Entry(root)\n"
                "    entry.pack()\n"
                "    label = tk.Label(root, text='Noch nichts eingegeben')\n"
                "    label.pack()\n"
                "    button = tk.Button(root, text='OK', command=on_click)\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "input_app()\n"
            ],
            "required": [
                "Label(",
                "Noch nichts eingegeben",
                "label.config(",
                "text=text"
            ]
        },
        {
            "description": (
                "Aufgabe 2 – Level 4\n\n"
                "Ziel: Leere das Entry-Feld nach dem Klick auf den Button.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du ergänzt die Logik in on_click().\n"
                "- Nach der Verarbeitung wird das Eingabefeld geleert.\n\n"
                "Anforderungen:\n"
                "- In on_click(): entry.delete(0, 'end')\n"
            ),
            "concept": "Entry-Feld mit entry.delete(0, 'end') leeren",
            "hints": [
                "Hinweis 1:\n\n"
                "Nach dem Auslesen des Textes kannst du schreiben:\n"
                "    entry.delete(0, 'end')",
                "Hinweis 2:\n\n"
                "Achte darauf, dass entry in on_click() sichtbar ist (Closure).",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def input_app():\n"
                "    def on_click():\n"
                "        text = entry.get()\n"
                "        print(text)\n"
                "        label.config(text=text)\n"
                "        entry.delete(0, 'end')\n\n"
                "    root = tk.Tk()\n"
                "    entry = tk.Entry(root)\n"
                "    entry.pack()\n"
                "    label = tk.Label(root, text='Noch nichts eingegeben')\n"
                "    label.pack()\n"
                "    button = tk.Button(root, text='OK', command=on_click)\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "input_app()\n"
            ],
            "required": [
                "entry.delete(0, 'end')"
            ]
        },
        {
            "description": (
                "Aufgabe 2 – Level 5\n\n"
                "Ziel: Wenn das Entry-Feld leer ist, soll 'Bitte etwas eingeben' ausgegeben werden.\n\n"
                "Struktur der Aufgabe:\n"
                "- Du baust eine if-Abfrage in on_click().\n"
                "- Leere Eingabe wird speziell behandelt.\n\n"
                "Anforderungen:\n"
                "- if text == '':\n"
                "- print('Bitte etwas eingeben')\n"
                "- label.config(text='Bitte etwas eingeben')\n"
            ),
            "concept": "if-Abfrage auf leere Eingabe und Fehlermeldung anzeigen",
            "hints": [
                "Hinweis 1:\n\n"
                "In on_click():\n"
                "    text = entry.get()\n"
                "    if text == '':\n"
                "        ...\n"
                "    else:\n"
                "        ...",
                "Hinweis 2:\n\n"
                "Im leeren Fall:\n"
                "    print('Bitte etwas eingeben')\n"
                "    label.config(text='Bitte etwas eingeben')",
                "Beispiel-Lösung:\n\n"
                "import tkinter as tk\n\n"
                "def input_app():\n"
                "    def on_click():\n"
                "        text = entry.get()\n"
                "        if text == '':\n"
                "            print('Bitte etwas eingeben')\n"
                "            label.config(text='Bitte etwas eingeben')\n"
                "        else:\n"
                "            print(text)\n"
                "            label.config(text=text)\n"
                "        entry.delete(0, 'end')\n\n"
                "    root = tk.Tk()\n"
                "    entry = tk.Entry(root)\n"
                "    entry.pack()\n"
                "    label = tk.Label(root, text='Noch nichts eingegeben')\n"
                "    label.pack()\n"
                "    button = tk.Button(root, text='OK', command=on_click)\n"
                "    button.pack()\n"
                "    root.mainloop()\n\n"
                "input_app()\n"
            ],
            "required": [
                "if text ==",
                "Bitte etwas eingeben"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 2 – Eingabe & Ausgabe", "levels": levels_2})

    # ---------------- Python-Aufgaben 3–15: aufbauende Lernpfade ----------------
    # Jede Aufgabe besteht aus 5 Levels, die Schritt für Schritt aufeinander aufbauen.
    # Hinweis 3 enthält immer eine vollständige abschreibbare Lösung.
    def progressive_task(title, levels_data):
        levels = []
        for i, data in enumerate(levels_data, start=1):
            code = data["solution"].rstrip() + "\n"
            partial = data.get("partial") or code
            levels.append({
                "description": (
                    f"{title} – Level {i}\n\n"
                    f"Ziel: {data['goal']}\n\n"
                    "Was du in diesem Level baust:\n"
                    f"- {data['build']}\n\n"
                    "Warum das wichtig ist:\n"
                    f"- {data['why']}\n\n"
                    "Anforderungen:\n"
                    + "\n".join(f"- {req}" for req in data["required"])
                    + "\n\nAchte darauf, dass dein Code vollständig ist und unten aufgerufen wird, falls eine Funktion verlangt wird."
                ),
                "concept": data["concept"],
                "work_tip": data["tip"],
                "hints": [
                    "So gehst du vor:\n\n" + data["hint1"],
                    "Orientiere dich an dieser fast fertigen Struktur und ergänze die fehlenden Details:\n\n" + partial.rstrip(),
                    "Vollständige Lösung zum Abschreiben:\n\n" + code,
                ],
                "required": data["required"],
            })
        return {"title": title, "levels": levels}

    task_specs = [
        ("Aufgabe 3 – Schleifen", [
            dict(goal="Gib mit einer for-Schleife die Zahlen 1 bis 5 aus.", build="eine Funktion loops_lvl1(), die eine Zahlenreihe wiederholt ausgibt", why="Schleifen vermeiden, dass du denselben print-Befehl mehrfach schreiben musst.", concept="for-Schleifen mit range()", tip="Tipp: range(1, 6) erzeugt die Werte 1 bis 5. Die Schleife setzt jeden Wert nacheinander in die Variable zahl und print() gibt ihn aus.", hint1="Erstelle zuerst die Funktion. Danach kommt eine for-Schleife mit range(1, 6). In der Schleife gibst du die aktuelle Zahl aus.", required=["def loops_lvl1", "for zahl in range(1, 6)", "print(zahl)", "loops_lvl1("], partial="def loops_lvl1():\n    for zahl in range(1, 6):\n        print(zahl)\n\nloops_lvl1()", solution="def loops_lvl1():\n    for zahl in range(1, 6):\n        print(zahl)\n\nloops_lvl1()"),
            dict(goal="Sammle die Zahlen 1 bis 5 in einer Liste und gib die Liste aus.", build="eine Schleife, die Werte mit append() in einer Liste speichert", why="Du lernst, wie Wiederholung und Datensammlung zusammenarbeiten.", concept="Listen mit Schleifen füllen", tip="Tipp: Erstelle zuerst eine leere Liste. In jedem Schleifendurchlauf hängt append() eine neue Zahl hinten an diese Liste an.", hint1="Lege eine leere Liste zahlen an. Durchlaufe range(1, 6), füge jede zahl mit append() hinzu und gib danach die fertige Liste aus.", required=["def loops_lvl2", "zahlen = []", "for zahl in range(1, 6)", "zahlen.append(zahl)", "print(zahlen)", "loops_lvl2("], partial="def loops_lvl2():\n    zahlen = []\n    for zahl in range(1, 6):\n        zahlen.append(zahl)\n    print(zahlen)\n\nloops_lvl2()", solution="def loops_lvl2():\n    zahlen = []\n    for zahl in range(1, 6):\n        zahlen.append(zahl)\n    print(zahlen)\n\nloops_lvl2()"),
            dict(goal="Berechne die Summe der Zahlen 1 bis 5.", build="einen Zählerwert summe, der in der Schleife wächst", why="Viele Programme addieren Werte schrittweise, zum Beispiel Warenkörbe oder Punkte.", concept="Summenbildung in Schleifen", tip="Tipp: summe startet bei 0. Bei jedem Durchlauf wird die aktuelle Zahl addiert, danach enthält summe das Endergebnis.", hint1="Erstelle summe = 0. In der Schleife rechnest du summe = summe + zahl. Danach gibst du summe aus.", required=["def loops_lvl3", "summe = 0", "for zahl in range(1, 6)", "summe = summe + zahl", "print(summe)", "loops_lvl3("], partial="def loops_lvl3():\n    summe = 0\n    for zahl in range(1, 6):\n        summe = summe + zahl\n    print(summe)\n\nloops_lvl3()", solution="def loops_lvl3():\n    summe = 0\n    for zahl in range(1, 6):\n        summe = summe + zahl\n    print(summe)\n\nloops_lvl3()"),
            dict(goal="Gib nur gerade Zahlen zwischen 1 und 10 aus.", build="eine Schleife mit einer if-Bedingung für gerade Zahlen", why="Programme müssen oft nur bestimmte Werte verarbeiten und andere überspringen.", concept="Schleifen mit if-Bedingungen kombinieren", tip="Tipp: zahl % 2 berechnet den Rest bei Division durch 2. Wenn der Rest 0 ist, ist die Zahl gerade.", hint1="Durchlaufe range(1, 11). In der Schleife prüfst du mit if zahl % 2 == 0, ob die Zahl gerade ist.", required=["def loops_lvl4", "for zahl in range(1, 11)", "if zahl % 2 == 0", "print(zahl)", "loops_lvl4("], partial="def loops_lvl4():\n    for zahl in range(1, 11):\n        if zahl % 2 == 0:\n            print(zahl)\n\nloops_lvl4()", solution="def loops_lvl4():\n    for zahl in range(1, 11):\n        if zahl % 2 == 0:\n            print(zahl)\n\nloops_lvl4()"),
            dict(goal="Erzeuge ein kleines Einmaleins für die Zahl 3.", build="eine Schleife, die rechnet und einen lesbaren Satz ausgibt", why="Du verbindest Wiederholung, Rechnung und Textausgabe zu einem kleinen Programmablauf.", concept="Schleifen mit Berechnung und formatierter Ausgabe", tip="Tipp: In jedem Durchlauf wird ergebnis neu berechnet. Der f-String setzt Zahl und Ergebnis direkt in den Ausgabetext ein.", hint1="Durchlaufe die Faktoren 1 bis 10. Berechne ergebnis = 3 * faktor und gib z.B. '3 x 4 = 12' aus.", required=["def loops_lvl5", "for faktor in range(1, 11)", "ergebnis = 3 * faktor", "print(f\"3 x {faktor} = {ergebnis}\")", "loops_lvl5("], partial="def loops_lvl5():\n    for faktor in range(1, 11):\n        ergebnis = 3 * faktor\n        print(f\"3 x {faktor} = {ergebnis}\")\n\nloops_lvl5()", solution="def loops_lvl5():\n    for faktor in range(1, 11):\n        ergebnis = 3 * faktor\n        print(f\"3 x {faktor} = {ergebnis}\")\n\nloops_lvl5()"),
        ]),
        ("Aufgabe 4 – Listen", [
            dict(goal="Erstelle eine Liste mit drei Namen und gib sie aus.", build="eine einfache Liste in einer Funktion", why="Listen speichern mehrere zusammengehörige Werte in einer einzigen Variable.", concept="Listen erstellen und ausgeben", tip="Tipp: Eine Liste steht in eckigen Klammern. Die Namen sind Textwerte und stehen deshalb in Hochkommas.", hint1="Schreibe eine Funktion, lege namen = ['Anna', 'Ben', 'Carla'] an und gib namen mit print() aus.", required=["def lists_lvl1", "namen =", "Anna", "Ben", "Carla", "print(namen)", "lists_lvl1("], partial="def lists_lvl1():\n    namen = ['Anna', 'Ben', 'Carla']\n    print(namen)\n\nlists_lvl1()", solution="def lists_lvl1():\n    namen = ['Anna', 'Ben', 'Carla']\n    print(namen)\n\nlists_lvl1()"),
            dict(goal="Gib den ersten Namen aus der Liste aus.", build="einen Zugriff über den Index 0", why="Programme lesen gezielt einzelne Elemente aus Listen aus.", concept="Listenindex verwenden", tip="Tipp: Python zählt Listenpositionen ab 0. Der erste Eintrag ist deshalb namen[0].", hint1="Erstelle wieder die Liste namen. Danach gibst du mit print(namen[0]) das erste Element aus.", required=["def lists_lvl2", "namen =", "print(namen[0])", "lists_lvl2("], partial="def lists_lvl2():\n    namen = ['Anna', 'Ben', 'Carla']\n    print(namen[0])\n\nlists_lvl2()", solution="def lists_lvl2():\n    namen = ['Anna', 'Ben', 'Carla']\n    print(namen[0])\n\nlists_lvl2()"),
            dict(goal="Füge einen weiteren Namen zur Liste hinzu.", build="append() zum Erweitern einer Liste", why="Listen sind veränderbar und können während des Programms wachsen.", concept="Elemente mit append() hinzufügen", tip="Tipp: append('David') hängt den neuen Wert hinten an die bestehende Liste an. Danach enthält die Liste vier Namen.", hint1="Lege die Liste an, rufe namen.append('David') auf und gib anschließend die ganze Liste aus.", required=["def lists_lvl3", "namen.append('David')", "print(namen)", "lists_lvl3("], partial="def lists_lvl3():\n    namen = ['Anna', 'Ben', 'Carla']\n    namen.append('David')\n    print(namen)\n\nlists_lvl3()", solution="def lists_lvl3():\n    namen = ['Anna', 'Ben', 'Carla']\n    namen.append('David')\n    print(namen)\n\nlists_lvl3()"),
            dict(goal="Gehe mit einer Schleife durch alle Namen.", build="eine for-Schleife über eine Liste", why="So kannst du jeden Eintrag automatisch verarbeiten, egal wie lang die Liste ist.", concept="über Listen iterieren", tip="Tipp: for name in namen nimmt sich nacheinander jeden Eintrag aus der Liste und speichert ihn kurz in der Variable name.", hint1="Erstelle die Liste und schreibe dann for name in namen:. Innerhalb der Schleife gibst du name aus.", required=["def lists_lvl4", "for name in namen", "print(name)", "lists_lvl4("], partial="def lists_lvl4():\n    namen = ['Anna', 'Ben', 'Carla', 'David']\n    for name in namen:\n        print(name)\n\nlists_lvl4()", solution="def lists_lvl4():\n    namen = ['Anna', 'Ben', 'Carla', 'David']\n    for name in namen:\n        print(name)\n\nlists_lvl4()"),
            dict(goal="Zähle, wie viele Namen in der Liste stehen.", build="len() zur Längenbestimmung", why="Viele Programme müssen wissen, wie viele Einträge gespeichert sind.", concept="Listenlänge mit len()", tip="Tipp: len(namen) liefert eine Zahl. Diese Zahl kannst du in einer Variable speichern oder direkt ausgeben.", hint1="Erstelle die Liste, speichere anzahl = len(namen) und gib anzahl aus.", required=["def lists_lvl5", "anzahl = len(namen)", "print(anzahl)", "lists_lvl5("], partial="def lists_lvl5():\n    namen = ['Anna', 'Ben', 'Carla', 'David']\n    anzahl = len(namen)\n    print(anzahl)\n\nlists_lvl5()", solution="def lists_lvl5():\n    namen = ['Anna', 'Ben', 'Carla', 'David']\n    anzahl = len(namen)\n    print(anzahl)\n\nlists_lvl5()"),
        ]),
        ("Aufgabe 5 – Bedingungen", [
            dict(goal="Prüfe, ob eine Zahl größer als 10 ist.", build="eine einfache if-Abfrage", why="Bedingungen entscheiden, welcher Code ausgeführt wird.", concept="if-Abfragen", tip="Tipp: Der Code unter if läuft nur, wenn die Bedingung wahr ist. Die eingerückte print-Zeile gehört zum if-Block.", hint1="Lege zahl = 12 an. Prüfe mit if zahl > 10: und gib einen passenden Text aus.", required=["def conds_lvl1", "zahl = 12", "if zahl > 10", "print('größer als 10')", "conds_lvl1("], partial="def conds_lvl1():\n    zahl = 12\n    if zahl > 10:\n        print('größer als 10')\n\nconds_lvl1()", solution="def conds_lvl1():\n    zahl = 12\n    if zahl > 10:\n        print('größer als 10')\n\nconds_lvl1()"),
            dict(goal="Ergänze einen else-Fall.", build="if und else für zwei mögliche Wege", why="Mit else reagiert dein Programm auch, wenn die Bedingung nicht wahr ist.", concept="if/else", tip="Tipp: else hat keine eigene Bedingung. Es bedeutet: Führe diesen Block aus, wenn das if nicht zutrifft.", hint1="Prüfe zahl > 10. Unter else gibst du '10 oder kleiner' aus.", required=["def conds_lvl2", "if zahl > 10", "else", "print('10 oder kleiner')", "conds_lvl2("], partial="def conds_lvl2():\n    zahl = 7\n    if zahl > 10:\n        print('größer als 10')\n    else:\n        print('10 oder kleiner')\n\nconds_lvl2()", solution="def conds_lvl2():\n    zahl = 7\n    if zahl > 10:\n        print('größer als 10')\n    else:\n        print('10 oder kleiner')\n\nconds_lvl2()"),
            dict(goal="Prüfe drei Fälle: positiv, negativ oder null.", build="if, elif und else", why="Damit kann dein Programm mehrere mögliche Situationen unterscheiden.", concept="mehrere Bedingungen mit elif", tip="Tipp: Python prüft von oben nach unten. Sobald eine Bedingung passt, wird deren Block ausgeführt.", hint1="Nutze if zahl > 0, elif zahl < 0 und else für genau 0.", required=["def conds_lvl3", "elif zahl < 0", "else", "print('null')", "conds_lvl3("], partial="def conds_lvl3():\n    zahl = 0\n    if zahl > 0:\n        print('positiv')\n    elif zahl < 0:\n        print('negativ')\n    else:\n        print('null')\n\nconds_lvl3()", solution="def conds_lvl3():\n    zahl = 0\n    if zahl > 0:\n        print('positiv')\n    elif zahl < 0:\n        print('negativ')\n    else:\n        print('null')\n\nconds_lvl3()"),
            dict(goal="Prüfe, ob ein Alter für Volljährigkeit reicht.", build="eine realistische Bedingung mit Vergleich >=", why="Bedingungen werden oft genutzt, um Regeln abzubilden.", concept="Vergleichsoperatoren", tip="Tipp: >= bedeutet größer oder gleich. Bei alter 18 oder mehr soll 'volljährig' ausgegeben werden.", hint1="Lege alter = 18 an. Prüfe if alter >= 18: sonst else.", required=["def conds_lvl4", "alter = 18", "if alter >= 18", "print('volljährig')", "conds_lvl4("], partial="def conds_lvl4():\n    alter = 18\n    if alter >= 18:\n        print('volljährig')\n    else:\n        print('minderjährig')\n\nconds_lvl4()", solution="def conds_lvl4():\n    alter = 18\n    if alter >= 18:\n        print('volljährig')\n    else:\n        print('minderjährig')\n\nconds_lvl4()"),
            dict(goal="Kombiniere Bedingungen mit and.", build="eine Bedingung, die zwei Regeln gleichzeitig prüft", why="Viele Entscheidungen brauchen mehrere Voraussetzungen gleichzeitig.", concept="logische Operatoren mit and", tip="Tipp: and ist nur wahr, wenn beide Teile wahr sind. Hier muss der Nutzer alt genug sein und ein Ticket besitzen.", hint1="Lege alter und hat_ticket an. Prüfe if alter >= 18 and hat_ticket == True:.", required=["def conds_lvl5", "hat_ticket = True", "and", "print('Einlass erlaubt')", "conds_lvl5("], partial="def conds_lvl5():\n    alter = 20\n    hat_ticket = True\n    if alter >= 18 and hat_ticket == True:\n        print('Einlass erlaubt')\n    else:\n        print('Kein Einlass')\n\nconds_lvl5()", solution="def conds_lvl5():\n    alter = 20\n    hat_ticket = True\n    if alter >= 18 and hat_ticket == True:\n        print('Einlass erlaubt')\n    else:\n        print('Kein Einlass')\n\nconds_lvl5()"),
        ]),
        ("Aufgabe 6 – Funktionen", [
            dict(goal="Schreibe eine Funktion, die einen Namen begrüßt.", build="eine Funktion mit einem Parameter", why="Parameter machen Funktionen flexibel, weil sie Werte von außen bekommen.", concept="Funktionen mit Parametern", tip="Tipp: name ist ein Platzhalter. Beim Aufruf begruessen('Mia') wird name innerhalb der Funktion zu 'Mia'.", hint1="Definiere begruessen(name). In der Funktion gibst du den Namen in einem Satz aus.", required=["def begruessen(name)", "print(f'Hallo {name}')", "begruessen('Mia')"], partial="def begruessen(name):\n    print(f'Hallo {name}')\n\nbegruessen('Mia')", solution="def begruessen(name):\n    print(f'Hallo {name}')\n\nbegruessen('Mia')"),
            dict(goal="Gib die Summe zweier Zahlen zurück.", build="eine Funktion mit return", why="return gibt ein Ergebnis an den Aufrufer zurück, damit man damit weiterarbeiten kann.", concept="Rückgabewerte", tip="Tipp: addieren(3, 4) liefert 7 zurück. print() zeigt dieses Ergebnis dann auf dem Bildschirm an.", hint1="Definiere addieren(a, b). Rechne a + b und gib es mit return zurück.", required=["def addieren(a, b)", "return a + b", "print(addieren(3, 4))"], partial="def addieren(a, b):\n    return a + b\n\nprint(addieren(3, 4))", solution="def addieren(a, b):\n    return a + b\n\nprint(addieren(3, 4))"),
            dict(goal="Berechne den Durchschnitt einer Liste.", build="eine Funktion, die sum() und len() nutzt", why="Funktionen können Daten aufnehmen, berechnen und ein Ergebnis liefern.", concept="Berechnung in Funktionen", tip="Tipp: sum(werte) addiert alle Zahlen. len(werte) zählt sie. Durchschnitt ist Summe geteilt durch Anzahl.", hint1="Definiere durchschnitt(werte). Gib sum(werte) / len(werte) zurück.", required=["def durchschnitt(werte)", "sum(werte)", "len(werte)", "print(durchschnitt", "funcs_lvl3"], partial="def durchschnitt(werte):\n    return sum(werte) / len(werte)\n\ndef funcs_lvl3():\n    zahlen = [2, 4, 6]\n    print(durchschnitt(zahlen))\n\nfuncs_lvl3()", solution="def durchschnitt(werte):\n    return sum(werte) / len(werte)\n\ndef funcs_lvl3():\n    zahlen = [2, 4, 6]\n    print(durchschnitt(zahlen))\n\nfuncs_lvl3()"),
            dict(goal="Nutze einen Standardwert für einen Parameter.", build="eine Funktion, die auch ohne zweiten Parameter funktioniert", why="Standardwerte machen Funktionen bequemer und verhindern unnötige Wiederholung.", concept="Default-Parameter", tip="Tipp: Wenn keine sprache übergeben wird, nutzt Python automatisch 'de'.", hint1="Definiere begruessung(name, sprache='de'). Prüfe die Sprache mit if.", required=["def begruessung(name, sprache='de')", "if sprache == 'de'", "return", "print(begruessung('Mia'))"], partial="def begruessung(name, sprache='de'):\n    if sprache == 'de':\n        return f'Hallo {name}'\n    return f'Hello {name}'\n\nprint(begruessung('Mia'))", solution="def begruessung(name, sprache='de'):\n    if sprache == 'de':\n        return f'Hallo {name}'\n    return f'Hello {name}'\n\nprint(begruessung('Mia'))"),
            dict(goal="Baue Funktionen zusammen: Preis, Steuer und Endpreis.", build="mehrere Funktionen, die miteinander arbeiten", why="Größere Programme bestehen aus kleinen Funktionen, die jeweils eine klare Aufgabe haben.", concept="Funktionen kombinieren", tip="Tipp: berechne_steuer() liefert nur den Steuerbetrag. endpreis() addiert Preis und Steuer zum Endpreis.", hint1="Schreibe berechne_steuer(preis) und endpreis(preis). endpreis ruft berechne_steuer(preis) auf.", required=["def berechne_steuer(preis)", "return preis * 0.19", "def endpreis(preis)", "return preis + berechne_steuer(preis)", "print(endpreis(100))"], partial="def berechne_steuer(preis):\n    return preis * 0.19\n\ndef endpreis(preis):\n    return preis + berechne_steuer(preis)\n\nprint(endpreis(100))", solution="def berechne_steuer(preis):\n    return preis * 0.19\n\ndef endpreis(preis):\n    return preis + berechne_steuer(preis)\n\nprint(endpreis(100))"),
        ]),
    ]

    # Weitere Aufgaben werden kompakt, aber mit eigenen aufbauenden Levels erzeugt.
    task_specs.extend([
        ("Aufgabe 7 – Klassen", [
            dict(goal="Erstelle eine einfache Klasse Person.", build="eine Klasse mit __init__ und Attribut name", why="Klassen bündeln Daten und Verhalten zu eigenen Objekten.", concept="Klassen und Objekte", tip="Tipp: __init__ läuft automatisch, wenn ein Objekt erstellt wird. self.name speichert den Namen im Objekt.", hint1="Definiere class Person. In __init__ speicherst du name in self.name.", required=["class Person", "def __init__(self, name)", "self.name = name", "person = Person('Mia')", "print(person.name)"], partial="class Person:\n    def __init__(self, name):\n        self.name = name\n\nperson = Person('Mia')\nprint(person.name)", solution="class Person:\n    def __init__(self, name):\n        self.name = name\n\nperson = Person('Mia')\nprint(person.name)"),
            dict(goal="Füge der Klasse ein Alter hinzu.", build="zwei Attribute in einem Objekt", why="Objekte können mehrere zusammengehörige Informationen speichern.", concept="mehrere Attribute", tip="Tipp: self.alter ist ein zweiter gespeicherter Wert im selben Objekt. Damit gehören Name und Alter zusammen.", hint1="Erweitere __init__ um alter und speichere self.alter = alter.", required=["class Person", "self.name = name", "self.alter = alter", "Person('Mia', 21)", "print(person.alter)"], partial="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\nperson = Person('Mia', 21)\nprint(person.name)\nprint(person.alter)", solution="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\nperson = Person('Mia', 21)\nprint(person.name)\nprint(person.alter)"),
            dict(goal="Füge eine Methode vorstellen() hinzu.", build="eine Methode, die Objektwerte verwendet", why="Methoden sind Funktionen, die zu einem Objekt gehören und dessen Daten nutzen.", concept="Methoden in Klassen", tip="Tipp: Eine Methode bekommt self als ersten Parameter. Dadurch kann sie auf self.name und self.alter zugreifen.", hint1="Schreibe in der Klasse def vorstellen(self): und gib einen Satz mit Name und Alter aus.", required=["def vorstellen(self)", "print(f'Ich bin {self.name} und {self.alter} Jahre alt')", "person.vorstellen()"], partial="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def vorstellen(self):\n        print(f'Ich bin {self.name} und {self.alter} Jahre alt')\n\nperson = Person('Mia', 21)\nperson.vorstellen()", solution="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def vorstellen(self):\n        print(f'Ich bin {self.name} und {self.alter} Jahre alt')\n\nperson = Person('Mia', 21)\nperson.vorstellen()"),
            dict(goal="Erstelle mehrere Person-Objekte in einer Liste.", build="Objekte speichern und mit einer Schleife nutzen", why="In echten Apps arbeitet man häufig mit vielen Objekten gleichzeitig.", concept="Listen von Objekten", tip="Tipp: Die Liste personen enthält zwei fertige Person-Objekte. Die Schleife ruft bei jedem Objekt vorstellen() auf.", hint1="Erstelle eine Liste mit Person('Mia', 21) und Person('Ben', 24). Laufe mit for person in personen darüber.", required=["personen = [", "Person('Mia', 21)", "Person('Ben', 24)", "for person in personen", "person.vorstellen()"], partial="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def vorstellen(self):\n        print(f'Ich bin {self.name} und {self.alter} Jahre alt')\n\npersonen = [Person('Mia', 21), Person('Ben', 24)]\nfor person in personen:\n    person.vorstellen()", solution="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def vorstellen(self):\n        print(f'Ich bin {self.name} und {self.alter} Jahre alt')\n\npersonen = [Person('Mia', 21), Person('Ben', 24)]\nfor person in personen:\n    person.vorstellen()"),
            dict(goal="Ergänze eine Methode ist_volljaehrig().", build="eine Methode mit Rückgabewert True/False", why="Objekte können eigene Regeln prüfen und ein Ergebnis zurückgeben.", concept="Methoden mit return", tip="Tipp: ist_volljaehrig() gibt einen Wahrheitswert zurück. Die if-Abfrage entscheidet danach, welcher Text angezeigt wird.", hint1="Schreibe eine Methode, die self.alter >= 18 zurückgibt. Nutze sie in einer if-Abfrage.", required=["def ist_volljaehrig(self)", "return self.alter >= 18", "if person.ist_volljaehrig()", "print(f'{person.name} ist volljährig')"], partial="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def ist_volljaehrig(self):\n        return self.alter >= 18\n\nperson = Person('Mia', 21)\nif person.ist_volljaehrig():\n    print(f'{person.name} ist volljährig')\nelse:\n    print(f'{person.name} ist minderjährig')", solution="class Person:\n    def __init__(self, name, alter):\n        self.name = name\n        self.alter = alter\n\n    def ist_volljaehrig(self):\n        return self.alter >= 18\n\nperson = Person('Mia', 21)\nif person.ist_volljaehrig():\n    print(f'{person.name} ist volljährig')\nelse:\n    print(f'{person.name} ist minderjährig')"),
        ]),
        ("Aufgabe 8 – Dateien", [
            dict(goal="Schreibe Text in eine Datei.", build="open() im Schreibmodus", why="Dateien speichern Daten dauerhaft außerhalb des Programms.", concept="Dateien schreiben", tip="Tipp: with open(...) öffnet die Datei sicher. Nach dem eingerückten Block wird sie automatisch geschlossen.", hint1="Öffne notiz.txt mit mode 'w' und schreibe einen Satz hinein.", required=["def files_lvl1", "with open('notiz.txt', 'w'", "f.write('Hallo Datei')", "files_lvl1("], partial="def files_lvl1():\n    with open('notiz.txt', 'w', encoding='utf-8') as f:\n        f.write('Hallo Datei')\n\nfiles_lvl1()", solution="def files_lvl1():\n    with open('notiz.txt', 'w', encoding='utf-8') as f:\n        f.write('Hallo Datei')\n\nfiles_lvl1()"),
            dict(goal="Lies den Text aus der Datei wieder ein.", build="open() im Lesemodus", why="Programme müssen gespeicherte Daten später wieder laden können.", concept="Dateien lesen", tip="Tipp: read() liest den kompletten Dateiinhalt als Text. Danach kannst du ihn ausgeben oder weiterverarbeiten.", hint1="Öffne notiz.txt mit 'r', lies mit read() und gib den Inhalt aus.", required=["def files_lvl2", "with open('notiz.txt', 'r'", "inhalt = f.read()", "print(inhalt)", "files_lvl2("], partial="def files_lvl2():\n    with open('notiz.txt', 'r', encoding='utf-8') as f:\n        inhalt = f.read()\n    print(inhalt)\n\nfiles_lvl2()", solution="def files_lvl2():\n    with open('notiz.txt', 'r', encoding='utf-8') as f:\n        inhalt = f.read()\n    print(inhalt)\n\nfiles_lvl2()"),
            dict(goal="Füge eine zweite Zeile an die Datei an.", build="append-Modus 'a'", why="Anhängen verändert vorhandene Daten, ohne die Datei komplett zu überschreiben.", concept="Dateien erweitern", tip="Tipp: 'a' bedeutet append. Der neue Text wird an das Dateiende geschrieben.", hint1="Öffne die Datei mit 'a' und schreibe mit \n eine neue Zeile hinein.", required=["def files_lvl3", "with open('notiz.txt', 'a'", "f.write(", "files_lvl3("], partial="def files_lvl3():\n    with open('notiz.txt', 'a', encoding='utf-8') as f:\n        f.write('\\nZweite Zeile')\n\nfiles_lvl3()", solution="def files_lvl3():\n    with open('notiz.txt', 'a', encoding='utf-8') as f:\n        f.write('\\nZweite Zeile')\n\nfiles_lvl3()"),
            dict(goal="Lies alle Zeilen als Liste ein.", build="readlines() und eine Schleife über Zeilen", why="Zeilenweise Verarbeitung ist wichtig für Logs, CSV-Dateien und Listen.", concept="Dateien zeilenweise lesen", tip="Tipp: readlines() gibt eine Liste von Zeilen zurück. strip() entfernt den Zeilenumbruch am Ende.", hint1="Lies zeilen = f.readlines(). Danach gehst du mit for zeile in zeilen darüber.", required=["def files_lvl4", "zeilen = f.readlines()", "for zeile in zeilen", "print(zeile.strip())", "files_lvl4("], partial="def files_lvl4():\n    with open('notiz.txt', 'r', encoding='utf-8') as f:\n        zeilen = f.readlines()\n    for zeile in zeilen:\n        print(zeile.strip())\n\nfiles_lvl4()", solution="def files_lvl4():\n    with open('notiz.txt', 'r', encoding='utf-8') as f:\n        zeilen = f.readlines()\n    for zeile in zeilen:\n        print(zeile.strip())\n\nfiles_lvl4()"),
            dict(goal="Speichere eine Liste von Aufgaben in einer Datei.", build="eine Liste mit einer Schreib-Schleife", why="So entstehen einfache Exportfunktionen für App-Daten.", concept="Listen in Dateien speichern", tip="Tipp: Jede Aufgabe wird in einer eigenen Zeile gespeichert. Das \n sorgt dafür, dass die nächste Aufgabe in der nächsten Zeile steht.", hint1="Lege eine Liste aufgaben an. Öffne todo.txt mit 'w' und schreibe jede Aufgabe in einer for-Schleife.", required=["def files_lvl5", "aufgaben =", "with open('todo.txt', 'w'", "for aufgabe in aufgaben", "f.write(aufgabe +", "files_lvl5("], partial="def files_lvl5():\n    aufgaben = ['lernen', 'üben', 'wiederholen']\n    with open('todo.txt', 'w', encoding='utf-8') as f:\n        for aufgabe in aufgaben:\n            f.write(aufgabe + '\\n')\n\nfiles_lvl5()", solution="def files_lvl5():\n    aufgaben = ['lernen', 'üben', 'wiederholen']\n    with open('todo.txt', 'w', encoding='utf-8') as f:\n        for aufgabe in aufgaben:\n            f.write(aufgabe + '\\n')\n\nfiles_lvl5()"),
        ]),
        ("Aufgabe 9 – Fehlerbehandlung", [
            dict(goal="Fange eine Division durch 0 ab.", build="try/except um riskanten Code", why="Fehlerbehandlung verhindert, dass das Programm sofort abstürzt.", concept="try/except", tip="Tipp: Der Code im try wird versucht. Wenn ZeroDivisionError passiert, springt Python in den except-Block.", hint1="Setze 10 / 0 in try. Fange ZeroDivisionError ab und gib eine verständliche Meldung aus.", required=["def errors_lvl1", "try", "10 / 0", "except ZeroDivisionError", "print('Division durch 0 ist nicht erlaubt')", "errors_lvl1("], partial="def errors_lvl1():\n    try:\n        ergebnis = 10 / 0\n        print(ergebnis)\n    except ZeroDivisionError:\n        print('Division durch 0 ist nicht erlaubt')\n\nerrors_lvl1()", solution="def errors_lvl1():\n    try:\n        ergebnis = 10 / 0\n        print(ergebnis)\n    except ZeroDivisionError:\n        print('Division durch 0 ist nicht erlaubt')\n\nerrors_lvl1()"),
            dict(goal="Fange eine ungültige Zahlumwandlung ab.", build="ValueError behandeln", why="Benutzereingaben sind oft falsch und müssen sicher geprüft werden.", concept="ValueError", tip="Tipp: int('abc') kann nicht funktionieren. Genau dafür ist except ValueError da.", hint1="Versuche int('abc') in try und fange ValueError ab.", required=["def errors_lvl2", "int('abc')", "except ValueError", "print('Keine gültige Zahl')", "errors_lvl2("], partial="def errors_lvl2():\n    try:\n        zahl = int('abc')\n        print(zahl)\n    except ValueError:\n        print('Keine gültige Zahl')\n\nerrors_lvl2()", solution="def errors_lvl2():\n    try:\n        zahl = int('abc')\n        print(zahl)\n    except ValueError:\n        print('Keine gültige Zahl')\n\nerrors_lvl2()"),
            dict(goal="Nutze else, wenn kein Fehler passiert.", build="try/except/else", why="else trennt den Erfolgsfall sauber vom Fehlerfall.", concept="try/except/else", tip="Tipp: else läuft nur, wenn der try-Block keinen Fehler ausgelöst hat.", hint1="Teile 10 durch 2. Im else-Block gibst du das Ergebnis aus.", required=["def errors_lvl3", "try", "ergebnis = 10 / 2", "except ZeroDivisionError", "else", "print(ergebnis)", "errors_lvl3("], partial="def errors_lvl3():\n    try:\n        ergebnis = 10 / 2\n    except ZeroDivisionError:\n        print('Fehler')\n    else:\n        print(ergebnis)\n\nerrors_lvl3()", solution="def errors_lvl3():\n    try:\n        ergebnis = 10 / 2\n    except ZeroDivisionError:\n        print('Fehler')\n    else:\n        print(ergebnis)\n\nerrors_lvl3()"),
            dict(goal="Nutze finally für Aufräumarbeiten.", build="finally nach try/except", why="finally läuft immer und eignet sich für Aufräumen oder Abschlussmeldungen.", concept="finally", tip="Tipp: Egal ob Fehler oder Erfolg: Der finally-Block wird am Ende ausgeführt.", hint1="Schreibe try/except und danach finally mit einer Abschlussmeldung.", required=["def errors_lvl4", "finally", "print('Prüfung beendet')", "errors_lvl4("], partial="def errors_lvl4():\n    try:\n        zahl = int('42')\n        print(zahl)\n    except ValueError:\n        print('Fehler')\n    finally:\n        print('Prüfung beendet')\n\nerrors_lvl4()", solution="def errors_lvl4():\n    try:\n        zahl = int('42')\n        print(zahl)\n    except ValueError:\n        print('Fehler')\n    finally:\n        print('Prüfung beendet')\n\nerrors_lvl4()"),
            dict(goal="Schreibe eine sichere Division als Funktion.", build="eine Funktion, die bei Fehler None zurückgibt", why="So kann anderer Code erkennen, ob die Berechnung funktioniert hat.", concept="Fehlerbehandlung in Funktionen", tip="Tipp: Bei b == 0 wird ein Fehler abgefangen und None zurückgegeben. Sonst kommt das Rechenergebnis zurück.", hint1="Definiere sichere_division(a, b). Gib im try a / b zurück, im except None.", required=["def sichere_division(a, b)", "return a / b", "except ZeroDivisionError", "return None", "print(sichere_division(10, 0))"], partial="def sichere_division(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n\nprint(sichere_division(10, 0))", solution="def sichere_division(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n\nprint(sichere_division(10, 0))"),
        ]),
    ])

    # Kompakte, aber nicht wiederholende Lernpfade für Aufgaben 10–15.
    remaining = {
        "Aufgabe 10 – Module": ("mods", [
            ("Importiere math und gib pi aus.", "import math\n\ndef mods_lvl1():\n    print(math.pi)\n\nmods_lvl1()", ["import math", "math.pi", "mods_lvl1("]),
            ("Nutze math.sqrt() für eine Quadratwurzel.", "import math\n\ndef mods_lvl2():\n    wurzel = math.sqrt(16)\n    print(wurzel)\n\nmods_lvl2()", ["math.sqrt(16)", "wurzel", "print(wurzel)", "mods_lvl2("]),
            ("Importiere randint aus random.", "from random import randint\n\ndef mods_lvl3():\n    zahl = randint(1, 6)\n    print(zahl)\n\nmods_lvl3()", ["from random import randint", "randint(1, 6)", "mods_lvl3("]),
            ("Nutze datetime für das heutige Datum.", "from datetime import date\n\ndef mods_lvl4():\n    heute = date.today()\n    print(heute)\n\nmods_lvl4()", ["from datetime import date", "date.today()", "print(heute)", "mods_lvl4("]),
            ("Baue eine kleine Modul-Demo mit zwei Imports.", "import math\nfrom random import randint\n\ndef mods_lvl5():\n    zahl = randint(1, 10)\n    wurzel = math.sqrt(zahl)\n    print(zahl)\n    print(wurzel)\n\nmods_lvl5()", ["import math", "from random import randint", "math.sqrt(zahl)", "mods_lvl5("]),
        ], "Module stellen fertige Werkzeuge bereit. Du importierst sie und nutzt dann ihre Funktionen im eigenen Code."),
        "Aufgabe 11 – Mini-Kalkulator": ("calc", [
            ("Addiere zwei feste Zahlen.", "def calc_lvl1():\n    a = 4\n    b = 5\n    print(a + b)\n\ncalc_lvl1()", ["a = 4", "b = 5", "print(a + b)", "calc_lvl1("]),
            ("Schreibe eine addieren-Funktion.", "def addieren(a, b):\n    return a + b\n\ndef calc_lvl2():\n    print(addieren(4, 5))\n\ncalc_lvl2()", ["def addieren(a, b)", "return a + b", "print(addieren(4, 5))", "calc_lvl2("]),
            ("Ergänze Subtraktion.", "def subtrahieren(a, b):\n    return a - b\n\ndef calc_lvl3():\n    print(subtrahieren(10, 3))\n\ncalc_lvl3()", ["def subtrahieren(a, b)", "return a - b", "calc_lvl3("]),
            ("Wähle eine Rechenart mit if.", "def calc_lvl4():\n    a = 8\n    b = 2\n    operator = '+'\n    if operator == '+':\n        print(a + b)\n    else:\n        print(a - b)\n\ncalc_lvl4()", ["operator = '+'", "if operator == '+'", "print(a + b)", "else", "calc_lvl4("]),
            ("Baue einen kleinen Kalkulator mit vier Rechenarten.", "def calc_lvl5():\n    a = 8\n    b = 2\n    operator = '*'\n    if operator == '+':\n        print(a + b)\n    elif operator == '-':\n        print(a - b)\n    elif operator == '*':\n        print(a * b)\n    elif operator == '/':\n        print(a / b)\n\ncalc_lvl5()", ["elif operator == '-'", "elif operator == '*'", "elif operator == '/'", "calc_lvl5("]),
        ], "Ein Kalkulator zeigt, wie Variablen, Funktionen und Bedingungen zusammenspielen."),
        "Aufgabe 12 – Klickzähler": ("click", [
            ("Erstelle eine Zählvariable und gib sie aus.", "def click_lvl1():\n    count = 0\n    print(count)\n\nclick_lvl1()", ["count = 0", "print(count)", "click_lvl1("]),
            ("Erhöhe den Zähler um 1.", "def click_lvl2():\n    count = 0\n    count = count + 1\n    print(count)\n\nclick_lvl2()", ["count = count + 1", "print(count)", "click_lvl2("]),
            ("Simuliere drei Klicks mit einer Schleife.", "def click_lvl3():\n    count = 0\n    for klick in range(3):\n        count = count + 1\n    print(count)\n\nclick_lvl3()", ["for klick in range(3)", "count = count + 1", "click_lvl3("]),
            ("Schreibe eine Funktion click(), die den Zähler erhöht.", "def click_lvl4():\n    count = 0\n    def click():\n        nonlocal count\n        count = count + 1\n        print(count)\n    click()\n    click()\n\nclick_lvl4()", ["def click()", "nonlocal count", "click()", "click_lvl4("]),
            ("Baue einen Tkinter-Klickzähler.", "import tkinter as tk\n\ndef click_lvl5():\n    count = 0\n    root = tk.Tk()\n    label = tk.Label(root, text='0')\n    label.pack()\n    def click():\n        nonlocal count\n        count = count + 1\n        label.config(text=str(count))\n    button = tk.Button(root, text='Klick', command=click)\n    button.pack()\n    root.mainloop()\n\nclick_lvl5()", ["import tkinter as tk", "nonlocal count", "label.config(text=str(count))", "command=click", "click_lvl5("]),
        ], "Ein Klickzähler macht Zustand sichtbar: Eine Variable merkt sich, wie oft etwas passiert ist."),
        "Aufgabe 13 – Canvas": ("canvas", [
            ("Erstelle ein Fenster mit Canvas.", "import tkinter as tk\n\ndef canvas_lvl1():\n    root = tk.Tk()\n    canvas = tk.Canvas(root, width=300, height=200)\n    canvas.pack()\n    root.mainloop()\n\ncanvas_lvl1()", ["tk.Canvas", "width=300", "height=200", "canvas_lvl1("]),
            ("Zeichne ein Rechteck.", "import tkinter as tk\n\ndef canvas_lvl2():\n    root = tk.Tk()\n    canvas = tk.Canvas(root, width=300, height=200)\n    canvas.pack()\n    canvas.create_rectangle(50, 50, 150, 120)\n    root.mainloop()\n\ncanvas_lvl2()", ["create_rectangle", "50, 50, 150, 120", "canvas_lvl2("]),
            ("Zeichne zusätzlich einen Kreis.", "import tkinter as tk\n\ndef canvas_lvl3():\n    root = tk.Tk()\n    canvas = tk.Canvas(root, width=300, height=200)\n    canvas.pack()\n    canvas.create_rectangle(50, 50, 150, 120)\n    canvas.create_oval(170, 50, 240, 120)\n    root.mainloop()\n\ncanvas_lvl3()", ["create_rectangle", "create_oval", "canvas_lvl3("]),
            ("Füge Text auf dem Canvas hinzu.", "import tkinter as tk\n\ndef canvas_lvl4():\n    root = tk.Tk()\n    canvas = tk.Canvas(root, width=300, height=200)\n    canvas.pack()\n    canvas.create_rectangle(50, 50, 150, 120)\n    canvas.create_oval(170, 50, 240, 120)\n    canvas.create_text(150, 160, text='Meine Zeichnung')\n    root.mainloop()\n\ncanvas_lvl4()", ["create_text", "Meine Zeichnung", "canvas_lvl4("]),
            ("Baue eine vollständige kleine Zeichnung.", "import tkinter as tk\n\ndef canvas_lvl5():\n    root = tk.Tk()\n    root.title('Canvas Demo')\n    canvas = tk.Canvas(root, width=300, height=200)\n    canvas.pack()\n    canvas.create_rectangle(40, 80, 140, 150)\n    canvas.create_oval(180, 60, 250, 130)\n    canvas.create_line(20, 170, 280, 170)\n    canvas.create_text(150, 25, text='Formen')\n    root.mainloop()\n\ncanvas_lvl5()", ["root.title('Canvas Demo')", "create_line", "create_text", "canvas_lvl5("]),
        ], "Canvas ist eine Zeichenfläche. Du gibst Koordinaten an und Tkinter zeichnet Formen an diese Positionen."),
        "Aufgabe 14 – Layout": ("layout", [
            ("Erstelle ein Fenster mit einem Frame.", "import tkinter as tk\n\ndef layout_lvl1():\n    root = tk.Tk()\n    frame = tk.Frame(root)\n    frame.pack()\n    root.mainloop()\n\nlayout_lvl1()", ["tk.Frame", "frame.pack()", "layout_lvl1("]),
            ("Packe zwei Labels untereinander.", "import tkinter as tk\n\ndef layout_lvl2():\n    root = tk.Tk()\n    frame = tk.Frame(root)\n    frame.pack()\n    tk.Label(frame, text='Oben').pack()\n    tk.Label(frame, text='Unten').pack()\n    root.mainloop()\n\nlayout_lvl2()", ["Oben", "Unten", "layout_lvl2("]),
            ("Ordne Labels nebeneinander an.", "import tkinter as tk\n\ndef layout_lvl3():\n    root = tk.Tk()\n    frame = tk.Frame(root)\n    frame.pack()\n    tk.Label(frame, text='Links').pack(side='left')\n    tk.Label(frame, text='Rechts').pack(side='left')\n    root.mainloop()\n\nlayout_lvl3()", ["side='left'", "Links", "Rechts", "layout_lvl3("]),
            ("Nutze grid für Zeilen und Spalten.", "import tkinter as tk\n\ndef layout_lvl4():\n    root = tk.Tk()\n    tk.Label(root, text='Name').grid(row=0, column=0)\n    tk.Entry(root).grid(row=0, column=1)\n    tk.Button(root, text='OK').grid(row=1, column=0, columnspan=2)\n    root.mainloop()\n\nlayout_lvl4()", ["grid(row=0, column=0)", "tk.Entry", "columnspan=2", "layout_lvl4("]),
            ("Baue ein zweigeteiltes Layout.", "import tkinter as tk\n\ndef layout_lvl5():\n    root = tk.Tk()\n    left = tk.Frame(root)\n    right = tk.Frame(root)\n    left.pack(side='left', fill='both', expand=True)\n    right.pack(side='right', fill='both', expand=True)\n    tk.Label(left, text='Menü').pack()\n    tk.Label(right, text='Inhalt').pack()\n    root.mainloop()\n\nlayout_lvl5()", ["left.pack(side='left'", "right.pack(side='right'", "expand=True", "layout_lvl5("]),
        ], "Layout entscheidet, wo Widgets erscheinen. pack() ist einfach, grid() ist gut für Tabellenformen."),
        "Aufgabe 15 – Mini-App": ("miniapp", [
            ("Erstelle das Grundfenster der Mini-App.", "import tkinter as tk\n\ndef miniapp_lvl1():\n    root = tk.Tk()\n    root.title('Mini-App')\n    root.mainloop()\n\nminiapp_lvl1()", ["root.title('Mini-App')", "miniapp_lvl1("]),
            ("Füge Eingabefeld und Button hinzu.", "import tkinter as tk\n\ndef miniapp_lvl2():\n    root = tk.Tk()\n    root.title('Mini-App')\n    entry = tk.Entry(root)\n    entry.pack()\n    button = tk.Button(root, text='Speichern')\n    button.pack()\n    root.mainloop()\n\nminiapp_lvl2()", ["tk.Entry", "text='Speichern'", "miniapp_lvl2("]),
            ("Zeige die Eingabe in einem Label an.", "import tkinter as tk\n\ndef miniapp_lvl3():\n    root = tk.Tk()\n    entry = tk.Entry(root)\n    entry.pack()\n    label = tk.Label(root, text='Noch leer')\n    label.pack()\n    def speichern():\n        label.config(text=entry.get())\n    button = tk.Button(root, text='Speichern', command=speichern)\n    button.pack()\n    root.mainloop()\n\nminiapp_lvl3()", ["def speichern()", "label.config(text=entry.get())", "command=speichern", "miniapp_lvl3("]),
            ("Speichere mehrere Eingaben in einer Liste.", "import tkinter as tk\n\ndef miniapp_lvl4():\n    eintraege = []\n    root = tk.Tk()\n    entry = tk.Entry(root)\n    entry.pack()\n    label = tk.Label(root, text='[]')\n    label.pack()\n    def speichern():\n        eintraege.append(entry.get())\n        label.config(text=str(eintraege))\n    tk.Button(root, text='Speichern', command=speichern).pack()\n    root.mainloop()\n\nminiapp_lvl4()", ["eintraege = []", "eintraege.append(entry.get())", "str(eintraege)", "miniapp_lvl4("]),
            ("Baue eine kleine To-do-App mit Leeren des Eingabefelds.", "import tkinter as tk\n\ndef miniapp_lvl5():\n    eintraege = []\n    root = tk.Tk()\n    root.title('To-do Mini-App')\n    entry = tk.Entry(root)\n    entry.pack()\n    label = tk.Label(root, text='Noch keine Einträge')\n    label.pack()\n    def speichern():\n        text = entry.get()\n        if text != '':\n            eintraege.append(text)\n            label.config(text='\\n'.join(eintraege))\n            entry.delete(0, 'end')\n    tk.Button(root, text='Speichern', command=speichern).pack()\n    root.mainloop()\n\nminiapp_lvl5()", ["root.title('To-do Mini-App')", "if text != ''", "'\\n'.join(eintraege)", "entry.delete(0, 'end')", "miniapp_lvl5("]),
        ], "Die Mini-App verbindet Fenster, Eingabe, Zustand und Aktualisierung der Oberfläche."),
    }
    for title, (base, items, theme_tip) in remaining.items():
        levels = []
        for i, (goal, solution, required) in enumerate(items, start=1):
            levels.append(dict(
                goal=goal,
                build=f"Level {i} erweitert das Thema Schritt für Schritt und nutzt neuen Code statt nur Wiederholung.",
                why=theme_tip,
                concept=f"{title.split('–',1)[1].strip()} – Level {i}",
                tip=f"Tipp: {theme_tip} In diesem Level ist wichtig: {goal}",
                hint1=f"Lies zuerst das Ziel: {goal} Baue die Lösung in kleinen Zeilen auf und prüfe danach die Checkliste.",
                required=required,
                partial=solution,
                solution=solution,
            ))
        task_specs.append((title, levels))

    for title, levels_data in task_specs:
        tasks.append(progressive_task(title, levels_data))

    # ---------------- SQL-Aufgaben 16–20: „fett“ und lernfreundlich ----------------noch unvollständig in der Erklärung
    # Gemeinsames Szenario:
    # Tabelle users(id, name, age, city)
    # Tabelle orders(id, user_id, amount, status)

    # ---------- Aufgabe 16 – SQL SELECT ----------
    levels_16 = [
        {
            "description": (
                "Aufgabe 16 – SQL SELECT – Level 1\n\n"
                "Ziel: Schreibe eine einfache SELECT-Abfrage, die alle Spalten aus der Tabelle users zurückgibt.\n\n"
                "Datenbankszenario:\n"
                "Tabelle users:\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SQL-Abfrage.\n"
                "- Sie soll alle Spalten und alle Zeilen aus users liefern.\n\n"
                "Anforderungen:\n"
                "- Verwende SELECT und FROM.\n"
                "- Nutze den Tabellennamen users.\n"
                "- Schreibe eine Abfrage der Form: SELECT * FROM users;\n"
            ),
            "concept": "eine einfache SELECT * FROM ... Abfrage schreiben",
            "hints": [
                "Hinweis 1 (Grundform):\n\n"
                "Die einfachste Form ist:\n"
                "    SELECT * FROM users;\n\n"
                "SELECT wählt Spalten, * bedeutet alle Spalten, FROM gibt die Tabelle an.",
                "Hinweis 2 (Details):\n\n"
                "- SQL-Schlüsselwörter werden oft groß geschrieben (SELECT, FROM).\n"
                "- Das Semikolon ; beendet die Anweisung.\n"
                "- Du kannst auch explizit Spalten wählen, z.B. SELECT id, name FROM users;",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users;\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users"
            ]
        },
        {
            "description": (
                "Aufgabe 16 – SQL SELECT – Level 2\n\n"
                "Ziel: Gib nur die Spalten name und city aus der Tabelle users zurück.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit expliziten Spalten.\n"
                "- Es sollen nur name und city zurückgegeben werden.\n\n"
                "Anforderungen:\n"
                "- Verwende SELECT name, city FROM users;\n"
            ),
            "concept": "nur bestimmte Spalten mit SELECT spalte1, spalte2 FROM ... auswählen",
            "hints": [
                "Hinweis 1:\n\n"
                "Du kannst mehrere Spalten mit Komma trennen:\n"
                "    SELECT name, city FROM users;\n",
                "Hinweis 2:\n\n"
                "Die Reihenfolge der Spalten in SELECT bestimmt die Reihenfolge im Ergebnis.",
                "Beispiel-Lösung:\n\n"
                "SELECT name, city FROM users;\n"
            ],
            "required": [
                "SELECT",
                "name",
                "city",
                "FROM",
                "users"
            ]
        },
        {
            "description": (
                "Aufgabe 16 – SQL SELECT – Level 3\n\n"
                "Ziel: Gib alle Benutzer aus, sortiert nach age aufsteigend.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit ORDER BY.\n"
                "- Sortiere nach age aufsteigend (ASC).\n\n"
                "Anforderungen:\n"
                "- Verwende ORDER BY age ASC.\n"
            ),
            "concept": "Ergebnisse mit ORDER BY sortieren",
            "hints": [
                "Hinweis 1:\n\n"
                "Grundform:\n"
                "    SELECT * FROM users\n"
                "    ORDER BY age ASC;\n",
                "Hinweis 2:\n\n"
                "ASC bedeutet aufsteigend, DESC wäre absteigend.",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "ORDER BY age ASC;\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "ORDER BY",
                "age"
            ]
        },
        {
            "description": (
                "Aufgabe 16 – SQL SELECT – Level 4\n\n"
                "Ziel: Gib alle unterschiedlichen Städte (city) aus der Tabelle users zurück.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 25  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit DISTINCT.\n"
                "- Es sollen doppelte Städte nur einmal erscheinen.\n\n"
                "Anforderungen:\n"
                "- Verwende SELECT DISTINCT city FROM users;\n"
            ),
            "concept": "Duplikate mit DISTINCT entfernen",
            "hints": [
                "Hinweis 1:\n\n"
                "DISTINCT steht direkt nach SELECT:\n"
                "    SELECT DISTINCT city FROM users;\n",
                "Hinweis 2:\n\n"
                "Ohne DISTINCT würdest du Berlin mehrfach sehen.",
                "Beispiel-Lösung:\n\n"
                "SELECT DISTINCT city FROM users;\n"
            ],
            "required": [
                "SELECT",
                "DISTINCT",
                "city",
                "FROM",
                "users"
            ]
        },
        {
            "description": (
                "Aufgabe 16 – SQL SELECT – Level 5\n\n"
                "Ziel: Zähle, wie viele Benutzer es insgesamt gibt.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 25  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit COUNT().\n"
                "- Es soll die Anzahl der Zeilen in users gezählt werden.\n\n"
                "Anforderungen:\n"
                "- Verwende SELECT COUNT(*) FROM users;\n"
            ),
            "concept": "Zeilen mit COUNT(*) zählen",
            "hints": [
                "Hinweis 1:\n\n"
                "COUNT(*) zählt alle Zeilen:\n"
                "    SELECT COUNT(*) FROM users;\n",
                "Hinweis 2:\n\n"
                "Du kannst der Spalte auch einen Alias geben:\n"
                "    SELECT COUNT(*) AS user_count FROM users;",
                "Beispiel-Lösung:\n\n"
                "SELECT COUNT(*) FROM users;\n"
            ],
            "required": [
                "SELECT",
                "COUNT",
                "FROM",
                "users"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 16 – SQL SELECT", "levels": levels_16})

    # ---------- Aufgabe 17 – SQL WHERE ----------
    levels_17 = [
        {
            "description": (
                "Aufgabe 17 – SQL WHERE – Level 1\n\n"
                "Ziel: Gib alle Benutzer aus, die älter als 25 Jahre sind.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 27  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit WHERE.\n"
                "- Bedingung: age > 25.\n\n"
                "Anforderungen:\n"
                "- Verwende WHERE age > 25.\n"
            ),
            "concept": "Zeilen mit WHERE und Vergleichsoperatoren filtern",
            "hints": [
                "Hinweis 1:\n\n"
                "Grundform:\n"
                "    SELECT * FROM users\n"
                "    WHERE age > 25;\n",
                "Hinweis 2:\n\n"
                "Vergleichsoperatoren: >, <, >=, <=, =, <> (ungleich).",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "WHERE age > 25;\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "WHERE",
                "age",
                ">"
            ]
        },
        {
            "description": (
                "Aufgabe 17 – SQL WHERE – Level 2\n\n"
                "Ziel: Gib alle Benutzer aus, die in 'Berlin' wohnen.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 27  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine SELECT-Abfrage mit WHERE.\n"
                "- Bedingung: city = 'Berlin'.\n\n"
                "Anforderungen:\n"
                "- Verwende WHERE city = 'Berlin'.\n"
            ),
            "concept": "Zeilen mit WHERE und Gleichheitsbedingung filtern",
            "hints": [
                "Hinweis 1:\n\n"
                "Zeichenketten werden in Hochkommas geschrieben:\n"
                "    WHERE city = 'Berlin'\n",
                "Hinweis 2:\n\n"
                "Komplette Abfrage:\n"
                "    SELECT * FROM users\n"
                "    WHERE city = 'Berlin';",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "WHERE city = 'Berlin';\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "WHERE",
                "city",
                "Berlin"
            ]
        },
        {
            "description": (
                "Aufgabe 17 – SQL WHERE – Level 3\n\n"
                "Ziel: Gib alle Benutzer aus, die in Berlin wohnen UND älter als 25 sind.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 27  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du kombinierst Bedingungen mit AND.\n"
                "- city = 'Berlin' UND age > 25.\n\n"
                "Anforderungen:\n"
                "- Verwende WHERE city = 'Berlin' AND age > 25.\n"
            ),
            "concept": "Mehrere Bedingungen mit AND verknüpfen",
            "hints": [
                "Hinweis 1:\n\n"
                "Mehrere Bedingungen:\n"
                "    WHERE city = 'Berlin' AND age > 25\n",
                "Hinweis 2:\n\n"
                "Komplette Abfrage:\n"
                "    SELECT * FROM users\n"
                "    WHERE city = 'Berlin' AND age > 25;",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "WHERE city = 'Berlin' AND age > 25;\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "WHERE",
                "city",
                "Berlin",
                "AND",
                "age",
                ">"
            ]
        },
        {
            "description": (
                "Aufgabe 17 – SQL WHERE – Level 4\n\n"
                "Ziel: Gib alle Benutzer aus, die NICHT in Berlin wohnen.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 27  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest eine Ungleichheitsbedingung.\n"
                "- city <> 'Berlin' oder city != 'Berlin' (je nach Dialekt).\n\n"
                "Anforderungen:\n"
                "- Verwende eine Bedingung, die 'nicht Berlin' ausdrückt.\n"
            ),
            "concept": "Ungleichheitsbedingungen in WHERE verwenden",
            "hints": [
                "Hinweis 1:\n\n"
                "In vielen SQL-Dialekten:\n"
                "    WHERE city <> 'Berlin'\n",
                "Hinweis 2:\n\n"
                "Komplette Abfrage:\n"
                "    SELECT * FROM users\n"
                "    WHERE city <> 'Berlin';",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "WHERE city <> 'Berlin';\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "WHERE",
                "city"
            ]
        },
        {
            "description": (
                "Aufgabe 17 – SQL WHERE – Level 5\n\n"
                "Ziel: Gib alle Benutzer aus, deren Alter zwischen 20 und 30 (inklusive) liegt.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n"
                "   4 | David   | 27  | Berlin\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest BETWEEN oder zwei Bedingungen mit AND.\n"
                "- 20 <= age <= 30.\n\n"
                "Anforderungen:\n"
                "- Verwende entweder BETWEEN 20 AND 30 oder age >= 20 AND age <= 30.\n"
            ),
            "concept": "Bereiche mit BETWEEN oder Kombination von Bedingungen abfragen",
            "hints": [
                "Hinweis 1 (BETWEEN):\n\n"
                "    SELECT * FROM users\n"
                "    WHERE age BETWEEN 20 AND 30;\n",
                "Hinweis 2 (Alternative):\n\n"
                "    SELECT * FROM users\n"
                "    WHERE age >= 20 AND age <= 30;",
                "Beispiel-Lösung:\n\n"
                "SELECT * FROM users\n"
                "WHERE age BETWEEN 20 AND 30;\n"
            ],
            "required": [
                "SELECT",
                "FROM",
                "users",
                "WHERE",
                "age"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 17 – SQL WHERE", "levels": levels_17})

    # ---------- Aufgabe 18 – SQL INSERT ----------
    levels_18 = [
        {
            "description": (
                "Aufgabe 18 – SQL INSERT – Level 1\n\n"
                "Ziel: Füge einen neuen Benutzer in die Tabelle users ein.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine INSERT-Anweisung.\n"
                "- Füge z.B. 'David', 27, 'Berlin' ein.\n\n"
                "Anforderungen:\n"
                "- Verwende INSERT INTO users (...spalten...) VALUES (...werte...);\n"
            ),
            "concept": "neue Zeilen mit INSERT INTO ... VALUES(...) einfügen",
            "hints": [
                "Hinweis 1 (Grundform):\n\n"
                "    INSERT INTO users (name, age, city)\n"
                "    VALUES ('David', 27, 'Berlin');\n",
                "Hinweis 2:\n\n"
                "Die Spaltenreihenfolge in Klammern muss zu den Werten passen.",
                "Beispiel-Lösung:\n\n"
                "INSERT INTO users (name, age, city)\n"
                "VALUES ('David', 27, 'Berlin');\n"
            ],
            "required": [
                "INSERT",
                "INTO",
                "users",
                "VALUES"
            ]
        },
        {
            "description": (
                "Aufgabe 18 – SQL INSERT – Level 2\n\n"
                "Ziel: Füge zwei neue Benutzer mit einer einzigen INSERT-Anweisung ein.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest mehrere VALUES-Blöcke.\n"
                "- Beispiel: ('Eva', 29, 'Köln') und ('Frank', 33, 'Leipzig').\n\n"
                "Anforderungen:\n"
                "- Verwende INSERT INTO users (name, age, city) VALUES (...), (...);\n"
            ),
            "concept": "mehrere Zeilen in einem INSERT mit mehreren VALUES-Blöcken einfügen",
            "hints": [
                "Hinweis 1:\n\n"
                "    INSERT INTO users (name, age, city)\n"
                "    VALUES ('Eva', 29, 'Köln'),\n"
                "           ('Frank', 33, 'Leipzig');\n",
                "Hinweis 2:\n\n"
                "Achte auf Kommas zwischen den VALUES-Blöcken.",
                "Beispiel-Lösung:\n\n"
                "INSERT INTO users (name, age, city)\n"
                "VALUES ('Eva', 29, 'Köln'),\n"
                "       ('Frank', 33, 'Leipzig');\n"
            ],
            "required": [
                "INSERT",
                "INTO",
                "users",
                "VALUES"
            ]
        },
        {
            "description": (
                "Aufgabe 18 – SQL INSERT – Level 3\n\n"
                "Ziel: Füge einen neuen Eintrag in die Tabelle orders ein.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine INSERT-Anweisung für orders.\n"
                "- Füge z.B. user_id=1, amount=99.50, status='open' ein.\n\n"
                "Anforderungen:\n"
                "- Verwende INSERT INTO orders (user_id, amount, status) VALUES (...);\n"
            ),
            "concept": "INSERT in eine zweite Tabelle mit Fremdschlüssel user_id",
            "hints": [
                "Hinweis 1:\n\n"
                "    INSERT INTO orders (user_id, amount, status)\n"
                "    VALUES (1, 99.50, 'open');\n",
                "Hinweis 2:\n\n"
                "user_id verweist auf die id in users.",
                "Beispiel-Lösung:\n\n"
                "INSERT INTO orders (user_id, amount, status)\n"
                "VALUES (1, 99.50, 'open');\n"
            ],
            "required": [
                "INSERT",
                "INTO",
                "orders",
                "VALUES"
            ]
        },
        {
            "description": (
                "Aufgabe 18 – SQL INSERT – Level 4\n\n"
                "Ziel: Füge eine Bestellung für einen neuen Benutzer ein, den du vorher in users anlegst.\n\n"
                "Datenbankszenario:\n"
                "- Tabelle users(id, name, age, city)\n"
                "- Tabelle orders(id, user_id, amount, status)\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst zwei INSERTs (nacheinander):\n"
                "  1) INSERT in users\n"
                "  2) INSERT in orders mit passender user_id\n\n"
                "Anforderungen:\n"
                "- Schreibe zwei INSERT-Anweisungen, eine für users, eine für orders.\n"
            ),
            "concept": "zusammenhängende INSERTs in verknüpfte Tabellen",
            "hints": [
                "Hinweis 1:\n\n"
                "Beispiel:\n"
                "    INSERT INTO users (name, age, city)\n"
                "    VALUES ('Gina', 28, 'Stuttgart');\n\n"
                "    INSERT INTO orders (user_id, amount, status)\n"
                "    VALUES (4, 59.90, 'open');\n"
                "(Hier wird angenommen, dass id=4 zu Gina gehört.)",
                "Hinweis 2:\n\n"
                "Wichtig ist das Prinzip: erst Benutzer, dann Bestellung mit passender user_id.",
                "Beispiel-Lösung (Prinzip):\n\n"
                "INSERT INTO users (name, age, city)\n"
                "VALUES ('Gina', 28, 'Stuttgart');\n\n"
                "INSERT INTO orders (user_id, amount, status)\n"
                "VALUES (4, 59.90, 'open');\n"
            ],
            "required": [
                "INSERT",
                "INTO",
                "users",
                "orders",
                "VALUES"
            ]
        },
        {
            "description": (
                "Aufgabe 18 – SQL INSERT – Level 5\n\n"
                "Ziel: Füge mehrere Bestellungen für denselben Benutzer in einer einzigen INSERT-Anweisung ein.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest mehrere VALUES-Blöcke in INSERT INTO orders.\n"
                "- Beispiel: zwei Bestellungen für user_id=1.\n\n"
                "Anforderungen:\n"
                "- Verwende INSERT INTO orders (user_id, amount, status) VALUES (...), (...);\n"
            ),
            "concept": "mehrere Bestellungen in einem INSERT für dieselbe user_id einfügen",
            "hints": [
                "Hinweis 1:\n\n"
                "    INSERT INTO orders (user_id, amount, status)\n"
                "    VALUES (1, 10.00, 'open'),\n"
                "           (1, 20.00, 'open');\n",
                "Hinweis 2:\n\n"
                "Beide Zeilen haben user_id=1, aber unterschiedliche amounts.",
                "Beispiel-Lösung:\n\n"
                "INSERT INTO orders (user_id, amount, status)\n"
                "VALUES (1, 10.00, 'open'),\n"
                "       (1, 20.00, 'open');\n"
            ],
            "required": [
                "INSERT",
                "INTO",
                "orders",
                "VALUES"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 18 – SQL INSERT", "levels": levels_18})

    # ---------- Aufgabe 19 – SQL UPDATE ----------
    levels_19 = [
        {
            "description": (
                "Aufgabe 19 – SQL UPDATE – Level 1\n\n"
                "Ziel: Setze den Status einer Bestellung auf 'paid'.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine UPDATE-Anweisung.\n"
                "- Aktualisiere z.B. die Bestellung mit id=1 auf status='paid'.\n\n"
                "Anforderungen:\n"
                "- Verwende UPDATE orders SET status = 'paid' WHERE id = 1;\n"
            ),
            "concept": "Zeilen mit UPDATE ... SET ... WHERE ... aktualisieren",
            "hints": [
                "Hinweis 1:\n\n"
                "    UPDATE orders\n"
                "    SET status = 'paid'\n"
                "    WHERE id = 1;\n",
                "Hinweis 2:\n\n"
                "Ohne WHERE würdest du alle Zeilen ändern – immer WHERE benutzen!",
                "Beispiel-Lösung:\n\n"
                "UPDATE orders\n"
                "SET status = 'paid'\n"
                "WHERE id = 1;\n"
            ],
            "required": [
                "UPDATE",
                "orders",
                "SET",
                "status",
                "WHERE"
            ]
        },
        {
            "description": (
                "Aufgabe 19 – SQL UPDATE – Level 2\n\n"
                "Ziel: Erhöhe den amount aller offenen Bestellungen ('open') um 5.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |  10.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest eine UPDATE-Anweisung mit Rechenoperation.\n"
                "- amount = amount + 5 für alle Zeilen mit status='open'.\n\n"
                "Anforderungen:\n"
                "- Verwende UPDATE orders SET amount = amount + 5 WHERE status = 'open';\n"
            ),
            "concept": "Spaltenwerte mit UPDATE und Rechenoperationen ändern",
            "hints": [
                "Hinweis 1:\n\n"
                "    UPDATE orders\n"
                "    SET amount = amount + 5\n"
                "    WHERE status = 'open';\n",
                "Hinweis 2:\n\n"
                "amount = amount + 5 bedeutet: nimm den alten Wert und addiere 5.",
                "Beispiel-Lösung:\n\n"
                "UPDATE orders\n"
                "SET amount = amount + 5\n"
                "WHERE status = 'open';\n"
            ],
            "required": [
                "UPDATE",
                "orders",
                "SET",
                "amount",
                "WHERE",
                "status"
            ]
        },
        {
            "description": (
                "Aufgabe 19 – SQL UPDATE – Level 3\n\n"
                "Ziel: Ändere die Stadt eines Benutzers in der Tabelle users.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 22  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine UPDATE-Anweisung für users.\n"
                "- Ändere z.B. city von Bob auf 'Köln'.\n\n"
                "Anforderungen:\n"
                "- Verwende UPDATE users SET city = 'Köln' WHERE name = 'Bob';\n"
            ),
            "concept": "UPDATE auf einer anderen Tabelle (users) mit WHERE-Bedingung",
            "hints": [
                "Hinweis 1:\n\n"
                "    UPDATE users\n"
                "    SET city = 'Köln'\n"
                "    WHERE name = 'Bob';\n",
                "Hinweis 2:\n\n"
                "Du kannst auch über id filtern, z.B. WHERE id = 2.",
                "Beispiel-Lösung:\n\n"
                "UPDATE users\n"
                "SET city = 'Köln'\n"
                "WHERE name = 'Bob';\n"
            ],
            "required": [
                "UPDATE",
                "users",
                "SET",
                "city",
                "WHERE"
            ]
        },
        {
            "description": (
                "Aufgabe 19 – SQL UPDATE – Level 4\n\n"
                "Ziel: Setze alle Bestellungen eines bestimmten Benutzers auf 'paid'.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |  10.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest WHERE user_id = ...\n"
                "- Setze z.B. alle Bestellungen von user_id=1 auf 'paid'.\n\n"
                "Anforderungen:\n"
                "- Verwende UPDATE orders SET status = 'paid' WHERE user_id = 1;\n"
            ),
            "concept": "UPDATE mit Filter auf Fremdschlüssel user_id",
            "hints": [
                "Hinweis 1:\n\n"
                "    UPDATE orders\n"
                "    SET status = 'paid'\n"
                "    WHERE user_id = 1;\n",
                "Hinweis 2:\n\n"
                "Damit werden alle Zeilen mit user_id=1 geändert.",
                "Beispiel-Lösung:\n\n"
                "UPDATE orders\n"
                "SET status = 'paid'\n"
                "WHERE user_id = 1;\n"
            ],
            "required": [
                "UPDATE",
                "orders",
                "SET",
                "status",
                "WHERE",
                "user_id"
            ]
        },
        {
            "description": (
                "Aufgabe 19 – SQL UPDATE – Level 5\n\n"
                "Ziel: Setze alle Bestellungen mit amount > 50 auf status 'review'.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |  60.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du kombinierst UPDATE mit einer WHERE-Bedingung auf amount.\n"
                "- Bedingung: amount > 50.\n\n"
                "Anforderungen:\n"
                "- Verwende UPDATE orders SET status = 'review' WHERE amount > 50;\n"
            ),
            "concept": "UPDATE mit numerischer Bedingung in WHERE",
            "hints": [
                "Hinweis 1:\n\n"
                "    UPDATE orders\n"
                "    SET status = 'review'\n"
                "    WHERE amount > 50;\n",
                "Hinweis 2:\n\n"
                "Nur Zeilen mit amount > 50 werden geändert.",
                "Beispiel-Lösung:\n\n"
                "UPDATE orders\n"
                "SET status = 'review'\n"
                "WHERE amount > 50;\n"
            ],
            "required": [
                "UPDATE",
                "orders",
                "SET",
                "status",
                "WHERE",
                "amount",
                ">"
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 19 – SQL UPDATE", "levels": levels_19})

    # ---------- Aufgabe 20 – SQL DELETE ----------
    levels_20 = [
        {
            "description": (
                "Aufgabe 20 – SQL DELETE – Level 1\n\n"
                "Ziel: Lösche eine Bestellung mit einer bestimmten id.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine DELETE-Anweisung.\n"
                "- Lösche z.B. die Bestellung mit id=2.\n\n"
                "Anforderungen:\n"
                "- Verwende DELETE FROM orders WHERE id = 2;\n"
            ),
            "concept": "Zeilen mit DELETE FROM ... WHERE ... löschen",
            "hints": [
                "Hinweis 1:\n\n"
                "    DELETE FROM orders\n"
                "    WHERE id = 2;\n",
                "Hinweis 2:\n\n"
                "Ohne WHERE würdest du alle Zeilen löschen – immer WHERE benutzen!",
                "Beispiel-Lösung:\n\n"
                "DELETE FROM orders\n"
                "WHERE id = 2;\n"
            ],
            "required": [
                "DELETE",
                "FROM",
                "orders",
                "WHERE"
            ]
        },
        {
            "description": (
                "Aufgabe 20 – SQL DELETE – Level 2\n\n"
                "Ziel: Lösche alle Bestellungen mit status 'open'.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |  10.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest WHERE status = 'open'.\n"
                "- Alle offenen Bestellungen sollen gelöscht werden.\n\n"
                "Anforderungen:\n"
                "- Verwende DELETE FROM orders WHERE status = 'open';\n"
            ),
            "concept": "DELETE mit Filter auf eine Status-Spalte",
            "hints": [
                "Hinweis 1:\n\n"
                "    DELETE FROM orders\n"
                "    WHERE status = 'open';\n",
                "Hinweis 2:\n\n"
                "Nur Zeilen mit status='open' werden gelöscht.",
                "Beispiel-Lösung:\n\n"
                "DELETE FROM orders\n"
                "WHERE status = 'open';\n"
            ],
            "required": [
                "DELETE",
                "FROM",
                "orders",
                "WHERE",
                "status"
            ]
        },
        {
            "description": (
                "Aufgabe 20 – SQL DELETE – Level 3\n\n"
                "Ziel: Lösche alle Benutzer, die jünger als 18 sind.\n\n"
                "Datenbankszenario (users):\n"
                "  id | name    | age | city\n"
                "  ---+---------+-----+---------\n"
                "   1 | Alice   | 25  | Berlin\n"
                "   2 | Bob     | 31  | Hamburg\n"
                "   3 | Carla   | 16  | München\n\n"
                "Struktur der Aufgabe:\n"
                "- Du schreibst eine DELETE-Anweisung für users.\n"
                "- Bedingung: age < 18.\n\n"
                "Anforderungen:\n"
                "- Verwende DELETE FROM users WHERE age < 18;\n"
            ),
            "concept": "DELETE mit numerischer Bedingung in WHERE",
            "hints": [
                "Hinweis 1:\n\n"
                "    DELETE FROM users\n"
                "    WHERE age < 18;\n",
                "Hinweis 2:\n\n"
                "Damit entfernst du alle Minderjährigen aus der Tabelle.",
                "Beispiel-Lösung:\n\n"
                "DELETE FROM users\n"
                "WHERE age < 18;\n"
            ],
            "required": [
                "DELETE",
                "FROM",
                "users",
                "WHERE",
                "age",
                "<"
            ]
        },
        {
            "description": (
                "Aufgabe 20 – SQL DELETE – Level 4\n\n"
                "Ziel: Lösche alle Bestellungen eines bestimmten Benutzers.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |  10.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest WHERE user_id = ...\n"
                "- Lösche z.B. alle Bestellungen von user_id=1.\n\n"
                "Anforderungen:\n"
                "- Verwende DELETE FROM orders WHERE user_id = 1;\n"
            ),
            "concept": "DELETE mit Filter auf Fremdschlüssel user_id",
            "hints": [
                "Hinweis 1:\n\n"
                "    DELETE FROM orders\n"
                "    WHERE user_id = 1;\n",
                "Hinweis 2:\n\n"
                "Damit entfernst du alle Bestellungen dieses Benutzers.",
                "Beispiel-Lösung:\n\n"
                "DELETE FROM orders\n"
                "WHERE user_id = 1;\n"
            ],
            "required": [
                "DELETE",
                "FROM",
                "orders",
                "WHERE",
                "user_id"
            ]
        },
        {
            "description": (
                "Aufgabe 20 – SQL DELETE – Level 5\n\n"
                "Ziel: Lösche alle Bestellungen mit amount = 0.\n\n"
                "Datenbankszenario (orders):\n"
                "  id | user_id | amount | status\n"
                "  ---+---------+--------+--------\n"
                "   1 | 1       |  49.99 | 'open'\n"
                "   2 | 2       |  19.00 | 'paid'\n"
                "   3 | 1       |   0.00 | 'open'\n\n"
                "Struktur der Aufgabe:\n"
                "- Du verwendest eine Bedingung auf amount.\n"
                "- Lösche alle Zeilen mit amount = 0.\n\n"
                "Anforderungen:\n"
                "- Verwende DELETE FROM orders WHERE amount = 0;\n"
            ),
            "concept": "DELETE mit exakter numerischer Bedingung",
            "hints": [
                "Hinweis 1:\n\n"
                "    DELETE FROM orders\n"
                "    WHERE amount = 0;\n",
                "Hinweis 2:\n\n"
                "Damit entfernst du alle Bestellungen ohne Betrag.",
                "Beispiel-Lösung:\n\n"
                "DELETE FROM orders\n"
                "WHERE amount = 0;\n"
            ],
            "required": [
                "DELETE",
                "FROM",
                "orders",
                "WHERE",
                "amount",
                "="
            ]
        }
    ]
    tasks.append({"title": "Aufgabe 20 – SQL DELETE", "levels": levels_20})



    # ---------------- v15: echte aufbauende Lernpfade ----------------
    # Aufgaben 3–20 werden hier bewusst neu gesetzt: Jede Aufgabe ist ein eigenes Mini-Projekt.
    # Level 1–5 erweitern jeweils den Code/SQL-Text des vorherigen Levels.
    def make_progressive_level(title, level_no, goal, concept, tip, solution, required, partial=None):
        solution = solution.strip() + "\n"
        if partial is None:
            # Für Hinweis 2 wird die Lösung nicht versteckt, sondern als fast fertige Struktur gezeigt.
            # Einzelne letzte Zeilen werden als Lernlücke markiert; Hinweis 3 bleibt immer 100% Code.
            lines = solution.rstrip().splitlines()
            if len(lines) >= 4:
                partial = "\n".join(lines[:-2] + ["    # ergänze hier die letzten passenden Zeilen", lines[-1]])
            else:
                partial = solution.rstrip()
        return {
            "description": (
                f"{title} – Level {level_no}\n\n"
                f"Ziel: {goal}\n\n"
                "Dieses Level erweitert den bisherigen Code dieser Aufgabe. "
                "Übernimm die Grundidee aus dem vorherigen Level und ergänze nur den neuen Lernschritt.\n\n"
                "Anforderungen:\n" + "\n".join(f"- {r}" for r in required)
            ),
            "concept": concept,
            "work_tip": tip,
            "hints": [
                "Denke zuerst über den Ablauf nach:\n\n" + tip + "\n\nSchreibe dann die Grundstruktur und prüfe die Checkliste.",
                "Fast fertige Struktur zum Weiterdenken:\n\n" + partial.strip(),
                "Vollständige Lösung zum Abschreiben:\n\n" + solution,
            ],
            "required": required,
        }

    def py_task(title, rows):
        levels=[]
        for i,row in enumerate(rows,1):
            goal, concept, tip, code, required = row
            levels.append(make_progressive_level(title, i, goal, concept, tip, code, required))
        return {"title": title, "levels": levels}

    python_projects = [
        py_task("Aufgabe 3 – Zahlenanalyse mit Schleifen", [
            ("Gib Zahlen von 1 bis 5 aus.", "for-Schleife mit range", "Die Schleife wiederholt denselben Befehl für mehrere Zahlen. range(1, 6) liefert 1 bis 5, weil der Endwert nicht mehr enthalten ist.", """
def loops_lvl1():
    for zahl in range(1, 6):
        print(zahl)

loops_lvl1()
""", ["def loops_lvl1", "for zahl in range(1, 6)", "print(zahl)", "loops_lvl1("]),
            ("Speichere diese Zahlen zusätzlich in einer Liste.", "Schleife füllt eine Liste", "Die Liste zahlen sammelt Werte. append() hängt in jedem Durchlauf die aktuelle Zahl hinten an.", """
def loops_lvl2():
    zahlen = []
    for zahl in range(1, 6):
        zahlen.append(zahl)
        print(zahl)
    print(zahlen)

loops_lvl2()
""", ["def loops_lvl2", "zahlen = []", "zahlen.append(zahl)", "print(zahlen)", "loops_lvl2("]),
            ("Berechne die Summe der gespeicherten Zahlen.", "laufende Summe", "summe startet bei 0. Jede Zahl wird addiert, dadurch entsteht am Ende die Gesamtsumme.", """
def loops_lvl3():
    zahlen = []
    summe = 0
    for zahl in range(1, 6):
        zahlen.append(zahl)
        summe = summe + zahl
    print(zahlen)
    print(summe)

loops_lvl3()
""", ["def loops_lvl3", "summe = 0", "summe = summe + zahl", "print(summe)", "loops_lvl3("]),
            ("Zähle zusätzlich nur die geraden Zahlen.", "Bedingung in der Schleife", "Mit zahl % 2 == 0 prüfst du, ob eine Zahl gerade ist. Nur dann wird der Gerade-Zähler erhöht.", """
def loops_lvl4():
    zahlen = []
    summe = 0
    gerade = 0
    for zahl in range(1, 11):
        zahlen.append(zahl)
        summe = summe + zahl
        if zahl % 2 == 0:
            gerade = gerade + 1
    print(zahlen)
    print(summe)
    print(gerade)

loops_lvl4()
""", ["def loops_lvl4", "if zahl % 2 == 0", "gerade = gerade + 1", "print(gerade)", "loops_lvl4("]),
            ("Gib einen kleinen Analysebericht aus.", "Schleife, Liste, Summe und Auswertung", "Der Bericht verbindet alle vorherigen Teile: Liste erzeugen, Summe berechnen, gerade Zahlen zählen und verständlich ausgeben.", """
def loops_lvl5():
    zahlen = []
    summe = 0
    gerade = 0
    for zahl in range(1, 11):
        zahlen.append(zahl)
        summe = summe + zahl
        if zahl % 2 == 0:
            gerade = gerade + 1
    print(f"Zahlen: {zahlen}")
    print(f"Summe: {summe}")
    print(f"Gerade Zahlen: {gerade}")

loops_lvl5()
""", ["def loops_lvl5", "print(f\"Zahlen:", "print(f\"Summe:", "print(f\"Gerade Zahlen:", "loops_lvl5("]),
        ]),
        py_task("Aufgabe 4 – Kontaktliste", [
            ("Lege eine Namensliste an und gib sie aus.", "Liste erstellen", "Eine Liste fasst mehrere Namen in einer Variable zusammen. So kann das Programm später mit allen Namen arbeiten.", """
def lists_lvl1():
    kontakte = ['Anna', 'Ben', 'Carla']
    print(kontakte)

lists_lvl1()
""", ["def lists_lvl1", "kontakte =", "Anna", "Ben", "Carla", "lists_lvl1("]),
            ("Gib den ersten und letzten Kontakt einzeln aus.", "Indexzugriff", "Python zählt ab 0. kontakte[0] ist der erste Eintrag, kontakte[-1] ist der letzte Eintrag.", """
def lists_lvl2():
    kontakte = ['Anna', 'Ben', 'Carla']
    print(kontakte[0])
    print(kontakte[-1])

lists_lvl2()
""", ["def lists_lvl2", "kontakte[0]", "kontakte[-1]", "lists_lvl2("]),
            ("Füge einen neuen Kontakt hinzu.", "Liste verändern", "append() verändert die vorhandene Liste und hängt den neuen Namen hinten an.", """
def lists_lvl3():
    kontakte = ['Anna', 'Ben', 'Carla']
    kontakte.append('David')
    print(kontakte)

lists_lvl3()
""", ["def lists_lvl3", "kontakte.append('David')", "print(kontakte)", "lists_lvl3("]),
            ("Gib jeden Kontakt sauber nummeriert aus.", "Liste mit enumerate durchlaufen", "enumerate liefert Position und Wert. start=1 sorgt dafür, dass die Anzeige für Menschen bei 1 beginnt.", """
def lists_lvl4():
    kontakte = ['Anna', 'Ben', 'Carla']
    kontakte.append('David')
    for nummer, name in enumerate(kontakte, start=1):
        print(f"{nummer}. {name}")

lists_lvl4()
""", ["def lists_lvl4", "enumerate(kontakte, start=1)", "print(f\"{nummer}.", "lists_lvl4("]),
            ("Baue eine kleine Kontaktübersicht mit Anzahl.", "Liste auswerten", "len(kontakte) zählt die Einträge. Danach zeigt die Schleife alle Kontakte als übersichtliche Ausgabe.", """
def lists_lvl5():
    kontakte = ['Anna', 'Ben', 'Carla']
    kontakte.append('David')
    print(f"Kontakte insgesamt: {len(kontakte)}")
    for nummer, name in enumerate(kontakte, start=1):
        print(f"{nummer}. {name}")

lists_lvl5()
""", ["def lists_lvl5", "len(kontakte)", "for nummer, name", "lists_lvl5("]),
        ]),
        py_task("Aufgabe 5 – Passwortprüfung", [
            ("Prüfe, ob ein Passwort lang genug ist.", "if-Bedingung", "len(passwort) liefert die Länge. Die if-Abfrage entscheidet, welche Meldung angezeigt wird.", """
def conds_lvl1():
    passwort = 'abc12345'
    if len(passwort) >= 8:
        print('lang genug')
    else:
        print('zu kurz')

conds_lvl1()
""", ["def conds_lvl1", "len(passwort) >= 8", "else", "conds_lvl1("]),
            ("Prüfe zusätzlich, ob eine Zahl enthalten ist.", "any() mit Schleife über Zeichen", "any(zeichen.isdigit() for zeichen in passwort) wird wahr, sobald mindestens ein Zeichen eine Ziffer ist.", """
def conds_lvl2():
    passwort = 'abc12345'
    hat_zahl = any(zeichen.isdigit() for zeichen in passwort)
    if len(passwort) >= 8 and hat_zahl:
        print('besseres Passwort')
    else:
        print('Passwort verbessern')

conds_lvl2()
""", ["def conds_lvl2", "hat_zahl", "isdigit()", "and hat_zahl", "conds_lvl2("]),
            ("Prüfe zusätzlich Großbuchstaben.", "mehrere Bedingungen kombinieren", "and bedeutet: Alle Bedingungen müssen stimmen, damit das Passwort akzeptiert wird.", """
def conds_lvl3():
    passwort = 'Abc12345'
    hat_zahl = any(zeichen.isdigit() for zeichen in passwort)
    hat_gross = any(zeichen.isupper() for zeichen in passwort)
    if len(passwort) >= 8 and hat_zahl and hat_gross:
        print('sicher')
    else:
        print('unsicher')

conds_lvl3()
""", ["def conds_lvl3", "isupper()", "hat_gross", "and hat_gross", "conds_lvl3("]),
            ("Gib eine genaue Fehlermeldung aus.", "gezielte Prüfungen", "Mehrere if-Blöcke erklären dem Nutzer genau, was fehlt, statt nur falsch zu melden.", """
def conds_lvl4():
    passwort = 'abc123'
    if len(passwort) < 8:
        print('Mindestens 8 Zeichen verwenden')
    if not any(zeichen.isdigit() for zeichen in passwort):
        print('Mindestens eine Zahl verwenden')
    if not any(zeichen.isupper() for zeichen in passwort):
        print('Mindestens einen Großbuchstaben verwenden')

conds_lvl4()
""", ["def conds_lvl4", "if len(passwort) < 8", "not any", "conds_lvl4("]),
            ("Baue eine vollständige Passwortbewertung.", "Validierung mit Statusvariable", "Die Variable sicher merkt sich, ob ein Problem gefunden wurde. Am Ende entscheidet sie über die Abschlussmeldung.", """
def conds_lvl5():
    passwort = 'Abc12345'
    sicher = True
    if len(passwort) < 8:
        print('Mindestens 8 Zeichen verwenden')
        sicher = False
    if not any(zeichen.isdigit() for zeichen in passwort):
        print('Mindestens eine Zahl verwenden')
        sicher = False
    if not any(zeichen.isupper() for zeichen in passwort):
        print('Mindestens einen Großbuchstaben verwenden')
        sicher = False
    if sicher:
        print('Passwort ist sicher')

conds_lvl5()
""", ["def conds_lvl5", "sicher = True", "sicher = False", "if sicher", "conds_lvl5("]),
        ]),
        py_task("Aufgabe 6 – Rabattrechner", [
            ("Schreibe eine Funktion, die einen Preis zurückgibt.", "Funktion mit return", "return gibt einen Wert an die aufrufende Stelle zurück. Dadurch kann man mit dem Ergebnis weiterarbeiten.", """
def funcs_lvl1(preis):
    return preis

print(funcs_lvl1(100))
""", ["def funcs_lvl1(preis)", "return preis", "print(funcs_lvl1(100))"]),
            ("Berechne 10 Prozent Rabatt.", "Parameter und Rechnung", "Der Parameter preis wird in der Funktion verwendet. preis * 0.9 bedeutet: 90 Prozent des ursprünglichen Preises.", """
def funcs_lvl2(preis):
    rabattpreis = preis * 0.9
    return rabattpreis

print(funcs_lvl2(100))
""", ["def funcs_lvl2(preis)", "rabattpreis = preis * 0.9", "return rabattpreis"]),
            ("Übergib den Rabatt als zweiten Parameter.", "mehrere Parameter", "Mit rabatt_prozent wird die Funktion flexibler. Der Faktor wird aus dem Prozentwert berechnet.", """
def funcs_lvl3(preis, rabatt_prozent):
    faktor = 1 - rabatt_prozent / 100
    rabattpreis = preis * faktor
    return rabattpreis

print(funcs_lvl3(100, 20))
""", ["def funcs_lvl3(preis, rabatt_prozent)", "faktor = 1 - rabatt_prozent / 100", "print(funcs_lvl3(100, 20))"]),
            ("Runde das Ergebnis auf zwei Nachkommastellen.", "round() verwenden", "round(wert, 2) macht Geldbeträge lesbarer, weil nur zwei Nachkommastellen angezeigt werden.", """
def funcs_lvl4(preis, rabatt_prozent):
    faktor = 1 - rabatt_prozent / 100
    rabattpreis = preis * faktor
    return round(rabattpreis, 2)

print(funcs_lvl4(99.99, 15))
""", ["def funcs_lvl4", "round(rabattpreis, 2)", "print(funcs_lvl4(99.99, 15))"]),
            ("Gib einen vollständigen Rabattbericht aus.", "Funktion plus formatierte Ausgabe", "Die Funktion berechnet nur. Die Ausgabe erklärt dem Nutzer danach den alten Preis, Rabatt und Endpreis.", """
def funcs_lvl5(preis, rabatt_prozent):
    faktor = 1 - rabatt_prozent / 100
    rabattpreis = preis * faktor
    return round(rabattpreis, 2)

alter_preis = 99.99
rabatt = 15
neuer_preis = funcs_lvl5(alter_preis, rabatt)
print(f"Alter Preis: {alter_preis} Euro")
print(f"Rabatt: {rabatt}%")
print(f"Neuer Preis: {neuer_preis} Euro")
""", ["def funcs_lvl5", "alter_preis", "neuer_preis = funcs_lvl5", "print(f\"Neuer Preis:"]),
        ]),
        py_task("Aufgabe 7 – Bankkonto-Klasse", [
            ("Erstelle eine Klasse Bankkonto mit Besitzer.", "Klasse und Konstruktor", "__init__ läuft beim Erstellen des Objekts. self.besitzer speichert den Namen im Objekt.", """
class Bankkonto:
    def __init__(self, besitzer):
        self.besitzer = besitzer

konto = Bankkonto('Anna')
print(konto.besitzer)
""", ["class Bankkonto", "def __init__(self, besitzer)", "self.besitzer", "Bankkonto('Anna')"]),
            ("Speichere zusätzlich den Kontostand.", "Objektattribute", "Jedes Konto bekommt eigene Daten. self.kontostand gehört zu genau diesem Objekt.", """
class Bankkonto:
    def __init__(self, besitzer):
        self.besitzer = besitzer
        self.kontostand = 0

konto = Bankkonto('Anna')
print(konto.kontostand)
""", ["self.kontostand = 0", "print(konto.kontostand)"]),
            ("Füge eine Methode einzahlen() hinzu.", "Methode verändert Objektzustand", "Eine Methode ist eine Funktion innerhalb der Klasse. Sie verändert hier den gespeicherten Kontostand.", """
class Bankkonto:
    def __init__(self, besitzer):
        self.besitzer = besitzer
        self.kontostand = 0

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

konto = Bankkonto('Anna')
konto.einzahlen(50)
print(konto.kontostand)
""", ["def einzahlen(self, betrag)", "self.kontostand = self.kontostand + betrag", "konto.einzahlen(50)"]),
            ("Füge eine Methode abheben() mit Prüfung hinzu.", "Methode mit Bedingung", "Vor dem Abheben prüft die Methode, ob genug Geld vorhanden ist. So entsteht sichere Programmlogik.", """
class Bankkonto:
    def __init__(self, besitzer):
        self.besitzer = besitzer
        self.kontostand = 0

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand = self.kontostand - betrag
        else:
            print('Nicht genug Guthaben')

konto = Bankkonto('Anna')
konto.einzahlen(50)
konto.abheben(20)
print(konto.kontostand)
""", ["def abheben(self, betrag)", "if betrag <= self.kontostand", "Nicht genug Guthaben"]),
            ("Gib eine übersichtliche Kontoauskunft aus.", "Klasse mit mehreren Methoden", "Die Klasse bündelt Daten und Verhalten: Besitzer, Kontostand, Einzahlung, Abhebung und Ausgabe gehören zusammen.", """
class Bankkonto:
    def __init__(self, besitzer):
        self.besitzer = besitzer
        self.kontostand = 0

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand = self.kontostand - betrag
        else:
            print('Nicht genug Guthaben')

    def anzeigen(self):
        print(f"{self.besitzer}: {self.kontostand} Euro")

konto = Bankkonto('Anna')
konto.einzahlen(50)
konto.abheben(20)
konto.anzeigen()
""", ["def anzeigen(self)", "print(f\"{self.besitzer}", "konto.anzeigen()"]),
        ]),
    ]

    # Weitere Python-Lernpfade werden kompakt generiert, aber mit unterschiedlichen Mini-Projekten.
    more_py = [
        ("Aufgabe 8 – Notizen-Datei", "files", "notizen.txt", ["Text in eine Datei schreiben", "Datei wieder lesen", "Weitere Zeile anhängen", "Alle Zeilen nummeriert anzeigen", "Notiz-App mit schreiben und lesen"]),
        ("Aufgabe 9 – Sicherer Zahlenumwandler", "errors", "zahl", ["Text in Zahl umwandeln", "Fehler mit try/except abfangen", "Mehrere Eingaben prüfen", "Nur gültige Zahlen sammeln", "Durchschnitt gültiger Zahlen berechnen"]),
        ("Aufgabe 10 – Mathe-Modul verwenden", "mods", "math", ["math importieren", "Quadratwurzel berechnen", "Zahl aufrunden", "Kreisfläche berechnen", "Mathe-Bericht ausgeben"]),
        ("Aufgabe 11 – Mini-Kalkulator", "calc", "rechnen", ["Zwei Zahlen addieren", "Subtraktion ergänzen", "Multiplikation ergänzen", "Operator auswerten", "Vier Rechenarten als Bericht"]),
        ("Aufgabe 12 – Klickzähler", "click", "count", ["Zähler anlegen", "Zähler erhöhen", "Mehrere Klicks simulieren", "Funktion click() bauen", "Tkinter-Klickzähler bauen"]),
        ("Aufgabe 13 – Canvas-Zeichnung", "canvas", "canvas", ["Canvas-Fenster erstellen", "Rechteck zeichnen", "Kreis ergänzen", "Text ergänzen", "Komplette kleine Zeichnung bauen"]),
        ("Aufgabe 14 – Layout-App", "layout", "layout", ["Frame erstellen", "Labels untereinander", "Labels nebeneinander", "grid-Formular", "Zweigeteiltes Layout"]),
        ("Aufgabe 15 – To-do Mini-App", "miniapp", "todo", ["Fenster erstellen", "Entry und Button", "Eingabe anzeigen", "Liste von Einträgen", "Fertige To-do-App"]),
    ]

    def generated_more_task(title, base, keyword, goals):
        rows=[]
        for i, goal in enumerate(goals, 1):
            fname=f"{base}_lvl{i}"
            if base == "files":
                codes=[
"""def files_lvl1():
    with open('notizen.txt', 'w', encoding='utf-8') as datei:
        datei.write('Erste Notiz')
    print('Notiz gespeichert')

files_lvl1()""",
"""def files_lvl2():
    with open('notizen.txt', 'w', encoding='utf-8') as datei:
        datei.write('Erste Notiz')
    with open('notizen.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
    print(inhalt)

files_lvl2()""",
"""def files_lvl3():
    with open('notizen.txt', 'w', encoding='utf-8') as datei:
        datei.write('Erste Notiz\\n')
    with open('notizen.txt', 'a', encoding='utf-8') as datei:
        datei.write('Zweite Notiz\\n')
    with open('notizen.txt', 'r', encoding='utf-8') as datei:
        print(datei.read())

files_lvl3()""",
"""def files_lvl4():
    with open('notizen.txt', 'w', encoding='utf-8') as datei:
        datei.write('Erste Notiz\\nZweite Notiz\\n')
    with open('notizen.txt', 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()
    for nummer, zeile in enumerate(zeilen, start=1):
        print(f'{nummer}: {zeile.strip()}')

files_lvl4()""",
"""def files_lvl5():
    notizen = ['Python üben', 'SQL lernen', 'Projekt fertig bauen']
    with open('notizen.txt', 'w', encoding='utf-8') as datei:
        for notiz in notizen:
            datei.write(notiz + '\\n')
    with open('notizen.txt', 'r', encoding='utf-8') as datei:
        for nummer, zeile in enumerate(datei, start=1):
            print(f'{nummer}: {zeile.strip()}')

files_lvl5()"""]
            elif base == "errors":
                codes=[
"""def errors_lvl1():
    text = '42'
    zahl = int(text)
    print(zahl)

errors_lvl1()""",
"""def errors_lvl2():
    text = 'abc'
    try:
        zahl = int(text)
        print(zahl)
    except ValueError:
        print('Das ist keine Zahl')

errors_lvl2()""",
"""def errors_lvl3():
    eingaben = ['10', 'abc', '20']
    for text in eingaben:
        try:
            zahl = int(text)
            print(zahl)
        except ValueError:
            print(f'{text} ist ungültig')

errors_lvl3()""",
"""def errors_lvl4():
    eingaben = ['10', 'abc', '20']
    zahlen = []
    for text in eingaben:
        try:
            zahlen.append(int(text))
        except ValueError:
            print(f'{text} ist ungültig')
    print(zahlen)

errors_lvl4()""",
"""def errors_lvl5():
    eingaben = ['10', 'abc', '20', '30']
    zahlen = []
    for text in eingaben:
        try:
            zahlen.append(int(text))
        except ValueError:
            print(f'{text} ist ungültig')
    durchschnitt = sum(zahlen) / len(zahlen)
    print(f'Durchschnitt: {durchschnitt}')

errors_lvl5()"""]
            elif base == "mods":
                codes=[
"""import math

def mods_lvl1():
    print(math.pi)

mods_lvl1()""",
"""import math

def mods_lvl2():
    wurzel = math.sqrt(81)
    print(wurzel)

mods_lvl2()""",
"""import math

def mods_lvl3():
    wert = 4.2
    print(math.ceil(wert))

mods_lvl3()""",
"""import math

def mods_lvl4():
    radius = 5
    flaeche = math.pi * radius ** 2
    print(flaeche)

mods_lvl4()""",
"""import math

def mods_lvl5():
    radius = 5
    flaeche = math.pi * radius ** 2
    umfang = 2 * math.pi * radius
    print(f'Radius: {radius}')
    print(f'Fläche: {round(flaeche, 2)}')
    print(f'Umfang: {round(umfang, 2)}')

mods_lvl5()"""]
            elif base == "calc":
                codes=[
"""def calc_lvl1():
    a = 8
    b = 2
    print(a + b)

calc_lvl1()""",
"""def calc_lvl2():
    a = 8
    b = 2
    print(a + b)
    print(a - b)

calc_lvl2()""",
"""def calc_lvl3():
    a = 8
    b = 2
    print(a + b)
    print(a - b)
    print(a * b)

calc_lvl3()""",
"""def calc_lvl4():
    a = 8
    b = 2
    operator = '*'
    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)
    elif operator == '*':
        print(a * b)

calc_lvl4()""",
"""def calc_lvl5():
    a = 8
    b = 2
    operator = '/'
    if operator == '+':
        ergebnis = a + b
    elif operator == '-':
        ergebnis = a - b
    elif operator == '*':
        ergebnis = a * b
    elif operator == '/':
        ergebnis = a / b
    print(f'{a} {operator} {b} = {ergebnis}')

calc_lvl5()"""]
            elif base == "click":
                codes=[
"""def click_lvl1():
    count = 0
    print(count)

click_lvl1()""",
"""def click_lvl2():
    count = 0
    count = count + 1
    print(count)

click_lvl2()""",
"""def click_lvl3():
    count = 0
    for klick in range(3):
        count = count + 1
    print(count)

click_lvl3()""",
"""def click_lvl4():
    count = 0
    def click():
        nonlocal count
        count = count + 1
        print(count)
    click()
    click()

click_lvl4()""",
"""import tkinter as tk

def click_lvl5():
    count = 0
    root = tk.Tk()
    label = tk.Label(root, text='0')
    label.pack()
    def click():
        nonlocal count
        count = count + 1
        label.config(text=str(count))
    tk.Button(root, text='Klick', command=click).pack()
    root.mainloop()

click_lvl5()"""]
            elif base == "canvas":
                codes=[
"""import tkinter as tk

def canvas_lvl1():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    root.mainloop()

canvas_lvl1()""",
"""import tkinter as tk

def canvas_lvl2():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    canvas.create_rectangle(40, 80, 140, 150)
    root.mainloop()

canvas_lvl2()""",
"""import tkinter as tk

def canvas_lvl3():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    canvas.create_rectangle(40, 80, 140, 150)
    canvas.create_oval(180, 60, 250, 130)
    root.mainloop()

canvas_lvl3()""",
"""import tkinter as tk

def canvas_lvl4():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    canvas.create_rectangle(40, 80, 140, 150)
    canvas.create_oval(180, 60, 250, 130)
    canvas.create_text(150, 30, text='Formen')
    root.mainloop()

canvas_lvl4()""",
"""import tkinter as tk

def canvas_lvl5():
    root = tk.Tk()
    root.title('Canvas Zeichnung')
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    canvas.create_rectangle(40, 80, 140, 150)
    canvas.create_oval(180, 60, 250, 130)
    canvas.create_line(20, 170, 280, 170)
    canvas.create_text(150, 30, text='Formen')
    root.mainloop()

canvas_lvl5()"""]
            elif base == "layout":
                codes=[
"""import tkinter as tk

def layout_lvl1():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    root.mainloop()

layout_lvl1()""",
"""import tkinter as tk

def layout_lvl2():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text='Oben').pack()
    tk.Label(frame, text='Unten').pack()
    root.mainloop()

layout_lvl2()""",
"""import tkinter as tk

def layout_lvl3():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text='Links').pack(side='left')
    tk.Label(frame, text='Rechts').pack(side='left')
    root.mainloop()

layout_lvl3()""",
"""import tkinter as tk

def layout_lvl4():
    root = tk.Tk()
    tk.Label(root, text='Name').grid(row=0, column=0)
    tk.Entry(root).grid(row=0, column=1)
    tk.Button(root, text='OK').grid(row=1, column=0, columnspan=2)
    root.mainloop()

layout_lvl4()""",
"""import tkinter as tk

def layout_lvl5():
    root = tk.Tk()
    root.title('Layout-App')
    left = tk.Frame(root)
    right = tk.Frame(root)
    left.pack(side='left', fill='both', expand=True)
    right.pack(side='right', fill='both', expand=True)
    tk.Label(left, text='Menü').pack()
    tk.Label(right, text='Inhalt').pack()
    root.mainloop()

layout_lvl5()"""]
            else:
                codes=[
"""import tkinter as tk

def miniapp_lvl1():
    root = tk.Tk()
    root.title('Mini-App')
    root.mainloop()

miniapp_lvl1()""",
"""import tkinter as tk

def miniapp_lvl2():
    root = tk.Tk()
    root.title('Mini-App')
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text='Speichern').pack()
    root.mainloop()

miniapp_lvl2()""",
"""import tkinter as tk

def miniapp_lvl3():
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    label = tk.Label(root, text='Noch leer')
    label.pack()
    def speichern():
        label.config(text=entry.get())
    tk.Button(root, text='Speichern', command=speichern).pack()
    root.mainloop()

miniapp_lvl3()""",
"""import tkinter as tk

def miniapp_lvl4():
    eintraege = []
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    label = tk.Label(root, text='[]')
    label.pack()
    def speichern():
        eintraege.append(entry.get())
        label.config(text=str(eintraege))
    tk.Button(root, text='Speichern', command=speichern).pack()
    root.mainloop()

miniapp_lvl4()""",
"""import tkinter as tk

def miniapp_lvl5():
    eintraege = []
    root = tk.Tk()
    root.title('To-do Mini-App')
    entry = tk.Entry(root)
    entry.pack()
    label = tk.Label(root, text='Noch keine Einträge')
    label.pack()
    def speichern():
        text = entry.get()
        if text != '':
            eintraege.append(text)
            label.config(text='\\n'.join(eintraege))
            entry.delete(0, 'end')
    tk.Button(root, text='Speichern', command=speichern).pack()
    root.mainloop()

miniapp_lvl5()"""]
            code=codes[i-1]
            req=[f"def {fname}", f"{fname}("]
            if "import tkinter" in code: req.insert(0,"import tkinter as tk")
            if "SELECT" in code.upper(): req.append("SELECT")
            rows.append((goal, f"{title.split('–',1)[1].strip()} – Level {i}", f"{goal}. Dieses Level erweitert das vorherige Ergebnis und zeigt konkret, welche neue Codezeile den nächsten Nutzen bringt.", code, req))
        return py_task(title, rows)

    for spec in more_py:
        python_projects.append(generated_more_task(*spec))

    # SQL als aufbauende Skripte: Level 5 enthält jeweils ein vollständiges kleines SQL-Skript.
    def sql_task(title, rows):
        levels=[]
        for i,(goal,tip,script,required) in enumerate(rows,1):
            levels.append(make_progressive_level(title, i, goal, title, tip, script, required, partial=script.strip()))
        return {"title": title, "levels": levels}

    sql_projects = [
        sql_task("Aufgabe 16 – SQL SELECT Bericht", [
            ("Zeige alle Benutzer.", "SELECT liest Daten. Sternchen bedeutet: alle Spalten anzeigen.", "SELECT * FROM users;", ["SELECT", "FROM", "users"]),
            ("Zeige nur name und city.", "Jetzt wählst du gezielt Spalten aus, statt alles anzuzeigen.", "SELECT name, city FROM users;", ["SELECT", "name", "city", "FROM", "users"]),
            ("Sortiere die Benutzer nach Alter.", "ORDER BY ordnet das Ergebnis. ASC bedeutet aufsteigend.", "SELECT name, age, city\nFROM users\nORDER BY age ASC;", ["ORDER BY", "age", "ASC"]),
            ("Zeige jede Stadt nur einmal.", "DISTINCT entfernt doppelte Werte im Ergebnis.", "SELECT DISTINCT city\nFROM users\nORDER BY city ASC;", ["DISTINCT", "city", "ORDER BY"]),
            ("Baue einen kleinen SELECT-Bericht mit Anzahl.", "COUNT(*) zählt Zeilen. Das Skript zeigt nun Liste, Städte und Gesamtzahl.", "SELECT name, age, city\nFROM users\nORDER BY age ASC;\n\nSELECT DISTINCT city\nFROM users\nORDER BY city ASC;\n\nSELECT COUNT(*) AS user_count\nFROM users;", ["COUNT", "user_count", "SELECT", "FROM", "users"]),
        ]),
        sql_task("Aufgabe 17 – SQL WHERE Filter", [
            ("Filtere Benutzer über 25.", "WHERE begrenzt Zeilen. Nur Datensätze mit age > 25 erscheinen.", "SELECT *\nFROM users\nWHERE age > 25;", ["WHERE", "age", ">"]),
            ("Filtere Benutzer aus Berlin.", "Textwerte stehen in Hochkommas. city = 'Berlin' prüft die Stadt.", "SELECT *\nFROM users\nWHERE city = 'Berlin';", ["WHERE", "city", "Berlin"]),
            ("Kombiniere Berlin und Alter.", "AND bedeutet: Beide Bedingungen müssen gleichzeitig stimmen.", "SELECT *\nFROM users\nWHERE city = 'Berlin' AND age > 25;", ["AND", "city", "age", ">"]),
            ("Zeige Benutzer, die nicht in Berlin wohnen.", "<> bedeutet ungleich. Dadurch werden alle anderen Städte angezeigt.", "SELECT *\nFROM users\nWHERE city <> 'Berlin';", ["WHERE", "city", "<>"]),
            ("Baue einen vollständigen Filterbericht.", "BETWEEN prüft einen Bereich inklusive Grenzen. Das Skript zeigt mehrere typische Filter.", "SELECT *\nFROM users\nWHERE city = 'Berlin' AND age > 25;\n\nSELECT *\nFROM users\nWHERE city <> 'Berlin';\n\nSELECT *\nFROM users\nWHERE age BETWEEN 20 AND 30;", ["BETWEEN", "20", "30", "WHERE"]),
        ]),
        sql_task("Aufgabe 18 – SQL INSERT Aufbau", [
            ("Füge einen Benutzer ein.", "INSERT legt eine neue Zeile an. Spaltenliste und VALUES müssen zusammenpassen.", "INSERT INTO users (name, age, city)\nVALUES ('David', 27, 'Berlin');", ["INSERT", "INTO", "users", "VALUES"]),
            ("Füge zwei Benutzer ein.", "Mehrere VALUES-Blöcke erzeugen mehrere neue Zeilen in einem Befehl.", "INSERT INTO users (name, age, city)\nVALUES ('Eva', 29, 'Köln'),\n       ('Frank', 33, 'Leipzig');", ["Eva", "Frank", "VALUES"]),
            ("Füge eine Bestellung ein.", "orders verweist mit user_id auf einen Benutzer aus users.", "INSERT INTO orders (user_id, amount, status)\nVALUES (1, 99.50, 'open');", ["orders", "user_id", "amount", "status"]),
            ("Lege Benutzer und passende Bestellung an.", "Erst entsteht der Benutzer, danach eine Bestellung mit passender user_id.", "INSERT INTO users (name, age, city)\nVALUES ('Gina', 28, 'Stuttgart');\n\nINSERT INTO orders (user_id, amount, status)\nVALUES (4, 59.90, 'open');", ["users", "orders", "VALUES"]),
            ("Baue ein vollständiges INSERT-Skript.", "Das Skript zeigt Benutzer, einzelne Bestellung und mehrere Bestellungen für denselben Benutzer.", "INSERT INTO users (name, age, city)\nVALUES ('Gina', 28, 'Stuttgart');\n\nINSERT INTO orders (user_id, amount, status)\nVALUES (4, 59.90, 'open');\n\nINSERT INTO orders (user_id, amount, status)\nVALUES (4, 10.00, 'open'),\n       (4, 20.00, 'open');", ["INSERT", "users", "orders", "10.00", "20.00"]),
        ]),
        sql_task("Aufgabe 19 – SQL UPDATE Wartung", [
            ("Setze eine Bestellung auf paid.", "UPDATE verändert vorhandene Daten. WHERE begrenzt die Änderung auf eine Zeile.", "UPDATE orders\nSET status = 'paid'\nWHERE id = 1;", ["UPDATE", "SET", "WHERE", "paid"]),
            ("Erhöhe offene Bestellungen um 5.", "amount = amount + 5 verwendet den alten Wert und speichert den erhöhten Wert.", "UPDATE orders\nSET amount = amount + 5\nWHERE status = 'open';", ["amount = amount + 5", "status", "open"]),
            ("Ändere die Stadt eines Benutzers.", "Auch users kann aktualisiert werden. WHERE name = 'Bob' wählt Bob aus.", "UPDATE users\nSET city = 'Köln'\nWHERE name = 'Bob';", ["UPDATE", "users", "city", "Bob"]),
            ("Setze alle Bestellungen eines Benutzers auf paid.", "WHERE user_id = 1 betrifft mehrere Bestellungen desselben Benutzers.", "UPDATE orders\nSET status = 'paid'\nWHERE user_id = 1;", ["user_id", "paid", "orders"]),
            ("Baue ein vollständiges UPDATE-Wartungsskript.", "Mehrere UPDATEs zeigen typische Wartung: Status, Betrag, Benutzerdaten und Review-Markierung.", "UPDATE orders\nSET status = 'paid'\nWHERE id = 1;\n\nUPDATE orders\nSET amount = amount + 5\nWHERE status = 'open';\n\nUPDATE users\nSET city = 'Köln'\nWHERE name = 'Bob';\n\nUPDATE orders\nSET status = 'review'\nWHERE amount > 50;", ["review", "amount > 50", "UPDATE", "WHERE"]),
        ]),
        sql_task("Aufgabe 20 – SQL DELETE Aufräumen", [
            ("Lösche eine Bestellung per id.", "DELETE entfernt Zeilen. Mit WHERE id = 2 wird nur eine bestimmte Bestellung gelöscht.", "DELETE FROM orders\nWHERE id = 2;", ["DELETE", "FROM", "orders", "WHERE"]),
            ("Lösche offene Bestellungen.", "WHERE status = 'open' entfernt nur offene Bestellungen.", "DELETE FROM orders\nWHERE status = 'open';", ["status", "open", "DELETE"]),
            ("Lösche minderjährige Benutzer.", "Die Bedingung age < 18 findet Benutzer unter 18 Jahren.", "DELETE FROM users\nWHERE age < 18;", ["users", "age", "<"]),
            ("Lösche Bestellungen eines Benutzers.", "user_id verbindet Bestellungen mit einem Benutzer. So entfernst du alle seine Bestellungen.", "DELETE FROM orders\nWHERE user_id = 1;", ["user_id", "DELETE", "orders"]),
            ("Baue ein vollständiges DELETE-Aufräumskript.", "Das Skript zeigt sichere Löschungen mit unterschiedlichen Bedingungen. Jede DELETE-Anweisung hat ein WHERE.", "DELETE FROM orders\nWHERE id = 2;\n\nDELETE FROM orders\nWHERE status = 'open';\n\nDELETE FROM users\nWHERE age < 18;\n\nDELETE FROM orders\nWHERE amount = 0;", ["amount = 0", "DELETE", "WHERE"]),
        ]),
    ]

    tasks[2:15] = python_projects
    tasks[15:20] = sql_projects

    # Fallback-Lerntipps für ältere, bereits manuell formulierte Aufgaben (1, 2 und SQL).
    # Dadurch enthält der mittlere Bereich in jedem einzelnen Level eine echte Erklärung.
    for task_index, task in enumerate(tasks):
        for level_index, level in enumerate(task.get("levels", [])):
            if level.get("work_tip"):
                continue
            concept = str(level.get("concept", "dieses Konzept"))
            title = task.get("title", "")
            if task_index >= 15:
                if "SELECT" in title:
                    level["work_tip"] = "Tipp: Diese Abfrage liest Daten. SELECT bestimmt die sichtbaren Spalten, FROM nennt die Tabelle und Zusatzteile wie ORDER BY, DISTINCT oder COUNT verändern das Ergebnis."
                elif "WHERE" in title:
                    level["work_tip"] = "Tipp: WHERE filtert Zeilen. Du baust zuerst SELECT ... FROM users und ergänzt danach die Bedingung, damit nur passende Datensätze angezeigt werden."
                elif "INSERT" in title:
                    level["work_tip"] = "Tipp: INSERT legt neue Zeilen an. Die Spalten in der Klammer müssen in derselben Reihenfolge zu den Werten hinter VALUES passen."
                elif "UPDATE" in title:
                    level["work_tip"] = "Tipp: UPDATE verändert vorhandene Zeilen. SET beschreibt den neuen Wert und WHERE schützt davor, versehentlich alle Zeilen zu ändern."
                elif "DELETE" in title:
                    level["work_tip"] = "Tipp: DELETE entfernt Zeilen. Schreibe immer eine WHERE-Bedingung, damit nur die gewünschten Datensätze gelöscht werden."
                else:
                    level["work_tip"] = "Tipp: Lies SQL wie einen Satz: Was soll passieren, in welcher Tabelle, und welche Bedingung grenzt die Daten ein?"
            elif task_index == 0:
                level["work_tip"] = "Tipp: Du baust Schritt für Schritt ein Tkinter-Fenster. root ist das Hauptfenster, Widgets werden daran befestigt und mainloop() hält die App sichtbar."
            elif task_index == 1:
                level["work_tip"] = "Tipp: Diese Eingabe-App verbindet Entry, Button und Label. entry.get() liest Text, label.config(...) zeigt ihn an und command verbindet den Button mit der Funktion."
            else:
                level["work_tip"] = f"Tipp: Dieses Level übt {concept}. Lies jede Zeile als Aktion: Welche Variable entsteht, welche Funktion wird aufgerufen und was verändert sich dadurch?"

    return tasks


class TrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python & SQL Lerntrainer – korrigierte Aufgaben")
        self.root.geometry("1500x900")
        self.root.configure(bg="#1e1e1e")

        self.tasks = build_tasks()
        self.num_tasks = len(self.tasks)
        self.levels_per_task = 5

        self.progress = self.load_progress()

        self.current_task_index = 0
        self.current_level_index = 0
        self.hints_used_current = 0
        self.current_attempt_hints = 0

        self.build_ui()
        self.update_ui_for_task_and_level()

    def normalize_progress(self, progress):
        """Ergänzt fehlende Fortschritts-/Hinweisschlüssel aus älteren Versionen."""
        if not isinstance(progress, dict):
            progress = {}
        progress.setdefault("tasks", {})
        for i in range(self.num_tasks):
            tkey = str(i)
            progress["tasks"].setdefault(tkey, {})
            progress["tasks"][tkey].setdefault("max_level", 0)
            progress["tasks"][tkey].setdefault("points", 0.0)
            progress["tasks"][tkey].setdefault("hints_used", {})
            progress["tasks"][tkey].setdefault("completed_code", {})
            for l in range(self.levels_per_task):
                progress["tasks"][tkey]["hints_used"].setdefault(str(l), 0)
                progress["tasks"][tkey]["completed_code"].setdefault(str(l), "")
        return progress

    def load_progress(self):
        progress = None
        if os.path.exists(PROGRESS_FILE):
            try:
                with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                    progress = json.load(f)
            except Exception:
                progress = None
        progress = self.normalize_progress(progress)
        self.save_progress(progress)
        return progress

    def save_progress(self, progress=None):
        if progress is None:
            progress = self.progress
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, ensure_ascii=False, indent=2)

    def reset_all(self):
        if not messagebox.askyesno(
            "Reset all",
            "Willst du wirklich ALLE Fortschritte und Punkte zurücksetzen?"
        ):
            return
        if os.path.exists(PROGRESS_FILE):
            try:
                os.remove(PROGRESS_FILE)
            except Exception:
                pass
        self.progress = self.load_progress()
        self.current_task_index = 0
        self.current_level_index = 0
        self.hints_used_current = 0
        self.current_attempt_hints = 0
        self.update_ui_for_task_and_level()
        messagebox.showinfo("Reset", "Alle Fortschritte wurden zurückgesetzt.")

    def build_ui(self):
        self.sidebar = tk.Frame(self.root, width=260, bg="#252526")
        self.sidebar.pack(side="left", fill="y")

        py_label = tk.Label(
            self.sidebar, text="Python", bg="#252526", fg="#ffffff",
            font=("Segoe UI", 12, "bold")
        )
        py_label.pack(pady=(10, 2))

        self.task_buttons = []
        for i in range(15):
            btn = tk.Button(
                self.sidebar,
                text=f"Aufgabe {i+1}",
                bg="#2d2d30",
                fg="#ffffff",
                activebackground="#3e3e42",
                activeforeground="#ffffff",
                relief="flat",
                command=lambda idx=i: self.select_task(idx),
                takefocus=0
            )
            btn.pack(fill="x", pady=2, padx=8)
            self.task_buttons.append(btn)

        sql_label = tk.Label(
            self.sidebar, text="SQL", bg="#252526", fg="#ffffff",
            font=("Segoe UI", 12, "bold")
        )
        sql_label.pack(pady=(15, 2))

        for i in range(15, 20):
            btn = tk.Button(
                self.sidebar,
                text=f"Aufgabe {i+1}",
                bg="#2d2d30",
                fg="#ffffff",
                activebackground="#3e3e42",
                activeforeground="#ffffff",
                relief="flat",
                command=lambda idx=i: self.select_task(idx),
                takefocus=0
            )
            btn.pack(fill="x", pady=2, padx=8)
            self.task_buttons.append(btn)

        self.reset_button = tk.Button(
            self.sidebar,
            text="Reset all",
            bg="#a83232",
            fg="#ffffff",
            activebackground="#c23b3b",
            activeforeground="#ffffff",
            relief="flat",
            command=self.reset_all,
            takefocus=0
        )
        self.reset_button.pack(fill="x", pady=(15, 5), padx=8)

        self.main = tk.Frame(self.root, bg="#1e1e1e")
        self.main.pack(side="right", expand=True, fill="both")

        # Kopfbereich: Titel links, Level-Navigation rechts
        self.top_frame = tk.Frame(self.main, bg="#1e1e1e")
        self.top_frame.pack(fill="x", pady=(10, 4))

        self.title_label = tk.Label(
            self.top_frame, text="", bg="#1e1e1e", fg="#ffffff",
            font=("Segoe UI", 16, "bold")
        )
        self.title_label.pack(side="left", padx=20)

        self.version_label = tk.Label(
            self.top_frame, text="Code-Trainer", bg="#264f78", fg="#ffffff",
            font=("Segoe UI", 9, "bold"), padx=8, pady=3
        )
        self.version_label.pack(side="left", padx=(0, 12))

        self.score_label = tk.Label(
            self.top_frame,
            text="",
            bg="#1e1e1e",
            fg="#ffd700",
            font=("Segoe UI", 13, "bold"),
            padx=18
        )
        self.score_label.pack(side="left", expand=True)

        self.level_buttons_frame = tk.Frame(self.top_frame, bg="#1e1e1e")
        self.level_buttons_frame.pack(side="right", padx=20)

        self.level_buttons = []
        for lvl in range(self.levels_per_task):
            b = tk.Button(
                self.level_buttons_frame,
                text=f"L{lvl+1}",
                bg="#2d2d30",
                fg="#ffffff",
                activebackground="#3e3e42",
                activeforeground="#ffffff",
                relief="flat",
                state="disabled",
                command=lambda l=lvl: self.select_level(l),
                takefocus=0
            )
            b.pack(side="left", padx=3)
            self.level_buttons.append(b)

        # Lernbereich über dem Editor: drei klare Spalten statt langer Textblock.
        # So wird die Breite besser genutzt und die Hinweise bleiben beim Coden sichtbar.
        self.learning_frame = tk.Frame(self.main, bg="#1e1e1e")
        self.learning_frame.pack(fill="both", padx=20, pady=(4, 10))
        self.learning_frame.grid_columnconfigure(0, weight=4, uniform="learn")
        self.learning_frame.grid_columnconfigure(1, weight=3, uniform="learn")
        self.learning_frame.grid_columnconfigure(2, weight=4, uniform="learn")
        self.learning_frame.grid_rowconfigure(0, weight=1)

        def make_card(parent, column, title, color):
            card = tk.Frame(parent, bg="#252526", highlightthickness=1, highlightbackground="#555555")
            card.grid(row=0, column=column, sticky="nsew", padx=(0 if column == 0 else 8, 0 if column == 2 else 8))
            header = tk.Frame(card, bg="#2d2d30")
            header.pack(fill="x")
            tk.Label(
                header, text=title, bg="#2d2d30", fg=color,
                font=("Segoe UI", 11, "bold"), anchor="w"
            ).pack(fill="x", padx=10, pady=(8, 6))

            body = tk.Frame(card, bg="#252526")
            body.pack(fill="both", expand=True, padx=8, pady=(0, 8))
            text = tk.Text(
                body,
                height=16,
                wrap="word",
                bg="#252526",
                fg="#d4d4d4",
                insertbackground="#ffffff",
                font=("Segoe UI", 10),
                relief="flat",
                padx=8,
                pady=4
            )
            scroll = tk.Scrollbar(body, orient="vertical", command=text.yview)
            text.configure(yscrollcommand=scroll.set)
            text.pack(side="left", fill="both", expand=True)
            scroll.pack(side="right", fill="y")
            return card, text

        self.task_card, self.desc_text = make_card(self.learning_frame, 0, "1. Aufgabe", "#9cdcfe")
        self.requirements_card, self.requirements_text = make_card(self.learning_frame, 1, "2. Lernziel / Checkliste", "#b5cea8")
        self.helper_card, self.hint_text = make_card(self.learning_frame, 2, "3. Hinweise & Beispiel", "#ce9178")

        # Button-Leiste direkt vor dem Editor
        self.controls_frame = tk.Frame(self.main, bg="#1e1e1e")
        self.controls_frame.pack(fill="x", padx=20, pady=(0, 5))

        self.buttons_subframe = tk.Frame(self.controls_frame, bg="#1e1e1e")
        self.buttons_subframe.pack(side="left", anchor="w")

        self.next_button = tk.Button(
            self.buttons_subframe,
            text="Weiter",
            bg="#0e639c",
            fg="#ffffff",
            activebackground="#1177bb",
            activeforeground="#ffffff",
            relief="flat",
            command=self.check_and_next,
            takefocus=0
        )
        self.next_button.pack(side="left", padx=(0, 10))

        self.hint_button = tk.Button(
            self.buttons_subframe,
            text="Hinweis anzeigen",
            bg="#2d2d30",
            fg="#ffffff",
            activebackground="#3e3e42",
            activeforeground="#ffffff",
            relief="flat",
            command=self.show_hint,
            takefocus=0
        )
        self.hint_button.pack(side="left", padx=(0, 10))

        self.controls_info_label = tk.Label(
            self.controls_frame,
            text="",
            bg="#1e1e1e",
            fg="#9cdcfe",
            font=("Segoe UI", 9),
            anchor="w",
            justify="left"
        )
        self.controls_info_label.pack(side="left", padx=(20, 0))

        # Unterer Arbeitsbereich: links Eingabe, rechts bereits gebauter Code.
        # So sieht der Lernende nach einem bestandenen Level, was Schritt für Schritt entsteht.
        self.editor_frame = tk.Frame(self.main, bg="#1e1e1e")
        self.editor_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.editor_frame.grid_columnconfigure(0, weight=1, uniform="editor")
        self.editor_frame.grid_columnconfigure(1, weight=1, uniform="editor")
        self.editor_frame.grid_rowconfigure(1, weight=1)

        self.input_title = tk.Label(
            self.editor_frame, text="Eingabe – deine Lösung", bg="#1e1e1e", fg="#9cdcfe",
            font=("Segoe UI", 10, "bold"), anchor="w"
        )
        self.input_title.grid(row=0, column=0, sticky="ew", padx=(0, 8), pady=(0, 4))

        self.built_title = tk.Label(
            self.editor_frame, text="Gebauter Code – nach bestandenen Leveln", bg="#1e1e1e", fg="#b5cea8",
            font=("Segoe UI", 10, "bold"), anchor="w"
        )
        self.built_title.grid(row=0, column=1, sticky="ew", padx=(8, 0), pady=(0, 4))

        self.input_editor_frame = tk.Frame(self.editor_frame, bg="#1e1e1e", highlightthickness=1, highlightbackground="#555555")
        self.input_editor_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 8))

        self.output_editor_frame = tk.Frame(self.editor_frame, bg="#1e1e1e", highlightthickness=1, highlightbackground="#555555")
        self.output_editor_frame.grid(row=1, column=1, sticky="nsew", padx=(8, 0))

        self.linenumbers = tk.Text(
            self.input_editor_frame,
            width=5,
            bg="#252526",
            fg="#858585",
            font=("Consolas", 11),
            state="disabled",
            relief="flat"
        )
        self.linenumbers.pack(side="left", fill="y")

        self.text_scroll = tk.Scrollbar(self.input_editor_frame, orient="vertical")
        self.text_scroll.pack(side="right", fill="y")

        self.code_box = tk.Text(
            self.input_editor_frame,
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            font=("Consolas", 11),
            undo=True,
            yscrollcommand=self.text_scroll.set
        )
        self.code_box.pack(side="left", fill="both", expand=True)
        self.text_scroll.config(command=self.code_box.yview)

        self.built_scroll = tk.Scrollbar(self.output_editor_frame, orient="vertical")
        self.built_scroll.pack(side="right", fill="y")
        self.built_code_box = tk.Text(
            self.output_editor_frame,
            bg="#1b1b1b",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            font=("Consolas", 11),
            wrap="none",
            relief="flat",
            state="disabled",
            yscrollcommand=self.built_scroll.set
        )
        self.built_code_box.pack(side="left", fill="both", expand=True)
        self.built_scroll.config(command=self.built_code_box.yview)

        self.code_box.tag_config("error_line", background="#512020")
        self.code_box.tag_config("indent_line", background="#333333")
        self.code_box.tag_config("green_point", foreground="#00ff00")
        self.code_box.tag_config("red_point", foreground="#ff0000")

        self.code_box.bind("<KeyRelease>", self.on_key_release)
        self.code_box.bind("<Return>", self.on_return_key)
        self.code_box.bind("<KP_Enter>", self.on_return_key)
        self.code_box.bind("<Tab>", self.on_tab_key)
        self.code_box.bind("<Button-1>", self.on_click_editor)
        self.code_box.bind("<MouseWheel>", self.sync_scroll)
        self.linenumbers.bind("<MouseWheel>", self.sync_scroll)

        self.bottom_frame = tk.Frame(self.main, bg="#1e1e1e")
        self.bottom_frame.pack(pady=10, fill="x")

        self.info_label = tk.Label(
            self.bottom_frame,
            text="",
            bg="#1e1e1e",
            fg="#d4d4d4",
            font=("Segoe UI", 10)
        )
        self.info_label.pack(side="left", padx=20)

        self.progress_label = tk.Label(
            self.bottom_frame,
            text="",
            bg="#1e1e1e",
            fg="#00ff00",
            font=("Segoe UI", 10, "bold")
        )
        self.progress_label.pack(side="right", padx=20)

    def set_readonly_text(self, widget, text):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", text)
        widget.config(state="disabled")

    def build_requirements_panel_text(self, level):
        concept = level.get("concept", "")
        required = level.get("required", [])
        parts = []
        if concept:
            parts.append(f"Lernziel:\n{concept}")
        if self.is_sql_task():
            parts.append(
                "SQL-Grundidee für Anfänger:\n"
                "Eine SQL-Anweisung ist wie ein klarer Satz an die Datenbank.\n"
                "Du sagst zuerst, WAS passieren soll, dann WO es passieren soll, "
                "und danach WELCHE Spalten, Werte oder Bedingungen wichtig sind.\n\n"
                "Beispiel zum Lesen:\n"
                "SELECT name, city\n"
                "FROM users\n"
                "WHERE city = 'Berlin';\n\n"
                "Bedeutung:\n"
                "- SELECT name, city  → zeige nur diese Spalten\n"
                "- FROM users         → aus der Tabelle users\n"
                "- WHERE city = 'Berlin' → nur Zeilen, bei denen city Berlin ist"
            )
            parts.append(
                "Wichtige SQL-Regeln:\n"
                "- Tabellen heißen in diesen Aufgaben users oder orders.\n"
                "- Textwerte stehen in einfachen Hochkommas: 'Berlin'.\n"
                "- Zahlen stehen ohne Hochkommas: 25 oder 49.99.\n"
                "- WHERE begrenzt, welche Zeilen betroffen sind.\n"
                "- Eine SQL-Anweisung endet meistens mit einem Semikolon ;"
            )
        # Der mittlere Bereich soll nicht nur Stichworte zeigen, sondern erklären,
        # was der Code dieses Levels bewirkt und wie der Lernende ihn aufbauen soll.
        work_tip = self.build_work_tip(level)
        if work_tip:
            parts.append("Tipp zum Arbeiten:\n" + work_tip)
        if required:
            parts.append("Checkliste für deine Lösung:\n" + "\n".join(f"✓ {item}" for item in required))
        return "\n\n".join(parts)

    def is_sql_task(self):
        return self.current_task_index >= 15

    def extract_example_solution(self, level):
        """Liefert für jedes Level die vollständige abschreibbare Musterlösung."""
        hints = level.get("hints", []) or []
        for source in reversed(hints):
            text = str(source)
            # Neue Lernpfade benutzen 'Vollständige Lösung zum Abschreiben',
            # ältere Aufgaben benutzen 'Beispiel-Lösung'. Beides muss 1:1
            # als abschreibbarer Code im dritten Hinweis erscheinen.
            match = re.search(
                r"(?:Vollständige Lösung zum Abschreiben|Beispiel-Lösung(?:\s*\([^)]*\))?)\s*:\s*(.*)",
                text,
                re.S,
            )
            if match:
                solution = match.group(1).strip()
                if solution:
                    return solution
        for source in reversed(hints):
            lines = [line.rstrip() for line in str(source).splitlines()]
            code_lines = []
            for line in lines:
                stripped = line.strip()
                upper = stripped.upper()
                if (
                    stripped.startswith("import ")
                    or stripped.startswith("def ")
                    or stripped.endswith("()")
                    or "tk." in stripped
                    or "print(" in stripped
                    or upper.startswith(("SELECT", "FROM", "WHERE", "ORDER BY", "INSERT", "VALUES", "UPDATE", "SET", "DELETE"))
                ):
                    code_lines.append(line)
            if code_lines:
                return "\n".join(code_lines).strip()
        required = level.get("required", []) or []
        upper = " ".join(required).upper()
        if self.is_sql_task():
            if "DELETE" in upper and "AMOUNT" in upper:
                return "DELETE FROM orders\nWHERE amount = 0;"
            if "DELETE" in upper and "USER_ID" in upper:
                return "DELETE FROM orders\nWHERE user_id = 1;"
            if "DELETE" in upper and "USERS" in upper:
                return "DELETE FROM users\nWHERE age < 18;"
            if "DELETE" in upper and "STATUS" in upper:
                return "DELETE FROM orders\nWHERE status = 'open';"
            if "DELETE" in upper:
                return "DELETE FROM orders\nWHERE id = 2;"
            if "UPDATE" in upper and "AMOUNT" in upper:
                return "UPDATE orders\nSET amount = amount + 5\nWHERE status = 'open';"
            if "UPDATE" in upper and "USERS" in upper:
                return "UPDATE users\nSET city = 'Köln'\nWHERE name = 'Bob';"
            if "UPDATE" in upper and "USER_ID" in upper:
                return "UPDATE orders\nSET status = 'paid'\nWHERE user_id = 1;"
            if "UPDATE" in upper and "AMOUNT" in upper and ">" in upper:
                return "UPDATE orders\nSET status = 'review'\nWHERE amount > 50;"
            if "UPDATE" in upper:
                return "UPDATE orders\nSET status = 'paid'\nWHERE id = 1;"
            if "INSERT" in upper and "USERS" in upper and "ORDERS" in upper:
                return "INSERT INTO users (name, age, city)\nVALUES ('Gina', 28, 'Stuttgart');\n\nINSERT INTO orders (user_id, amount, status)\nVALUES (4, 59.90, 'open');"
            if "INSERT" in upper and "ORDERS" in upper:
                return "INSERT INTO orders (user_id, amount, status)\nVALUES (1, 99.50, 'open');"
            if "INSERT" in upper:
                return "INSERT INTO users (name, age, city)\nVALUES ('David', 27, 'Berlin');"
            if "SELECT" in upper and "COUNT" in upper:
                return "SELECT COUNT(*)\nFROM users;"
            if "SELECT" in upper and "DISTINCT" in upper:
                return "SELECT DISTINCT city\nFROM users;"
            if "SELECT" in upper and "ORDER BY" in upper:
                return "SELECT *\nFROM users\nORDER BY age ASC;"
            if "SELECT" in upper and "BETWEEN" in upper:
                return "SELECT *\nFROM users\nWHERE age BETWEEN 20 AND 30;"
            if "SELECT" in upper and "AND" in upper:
                return "SELECT *\nFROM users\nWHERE city = 'Berlin' AND age > 25;"
            if "SELECT" in upper and "CITY" in upper and "BERLIN" in upper:
                return "SELECT *\nFROM users\nWHERE city = 'Berlin';"
            if "SELECT" in upper and "NAME" in upper and "CITY" in upper:
                return "SELECT name, city\nFROM users;"
            return "SELECT *\nFROM users;"
        if required:
            first_def = next((x for x in required if str(x).startswith("def ")), None)
            if first_def:
                name = first_def.replace("def ", "").strip().rstrip(":").rstrip("(")
                return f"def {name}():\n    print('Ich übe dieses Level Schritt für Schritt.')\n\n{name}()"
            return "# Musterlösung mit den Pflichtteilen:\n" + "\n".join(str(x) for x in required)
        return "# Für dieses Level ist keine Musterlösung hinterlegt."

    def build_sql_pattern_example(self, level):
        """Gibt ein verständliches SQL-Muster zurück, ohne die fertige Lösung zu verraten."""
        title = self.tasks[self.current_task_index]["title"].upper()
        required = " ".join(level.get("required", [])).upper()

        if "SELECT" in title or ("SELECT" in required and "WHERE" not in title):
            if "COUNT" in required:
                return "SELECT COUNT(*)\nFROM tabelle;"
            if "DISTINCT" in required:
                return "SELECT DISTINCT spalte\nFROM tabelle;"
            if "ORDER BY" in required:
                return "SELECT *\nFROM tabelle\nORDER BY spalte ASC;"
            return "SELECT spalte1, spalte2\nFROM tabelle;"
        if "WHERE" in title or "WHERE" in required:
            return "SELECT *\nFROM tabelle\nWHERE spalte = wert;"
        if "INSERT" in title or "INSERT" in required:
            return "INSERT INTO tabelle (spalte1, spalte2)\nVALUES (wert1, wert2);"
        if "UPDATE" in title or "UPDATE" in required:
            return "UPDATE tabelle\nSET spalte = neuer_wert\nWHERE bedingung;"
        if "DELETE" in title or "DELETE" in required:
            return "DELETE FROM tabelle\nWHERE bedingung;"
        return "SELECT *\nFROM tabelle;"

    def explain_solution_lines(self, solution):
        lines = [line.rstrip() for line in solution.strip().splitlines() if line.strip()]
        notes = []
        for line in lines:
            upper = line.strip().upper()
            if upper.startswith("SELECT"):
                notes.append("- SELECT legt fest, welche Spalten angezeigt oder berechnet werden.")
            elif upper.startswith("FROM"):
                notes.append("- FROM nennt die Tabelle, aus der die Daten kommen.")
            elif upper.startswith("WHERE"):
                notes.append("- WHERE filtert Zeilen. Nur passende Zeilen werden genommen oder verändert.")
            elif upper.startswith("ORDER BY"):
                notes.append("- ORDER BY sortiert das Ergebnis nach einer Spalte.")
            elif upper.startswith("INSERT"):
                notes.append("- INSERT INTO nennt die Tabelle und die Spalten, in die neue Werte eingefügt werden.")
            elif upper.startswith("VALUES"):
                notes.append("- VALUES enthält die neuen Werte in derselben Reihenfolge wie die Spaltenliste.")
            elif upper.startswith("UPDATE"):
                notes.append("- UPDATE nennt die Tabelle, in der vorhandene Zeilen geändert werden.")
            elif upper.startswith("SET"):
                notes.append("- SET legt fest, welche Spalte welchen neuen Wert bekommt.")
            elif upper.startswith("DELETE"):
                notes.append("- DELETE FROM nennt die Tabelle, aus der Zeilen gelöscht werden.")
        # Duplikate behalten wir nicht mehrfach.
        unique = []
        for n in notes:
            if n not in unique:
                unique.append(n)
        return "\n".join(unique)

    def build_partial_solution(self, level):
        """Zeigt eine starke Starthilfe mit Code-Struktur und gezielten Lücken."""
        solution = self.extract_example_solution(level).strip()
        if not solution:
            return "Noch keine Teillösung vorhanden – nutze die Checkliste."

        if self.is_sql_task():
            text = solution
            replacements = [
                ("'Berlin'", "'____'"),
                ("'Hamburg'", "'____'"),
                ("'München'", "'____'"),
                ("'Köln'", "'____'"),
                ("'paid'", "'____'"),
                ("'open'", "'____'"),
                ("'review'", "'____'"),
                ("David", "____"),
                ("Eva", "____"),
                ("Frank", "____"),
                ("Gina", "____"),
                ("age > 25", "age > ____"),
                ("age < 18", "age < ____"),
                ("BETWEEN 20 AND 30", "BETWEEN ____ AND ____"),
                ("amount > 50", "amount > ____"),
                ("amount = 0", "amount = ____"),
                ("id = 1", "id = ____"),
                ("id = 2", "id = ____"),
                ("user_id = 1", "user_id = ____"),
                ("27", "__"),
                ("99.50", "__.__"),
                ("59.90", "__.__"),
            ]
            changed = False
            for old, new_value in replacements:
                if old in text:
                    text = text.replace(old, new_value, 1)
                    changed = True
                    break
            if not changed:
                lines = text.splitlines()
                if len(lines) > 1:
                    lines[-1] = lines[-1].replace(";", "") + "  -- diesen Teil selbst fertig machen;"
                    text = "\n".join(lines)
                else:
                    text = text.rstrip(";") + " ____;"
            return (
                "Schreibe diese Struktur ab und fülle die Lücken sinnvoll aus:\n\n"
                f"{text}\n\n"
                "Denke dabei so:\n"
                "- Welche Tabelle steht in der Aufgabe?\n"
                "- Welche Spalten oder Werte werden genannt?\n"
                "- Brauche ich eine WHERE-Bedingung, damit nicht alle Zeilen betroffen sind?"
            )

        lines = solution.splitlines()
        nonempty_count = len([line for line in lines if line.strip()])
        if nonempty_count <= 1:
            required = level.get("required", []) or []
            if len(required) >= 2:
                return "\n".join(required[:-1]) + "\n# Ergänze den letzten wichtigen Teil selbst."
            return solution + "\n# Prüfe selbst, ob ein Aufruf oder eine wichtige Zeile fehlt."

        visible = max(1, int(len(lines) * 0.75))
        partial = lines[:visible]
        if visible < len(lines):
            partial.append("# Ergänze die letzten Zeilen selbst.")
        return "\n".join(partial)

    def build_first_hint_text(self, level):
        concept = level.get("concept", "")
        required = level.get("required", []) or []
        if self.is_sql_task():
            title = self.tasks[self.current_task_index]["title"].upper()
            if "SELECT" in title:
                basis = (
                    "SQL bedeutet: Du formulierst eine klare Anfrage an eine Tabelle.\n"
                    "Bei SELECT willst du Daten ansehen. Die Grundform ist:\n\n"
                    "SELECT spalte1, spalte2\n"
                    "FROM tabellenname;\n\n"
                    "SELECT sagt, welche Spalten angezeigt werden. FROM sagt, aus welcher Tabelle sie kommen.\n"
                    "Wenn alle Spalten angezeigt werden sollen, benutzt du * statt einzelner Spalten.\n"
                )
            elif "WHERE" in title:
                basis = (
                    "WHERE ist ein Filter. Ohne WHERE bekommst du alle Zeilen. Mit WHERE bekommst du nur passende Zeilen.\n"
                    "Die Grundform ist:\n\n"
                    "SELECT *\n"
                    "FROM tabellenname\n"
                    "WHERE spalte = wert;\n\n"
                    "Textwerte stehen in Hochkommas, z.B. 'Berlin'. Zahlen stehen ohne Hochkommas.\n"
                )
            elif "INSERT" in title:
                basis = (
                    "INSERT fügt neue Zeilen in eine Tabelle ein.\n"
                    "Du nennst zuerst die Tabelle und die Spalten, danach die Werte.\n"
                    "Die Grundform ist:\n\n"
                    "INSERT INTO tabellenname (spalte1, spalte2)\n"
                    "VALUES (wert1, wert2);\n\n"
                    "Die Reihenfolge der Werte muss zur Reihenfolge der Spalten passen.\n"
                )
            elif "UPDATE" in title:
                basis = (
                    "UPDATE ändert vorhandene Zeilen.\n"
                    "Sehr wichtig: Meist brauchst du WHERE, sonst änderst du alle Zeilen der Tabelle.\n"
                    "Die Grundform ist:\n\n"
                    "UPDATE tabellenname\n"
                    "SET spalte = neuer_wert\n"
                    "WHERE bedingung;\n\n"
                    "SET beschreibt die Änderung. WHERE beschreibt, welche Zeile(n) geändert werden.\n"
                )
            elif "DELETE" in title:
                basis = (
                    "DELETE löscht Zeilen aus einer Tabelle.\n"
                    "Sehr wichtig: Ohne WHERE löschst du alle Zeilen.\n"
                    "Die Grundform ist:\n\n"
                    "DELETE FROM tabellenname\n"
                    "WHERE bedingung;\n\n"
                    "DELETE FROM sagt, aus welcher Tabelle gelöscht wird. WHERE sagt, welche Zeilen gelöscht werden.\n"
                )
            else:
                basis = "SQL besteht aus klaren Bausteinen: SELECT, FROM, WHERE, INSERT, UPDATE, DELETE.\n"

            example = self.build_sql_pattern_example(level)
            return (
                f"{basis}\n"
                f"Lernziel dieses Levels:\n{concept}\n\n"
                "Passendes Muster für diese Aufgabe:\n"
                f"{example}\n\n"
                "Was du jetzt in deiner Lösung finden musst:\n"
                + "\n".join(f"✓ {item}" for item in required)
                + "\n\nArbeitsweise:\n"
                "1. Schreibe zuerst das SQL-Schlüsselwort.\n"
                "2. Setze danach die richtige Tabelle ein: users oder orders.\n"
                "3. Ergänze Spalten, Werte und Bedingungen aus der Aufgabe.\n"
                "4. Lies die fertige SQL-Anweisung wie einen deutschen Satz."
            )
        return (
            "Baue erst die Grundstruktur, dann die Details.\n\n"
            f"Lernziel:\n{concept}\n\n"
            "Typischer Python-Aufbau:\n"
            "import tkinter as tk  # nur wenn Tkinter gebraucht wird\n\n"
            "def meine_funktion():\n"
            "    # eingerückter Code kommt hier hinein\n"
            "    print('Beispiel')\n\n"
            "meine_funktion()\n\n"
            "Bausteine, die in deiner Lösung vorkommen müssen:\n"
            + "\n".join(f"✓ {item}" for item in required)
        )

    def build_second_hint_text(self, level):
        partial = self.build_partial_solution(level).strip()
        if self.is_sql_task():
            return (
                "Arbeite mit diesem fast fertigen SQL-Code. Fülle nur noch die Lücken und lies jede Zeile bewusst.\n\n"
                f"{partial}\n\n"
                "Prüfe danach:\n"
                "- Steht die richtige Tabelle hinter FROM, INSERT INTO, UPDATE oder DELETE FROM?\n"
                "- Stimmen Textwerte mit Hochkommas, z.B. 'Berlin'?\n"
                "- Gibt es eine WHERE-Zeile, wenn nur bestimmte Zeilen gemeint sind?"
            )
        return (
            "Arbeite mit diesem fast fertigen Code. Ergänze die fehlenden Zeilen selbst.\n\n"
            f"{partial}\n\n"
            "Prüfe danach die Einrückung und ob die Funktion unten wirklich aufgerufen wird."
        )

    def build_third_hint_text(self, level):
        """Dritter Klick: 100% der abschreibbaren Lösung, ohne Lücken."""
        solution = self.extract_example_solution(level).strip()
        if not solution:
            required = level.get("required", []) or []
            solution = "# Vollständige Lösung nicht gefunden. Pflichtteile:\n" + "\n".join(str(x) for x in required)

        if self.is_sql_task():
            return "Schreibe diese SQL-Lösung exakt ab:\n\n" + solution
        return "Schreibe dieses Python-Skript exakt ab:\n\n" + solution

    def build_hint_panel_text(self, level):
        shown_count = max(0, min(int(self.hints_used_current or 0), 3))

        if shown_count == 0:
            return (
                "Nutze den Hilfe-Button als Lernleiter.\n\n"
                "Beim ersten Klick bekommst du eine Erklärung und ein passendes Muster.\n"
                "Beim zweiten Klick bekommst du eine starke Starthilfe mit Code und Lücken.\n"
                "Beim dritten Klick bekommst du die vollständige Lösung zum Abschreiben und Verstehen.\n\n"
                "Punkte pro Level:\n"
                "- selbst gelöst: 2 Punkte\n"
                "- mit erster Hilfe gelöst: 1 Punkt\n"
                "- mit weiterer Hilfe oder Lösung gelöst: 0 Punkte\n\n"
                "Alle Punkte und freigeschalteten Level bleiben gespeichert, bis du „Reset all“ drückst."
            )

        sections = []
        try:
            if shown_count == 1:
                sections.append(self.build_first_hint_text(level))
            elif shown_count == 2:
                sections.append(self.build_second_hint_text(level))
            else:
                sections.append(self.build_third_hint_text(level))
        except Exception as exc:
            sections.append(
                "Nutze diese Pflichtteile für deine Lösung:\n"
                + "\n".join(f"✓ {item}" for item in (level.get("required", []) or []))
                + f"\n\nTechnischer Hinweis: {exc}"
            )

        text = "\n\n".join(part for part in sections if str(part).strip())
        if not text.strip():
            text = (
                "Für dieses Level wurden keine speziellen Hinweise gefunden. "
                "Nutze die Checkliste und schreibe die Grundstruktur der Aufgabe."
            )
        return text + "\n"


    def build_work_tip(self, level):
        """Kurzer aufgabenspezifischer Arbeitstipp für die mittlere Karte."""
        specific_tip = str(level.get("work_tip", "") or "").strip()
        if specific_tip:
            return specific_tip
        concept = level.get("concept", "").strip()
        required = [str(x) for x in level.get("required", [])]
        req_text = ", ".join(required[:4])
        if self.is_sql_task():
            title = self.tasks[self.current_task_index]["title"]
            if "SELECT" in title:
                return "Tipp: Beginne mit SELECT, entscheide dann, welche Spalten du sehen willst, und schreibe danach FROM mit der Tabelle. Prüfe am Ende, ob ORDER BY, DISTINCT oder COUNT gebraucht wird."
            if "WHERE" in title:
                return "Tipp: Schreibe zuerst die Grundabfrage SELECT ... FROM users. Danach begrenzt du mit WHERE genau die Zeilen, die zur Bedingung passen."
            if "INSERT" in title:
                return "Tipp: Bei INSERT müssen Spaltenliste und VALUES exakt zusammenpassen. Textwerte stehen in Hochkommas, Zahlen nicht."
            if "UPDATE" in title:
                return "Tipp: Schreibe UPDATE, dann SET für den neuen Wert und immer WHERE, damit nicht versehentlich alle Zeilen geändert werden."
            if "DELETE" in title:
                return "Tipp: Schreibe DELETE FROM und danach immer eine WHERE-Bedingung. Ohne WHERE würdest du zu viele Daten löschen."
            return "Tipp: Lies die SQL-Aufgabe wie einen Satz: Was soll passieren, in welcher Tabelle, und welche Bedingung grenzt die Daten ein?"
        if any("tk.Tk" in r or "Label" in r or "Button" in r or "Entry" in r for r in required):
            return "Tipp: Baue die Oberfläche von oben nach unten: zuerst root/Fenster, dann Widgets erstellen, mit pack() anzeigen und am Ende mainloop() starten."
        if any("def " in r for r in required):
            return f"Tipp: Lege zuerst die Funktion an und rücke den Funktionskörper ein. Danach rufst du die Funktion unten auf, damit der Code wirklich ausgeführt wird."
        if concept:
            return f"Tipp: Dieses Level übt {concept}. Schreibe zuerst die Grundstruktur und ergänze dann nur die Zeilen, die in der Checkliste verlangt werden."
        if req_text:
            return f"Tipp: Arbeite die Pflichtteile nacheinander ab: {req_text}. Danach mit Weiter prüfen."
        return "Tipp: Schreibe eine kleine vollständige Lösung, prüfe Einrückung und lies jede Zeile laut: Was macht diese Zeile?"

    def build_completed_code_text(self):
        """Zeigt die erfolgreich abgegebenen Lösungen der aktuellen Aufgabe als Baufortschritt."""
        tkey = str(self.current_task_index)
        task_progress = self.progress.get("tasks", {}).get(tkey, {})
        completed = task_progress.get("completed_code", {}) or {}
        task = self.tasks[self.current_task_index]
        blocks = []
        for idx in range(self.levels_per_task):
            code = str(completed.get(str(idx), "") or "").strip()
            if code:
                blocks.append(f"# {task['title']} – Level {idx + 1}\n{code}")
        if not blocks:
            return (
                "# Hier erscheint dein gebauter Code.\n"
                "# Sobald du ein Level richtig abschließt, wird deine abgegebene Lösung hier gespeichert.\n"
                "# So kannst du sehen, wie die Anwendung/Abfrage Schritt für Schritt wächst."
            )
        return "\n\n".join(blocks)

    def update_completed_code_panel(self):
        if not hasattr(self, "built_code_box"):
            return
        self.built_code_box.config(state="normal")
        self.built_code_box.delete("1.0", "end")
        self.built_code_box.insert("1.0", self.build_completed_code_text())
        self.built_code_box.config(state="disabled")
        self.built_code_box.yview_moveto(0)

    def select_task(self, task_index):
        """Wählt eine Aufgabe aus und startet eine neue Lern-Wiederholung."""
        self.current_task_index = task_index
        max_level = self.progress["tasks"][str(task_index)]["max_level"]
        self.current_level_index = max_level
        self.hints_used_current = 0
        self.current_attempt_hints = 0
        self.update_ui_for_task_and_level()

    def select_level(self, level_index):
        """Wählt ein freigeschaltetes Level aus und startet einen neuen Versuch."""
        max_level = self.progress["tasks"][str(self.current_task_index)]["max_level"]
        if level_index <= max_level:
            self.current_level_index = level_index
            self.hints_used_current = 0
            self.current_attempt_hints = 0
            self.update_ui_for_task_and_level()

    def update_ui_for_task_and_level(self):
        task = self.tasks[self.current_task_index]
        level = task["levels"][self.current_level_index]

        self.title_label.config(
            text=f"{task['title']} – Level {self.current_level_index+1}"
        )
        self.set_readonly_text(self.desc_text, level["description"])
        self.set_readonly_text(self.requirements_text, self.build_requirements_panel_text(level))
        self.set_readonly_text(self.hint_text, self.build_hint_panel_text(level))
        self.hint_text.yview_moveto(0)
        self.update_completed_code_panel()

        self.code_box.delete("1.0", "end")
        self.code_box.focus_set()
        self.code_box.tag_remove("error_line", "1.0", "end")
        self.code_box.tag_remove("green_point", "1.0", "end")
        self.code_box.tag_remove("red_point", "1.0", "end")
        self.update_linenumbers()
        self.draw_indent_guides()

        for i, btn in enumerate(self.level_buttons):
            max_level = self.progress["tasks"][str(self.current_task_index)]["max_level"]
            if i <= max_level:
                btn.config(state="normal", bg="#2d2d30")
            else:
                btn.config(state="disabled", bg="#1e1e1e")

        points = self.progress["tasks"][str(self.current_task_index)]["points"]
        total_points = sum(task_progress.get("points", 0.0) for task_progress in self.progress.get("tasks", {}).values())
        self.score_label.config(text=f"⭐ Punkte gesamt: {total_points:.1f}  |  Aufgabe: {points:.1f}")
        self.info_label.config(
            text=(
                f"Aufgabe {self.current_task_index+1}, Level {self.current_level_index+1} | "
                f"Hinweise in diesem Versuch: {self.current_attempt_hints} | "
                f"Punkte Aufgabe: {points:.1f}"
            )
        )

        max_level = self.progress["tasks"][str(self.current_task_index)]["max_level"]
        try:
            self.hint_button.config(text=f"Hinweis anzeigen ({min(int(self.current_attempt_hints or 0), 3)}/3)")
        except Exception:
            pass

        self.progress_label.config(
            text=f"Fortschritt: Level {max_level+1}/5"
        )

        self.controls_info_label.config(
            text=(
                self.build_work_tip(level) + " · "
                "● Grün: Zeile erfüllt Anforderungen · ● Rot: hier stimmt etwas noch nicht · Enter übernimmt Einrückung"
            )
        )

    def update_linenumbers(self, event=None):
        self.linenumbers.config(state="normal")
        self.linenumbers.delete("1.0", "end")
        line_count = int(self.code_box.index("end-1c").split(".")[0])
        for i in range(1, line_count + 1):
            self.linenumbers.insert("end", f"{i}\n")
        self.linenumbers.config(state="disabled")


    def draw_indent_guides(self):
        """Markiert Einrückungsebenen im Editor dezent im Hintergrund."""
        self.code_box.tag_remove("indent_line", "1.0", "end")
        line_count = int(self.code_box.index("end-1c").split(".")[0])
        for line_no in range(1, line_count + 1):
            line_text = self.code_box.get(f"{line_no}.0", f"{line_no}.end")
            leading_spaces = len(line_text) - len(line_text.lstrip(" "))
            # Jede Einrückungsebene entspricht 4 Leerzeichen.
            for col in range(4, leading_spaces + 1, 4):
                self.code_box.tag_add("indent_line", f"{line_no}.{col-1}", f"{line_no}.{col}")

    def on_key_release(self, event=None):
        self.update_linenumbers()
        self.draw_indent_guides()
        self.code_box.tag_remove("green_point", "1.0", "end")
        self.code_box.tag_remove("red_point", "1.0", "end")

    def on_return_key(self, event):
        """Enter erzeugt im Code-Editor eine echte neue Zeile.

        Zusätzlich wird die Einrückung der aktuellen Zeile übernommen.
        Endet die aktuelle Zeile mit einem Doppelpunkt, wird automatisch
        eine weitere Python-Ebene mit 4 Leerzeichen ergänzt.
        """
        cursor = self.code_box.index("insert")
        line, _ = map(int, cursor.split("."))
        current_line = self.code_box.get(f"{line}.0", f"{line}.end")

        indent = ""
        for ch in current_line:
            if ch in (" ", "\t"):
                indent += ch
            else:
                break

        # Nur den Teil vor dem Cursor für die Doppelpunkt-Prüfung verwenden.
        before_cursor = self.code_box.get(f"{line}.0", "insert")
        if before_cursor.rstrip().endswith(":"):
            indent += "    "

        self.code_box.insert("insert", "\n" + indent)
        self.update_linenumbers()
        self.draw_indent_guides()
        return "break"

    def on_tab_key(self, event=None):
        """Tab fügt im Editor 4 Leerzeichen ein, statt den Fokus zu wechseln."""
        self.code_box.insert("insert", "    ")
        self.update_linenumbers()
        self.draw_indent_guides()
        return "break"

    def on_click_editor(self, event=None):
        self.code_box.after(1, self.update_linenumbers)

    def sync_scroll(self, event):
        self.code_box.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.linenumbers.yview_moveto(self.code_box.yview()[0])
        return "break"

    def show_hint(self):
        """Hinweis-Button: jeder Klick erhöht die Hilfe-Stufe dieses Versuchs.

        Klick 1: echter Lernhinweis / Erklärung, was in die Lösung muss.
        Klick 2: ca. 75% der Lösung inklusive Code-Struktur.
        Klick 3: vollständige Lösung zum Abschreiben. Danach gibt es 0 Punkte.
        """
        level = self.tasks[self.current_task_index]["levels"][self.current_level_index]
        tkey = str(self.current_task_index)
        lkey = str(self.current_level_index)

        old_stage = int(getattr(self, "current_attempt_hints", 0) or 0)
        new_stage = min(old_stage + 1, 3)
        self.current_attempt_hints = new_stage
        self.hints_used_current = new_stage

        self.progress.setdefault("tasks", {})
        self.progress["tasks"].setdefault(tkey, {})
        self.progress["tasks"][tkey].setdefault("hints_used", {})
        previous_saved = int(self.progress["tasks"][tkey]["hints_used"].get(lkey, 0) or 0)
        self.progress["tasks"][tkey]["hints_used"][lkey] = max(previous_saved, new_stage)
        self.save_progress()

        if new_stage == 1:
            body = self.build_first_hint_text(level)
            points_now = 1
        elif new_stage == 2:
            body = self.build_second_hint_text(level)
            points_now = 0
        else:
            body = self.build_third_hint_text(level)
            points_now = 0

        text = str(body).strip() + "\n"
        if not str(body).strip():
            text += "\nPflichtteile:\n" + "\n".join(f"✓ {x}" for x in (level.get("required", []) or []))

        self.hint_text.config(state="normal")
        self.hint_text.delete("1.0", "end")
        self.hint_text.insert("1.0", text)
        self.hint_text.tag_configure("hint_title", foreground="#ffcc66", font=("Segoe UI", 11, "bold"))
        self.hint_text.tag_add("hint_title", "1.0", "1.end")
        self.hint_text.see("1.0")
        self.hint_text.yview_moveto(0)
        self.hint_text.config(state="disabled")

        self.hint_button.config(text=f"Hinweis anzeigen ({new_stage}/3)")
        try:
            self.helper_card.config(highlightbackground="#ffcc66", highlightthickness=3)
        except Exception:
            pass

        points = self.progress["tasks"].get(tkey, {}).get("points", 0.0)
        total_points = sum(tp.get("points", 0.0) for tp in self.progress.get("tasks", {}).values())
        self.score_label.config(text=f"⭐ Punkte gesamt: {total_points:.1f}  |  Aufgabe: {points:.1f}")
        self.info_label.config(
            text=(
                f"Aufgabe {self.current_task_index+1}, Level {self.current_level_index+1} | "
                f"Hinweise in diesem Versuch: {new_stage}/3 | "
                f"Punkte bei Lösung jetzt: {points_now}"
            )
        )
        self.root.update_idletasks()
        self.code_box.focus_set()

    def blink_error_line(self, line_index, count=6):
        if count <= 0:
            self.code_box.tag_remove("error_line", f"{line_index}.0", f"{line_index}.0 lineend")
            return
        current_bg = self.code_box.tag_cget("error_line", "background")
        new_bg = "#aa0000" if current_bg == "#512020" else "#512020"
        self.code_box.tag_config("error_line", background=new_bg)
        self.root.after(200, self.blink_error_line, line_index, count - 1)

    def highlight_error_line(self, line):
        self.code_box.tag_remove("error_line", "1.0", "end")
        self.code_box.tag_add("error_line", f"{line}.0", f"{line}.0 lineend")
        self.code_box.see(f"{line}.0")
        self.blink_error_line(line)

    def show_indent_help(self, line_text):
        stripped = line_text.lstrip()
        indent = len(line_text) - len(stripped)
        messagebox.showinfo(
            "Einrückungshilfe",
            f"Diese Zeile hat {indent} Leerzeichen Einrückung.\n\n"
            "Merke dir:\n"
            "- Nach 'def ...:' und 'if ...:' kommt ein eingerückter Block\n"
            "- Jede Ebene = 4 Leerzeichen\n"
            "- Die Linien im Editor zeigen dir die Ebenen\n"
        )

    def mark_error(self, user_code, missing_required):
        lines = user_code.split("\n")
        for idx, line in enumerate(lines, start=1):
            for req in missing_required:
                base = req.split("(")[0].strip()
                if base and base in line:
                    self.highlight_error_line(idx)
                    self.place_red_point(idx)
                    return
        if lines:
            self.highlight_error_line(1)
            self.place_red_point(1)

    def place_green_points(self, user_code, required):
        self.code_box.tag_remove("green_point", "1.0", "end")
        lines = user_code.split("\n")
        for idx, line in enumerate(lines, start=1):
            if line.strip():
                self.code_box.insert(f"{idx}.0", "● ")
                self.code_box.tag_add("green_point", f"{idx}.0", f"{idx}.1")

    def place_red_point(self, line_index):
        self.code_box.insert(f"{line_index}.0", "● ")
        self.code_box.tag_add("red_point", f"{line_index}.0", f"{line_index}.1")

    def check_and_next(self):
        user_code = self.code_box.get("1.0", "end").strip()
        task = self.tasks[self.current_task_index]
        level = task["levels"][self.current_level_index]
        required = level["required"]
        concept = level.get("concept", "dieses Konzept")

        missing = [r for r in required if r not in user_code]
        self.code_box.tag_remove("green_point", "1.0", "end")
        self.code_box.tag_remove("red_point", "1.0", "end")

        if missing:
            msg = "Der Code ist noch nicht korrekt.\n\nEs fehlen oder stimmen nicht folgende Teile:\n"
            msg += "\n".join(f"- {m}" for m in missing)
            messagebox.showerror("Fehler", msg)
            self.mark_error(user_code, missing)
            return

        self.place_green_points(user_code, required)

        attempt_hints = int(getattr(self, "current_attempt_hints", self.hints_used_current) or 0)
        if attempt_hints == 0:
            pts = 2.0
        elif attempt_hints == 1:
            pts = 1.0
        else:
            pts = 0.0

        tkey = str(self.current_task_index)
        lkey = str(self.current_level_index)

        self.progress["tasks"][tkey].setdefault("completed_code", {})
        self.progress["tasks"][tkey]["completed_code"][lkey] = user_code

        self.progress["tasks"][tkey]["points"] += pts

        max_level = self.progress["tasks"][tkey]["max_level"]
        if self.current_level_index == max_level and self.current_level_index < self.levels_per_task - 1:
            self.progress["tasks"][tkey]["max_level"] = max_level + 1
            messagebox.showinfo(
                "Gratulation",
                f"Gratulation, du hast soeben {concept} gebaut/geübt!\n\n"
                f"Du erhältst {pts} Punkte.\n"
                f"Weiter zu Level {self.current_level_index+2}."
            )
            self.current_level_index += 1
        else:
            messagebox.showinfo(
                "Gratulation",
                f"Gratulation, du hast soeben {concept} gebaut/geübt!\n\n"
                f"Du erhältst {pts} Punkte."
            )

        # Nach einer abgegebenen Lösung beginnt der nächste Versuch wieder ohne aktuelle Hinweise.
        # Die historisch genutzte höchste Hinweisstufe bleibt in progress.json gespeichert.
        self.current_attempt_hints = 0
        self.hints_used_current = 0
        self.save_progress()
        self.update_ui_for_task_and_level()


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainerApp(root)
    root.mainloop()
########################gebaut von sey37801################################