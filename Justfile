export FLASK_APP := "app.main"
db_url := "sqlite:///db/demo.sqlite3"


start:
    ./.venv/bin/python -m flask run 

# generate sqlalchemy from database
gen-sqlalchemy:
    sqlacodegen --generator declarative --outfile app/domain/models.py --tables "hero" "{{ db_url }}"
