# photo_task_manager.py
from database import PhotoTaskDatabase

class PhotoTaskManager:
    def __init__(self):
        self.database = PhotoTaskDatabase()

    def create_photo_task(self, description, deadline):
        self.database.create_task(description, deadline)

    def display_photo_tasks(self):
        tasks = self.database.get_all_tasks()
        if tasks:
            print("\nListe des tâches photo :")
            for task in tasks:
                print(f"ID: {task[0]}, Description: {task[1]}, Date d'échéance: {task[2]}, Statut: {task[3]}")
        else:
            print("Aucune tâche photo trouvée.")

    def mark_task_as_done(self, task_id):
        if self.database.task_exists(task_id):
            self.database.mark_task_as_done(task_id)
            print(f"Tâche photo avec l'ID {task_id} marquée comme terminée.")
        else:
            print(f"Tâche photo avec l'ID {task_id} non trouvée.")

    def delete_photo_task(self, task_id):
        if self.database.task_exists(task_id):
            self.database.delete_task(task_id)
            print(f"Tâche photo avec l'ID {task_id} supprimée.")
        else:
            print(f"Tâche photo avec l'ID {task_id} non trouvée.")
