Lab- Many To Many Zombies

You will need both psycopg2 and Flask installed to run this app. 

Download all files.
In Terminal, navigate into the folder

Then type into Terminal:

dropdb zombies
createdb zombies
psql -d zombies -f db/zombies.sql
psql -d zombies -f db/zombies.sql
python3 console.py
flask run

Then command click the URL that appears in Terminal

Control C to exit Flask