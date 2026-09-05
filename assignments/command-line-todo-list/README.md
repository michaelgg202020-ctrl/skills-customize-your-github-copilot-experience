# 📘 Assignment: Command-Line To-Do List

## 🎯 Objective

Build a command-line to-do list in Python while practicing lists, dictionaries, loops, functions, and user input validation.

## 📝 Tasks

### 🛠️ Create the Task List

#### Description

Create the program's task list and write a function that displays the current tasks with their completion status.

#### Requirements

Completed program should:

- Store each task with a description and a completed status.
- Display a helpful message when there are no tasks.
- Number tasks starting at 1 when displaying them.
- Show whether each task is complete or incomplete.

### 🛠️ Add Task Actions

#### Description

Add functions that let the user create a task, mark a task as complete, and remove a task from the list.

#### Requirements

Completed program should:

- Ask the user for a task description and add it as incomplete.
- Let the user select a task number to mark as complete.
- Let the user select a task number to delete.
- Handle invalid task numbers without crashing.

### 🛠️ Build the Menu Loop

#### Description

Connect the task actions with a repeating menu so the user can manage tasks until choosing to quit.

#### Requirements

Completed program should:

- Display options to view, add, complete, delete, or quit.
- Call the correct function for the selected option.
- Continue showing the menu after each action.
- Display a friendly message when the user quits.

Example menu:

```text
1. View tasks
2. Add a task
3. Complete a task
4. Delete a task
5. Quit
```
