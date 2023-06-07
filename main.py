# Dynamic list. To do list

# libraries
import os, time

# Color change subroutine
def c(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

# To-Do List
tasks = []

# Title
title = f"{c('purple')}My To-Do list\n"
print(f"{title:^35}")

# First use
print(f"{c('white')}Add the first task...\n")
task = input()
print()
tasks.append(task)
print("First task added!")
time.sleep(1)
os.system("clear")

# Action
while True:
  action = input(f"""
  {c('white')}What do you want to do with your tasks?
  {c('yellow')}
  1. View
  2. Add
  3. Remove
  4. Edit
  {c('white')}
  """)
  if action == "1":
    for i in tasks:
      print()
      print(f"{i}")
      print("---")
      continue
  elif action == "2":
    print()
    print(f"{c('white')}Write your new task...")
    print()
    task = input()
    tasks.append(task)
    print("Task added!")
    time.sleep(1)
    os.system("clear")
    continue
  elif action == "3":
    print(f"{c('white')}Which one you want to delete?")
    n = 0
    for i in tasks:
      n = n + 1
      print(f"{n}. {i}")
    tasknum = input()
    tasks.remove(tasknum)
    print("Task removed!")
    time.sleep(2)
    os.system("clear")
  else:
    print(f"{c('white')}Which one you want to change")
    continue
    
# Course solution:
# import os, time
# toDoList = []

# def printList():
#   print()
#   for item in toDoList:
#     print(item)
#   print()

# while True:
#   menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
#   if menu=="view":
#     printList()
#   elif menu=="add":
#     item = input("What do you want to add?\n")
#     toDoList.append(item)
#   elif menu=="edit":
#     item = input("What do you want to remove?\n")
#     if item in toDoList:
#       toDoList.remove(item)