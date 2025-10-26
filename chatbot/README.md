# Django + ChatterBot Terminal Client

A minimal terminal chat client using **Django** (for structure/packaging) and **ChatterBot** for responses.

## Features
- `python manage.py chatbot` runs an interactive terminal chat.
- `:reset` to wipe/retrain the ChatterBot SQLite database.
- Trains on `chatterbot_corpus` (greetings + conversations) and `bot/corpus/custom.yml`.

## Setup
```bash
cd chatbot_terminal
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py chatbot
```
