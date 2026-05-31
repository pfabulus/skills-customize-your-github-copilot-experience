import sqlite3
from sqlite3 import Connection
from typing import List, Tuple, Optional

DB_FILE = "python_sqlite.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
"""


def get_connection() -> Connection:
    conn = sqlite3.connect(DB_FILE)
    return conn


def initialize_database(conn: Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()


def add_note(conn: Connection, title: str, content: str) -> int:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content),
    )
    conn.commit()
    return cursor.lastrowid


def get_all_notes(conn: Connection) -> List[Tuple[int, str, str, str]]:
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, created_at FROM notes")
    return cursor.fetchall()


def get_note_by_id(conn: Connection, note_id: int) -> Optional[Tuple[int, str, str, str]]:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, content, created_at FROM notes WHERE id = ?",
        (note_id,),
    )
    return cursor.fetchone()


def update_note(conn: Connection, note_id: int, title: str, content: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notes SET title = ?, content = ? WHERE id = ?",
        (title, content, note_id),
    )
    conn.commit()
    return cursor.rowcount > 0


def delete_note(conn: Connection, note_id: int) -> bool:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    return cursor.rowcount > 0


if __name__ == "__main__":
    conn = get_connection()
    initialize_database(conn)

    print("Database initialized.")
    first_id = add_note(conn, "First note", "This is a starter note.")
    print(f"Added note with id={first_id}")

    notes = get_all_notes(conn)
    print("All notes:")
    for note in notes:
        print(note)

    note = get_note_by_id(conn, first_id)
    print("Fetched note:", note)

    updated = update_note(conn, first_id, "Updated title", "Updated content.")
    print("Updated note:", updated)

    deleted = delete_note(conn, first_id)
    print("Deleted note:", deleted)

    conn.close()
