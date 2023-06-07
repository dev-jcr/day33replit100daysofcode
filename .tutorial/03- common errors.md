# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Removing something that is not there
👉 Add "recording" to your list when you hit `run`. Now, remove "nap." Yikes! An ugly error message.


  
```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
```
<details> <summary> 👀 Answer </summary>
The error message is just saying "x not in list". What does that mean? The thing you asked to remove is not there. (i.e. You asked to remove a nap from a list that it was not added to in the first place). The best workaround is to add a nested `if` statement to  your code:

```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```

Try it again. Can you try to remove something that does not already exist in the list?

</details>
👉 Yuck! Why is this not working? What does that error even mean?

```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    item.append(myAgenda)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      item.remove(myAgenda)
    else:
      print(f"{item} was not in the list")
  printList()
```
<details> <summary> 👀 Answer </summary>

The problem is with the `append` function. We have two objects backwards. The list name comes *first* and then what's being added to the list goes inside `()`. Hint: You will see the same issue with `remove` too.

It always needs to be: `listname.append()` or `listname.remove()`
  
```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```


</details>