from db_handler import add_task, get_tasks, update_task_status, delete_task

def main():
    # Example flow
    print("Smart Task Manager Backend")

    # Add a sample task
    add_task("Phase 3 Integration", "Wire DB with app logic", "2026-06-20")

    # Show all tasks
    tasks = get_tasks()
    print("Tasks:", tasks)

    # Update a task
    update_task_status(1, "Completed")

    # Show updated tasks
    print("Updated Tasks:", get_tasks())

if __name__ == "__main__":
    main()
