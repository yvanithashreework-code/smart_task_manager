import streamlit as st
from db_handler import add_task, get_tasks, update_task_status, delete_task

st.title("🧠 Smart Task Manager")

# --- Add Task Section ---
st.subheader("Add a New Task")
title = st.text_input("Task Title")
description = st.text_area("Description")
due_date = st.date_input("Due Date")

if st.button("Add Task"):
    add_task(title, description, str(due_date))
    st.success("✅ Task added successfully!")

# --- View Tasks Section ---
st.subheader("View All Tasks")
tasks = get_tasks()
for task in tasks:
    st.write(f"🆔 {task[0]} | **{task[1]}** — {task[2]} (Status: {task[3]}, Due: {task[4]})")

# --- Update Task Status ---
st.subheader("Update Task Status")
task_id = st.number_input("Enter Task ID to update", min_value=1)
new_status = st.selectbox("New Status", ["Pending", "Completed"])
if st.button("Update Status"):
    update_task_status(task_id, new_status)
    st.success("✅ Status updated!")

# --- Delete Task ---
st.subheader("Delete Task")
delete_id = st.number_input("Enter Task ID to delete", min_value=1)
if st.button("Delete Task"):
    delete_task(delete_id)
    st.warning("🗑️ Task deleted!")
