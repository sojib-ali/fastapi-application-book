import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str|None = None, reset: bool = False):
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    
    if not name:
        name = os.getenv('CRYPTID_SQLITE_DB')
        # Go up three levels from /src/data/init.py to the project root
        top_dir = Path(__file__).resolve().parent.parent.parent
        db_dir = top_dir / 'db'
        os.makedirs(db_dir, exist_ok=True) # Ensure db directory exists
        db_name = 'cryptid.db'
        db_path = str(db_dir/db_name)
        name = os.getenv('CRYPTID_SQLITE_DB', db_path)
    conn = connect(name, check_same_thread = False)
    curs = conn.cursor()

get_db()