# main.py
from photo_task_manager import PhotoTaskManager

def main():
    task_manager = PhotoTaskManager()

    while True:
        print("\n===== Photo Task Manager CLI =====")
        print("1. Créer une nouvelle tâche photo")
        print("2. Afficher les tâches photo")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche photo")
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            task_description = input("Description de la tâche : ")
            deadline = input("Date d'échéance (YYYY-MM-DD) : ")
            task_manager.create_photo_task(task_description, deadline)
        elif choice == "2":
            task_manager.display_photo_tasks()
        elif choice == "3":
            task_id = input("ID de la tâche à marquer comme terminée : ")
            task_manager.mark_task_as_done(task_id)
        elif choice == "4":
            task_id = input("ID de la tâche à supprimer : ")
            task_manager.delete_photo_task(task_id)
        elif choice == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
