# database.py
import sqlite3
from utils import create_directory_if_not_exists

class PhotoTaskDatabase:
    def __init__(self):
        create_directory_if_not_exists("data")
        self.connection = sqlite3.connect("data/photo_tasks.db")
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                deadline TEXT,
                status TEXT DEFAULT 'En cours'
            )
            """)

    def create_task(self, description, deadline):
        with self.connection:
            self.connection.execute("INSERT INTO tasks (description, deadline) VALUES (?, ?)", (description, deadline))

    def get_all_tasks(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM tasks").fetchall()

    def mark_task_as_done(self, task_id):
        with self.connection:
            self.connection.execute("UPDATE tasks SET status='Terminée' WHERE id=?", (task_id,))

    def delete_task(self, task_id):
        with self.connection:
            self.connection.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    def task_exists(self, task_id):
        with self.connection:
            result = self.connection.execute("SELECT COUNT(*) FROM tasks WHERE id=?", (task_id,)).fetchone()
            return result[0] > 0
