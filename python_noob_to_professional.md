[Reference](https://youtu.be/qUeud6DvOWI)

# Arguments Defaults

Arguments Defaults is defined when the function is defined not **called**

## Bad Code

```py
def bad_append(n, l=[]):
    l.append(n)
    return l 


l1 = bad_append(0) # [0]
l2 = bad_append(1) # [0, 1] oops 
```

## Professional Code

```python
def append(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l 

l1 = bad_append(0) # [0]
l2 = bad_append(1) # [1]
```
  
---

# manually calling close on a file

## Bad Code

```python
def write_to_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()
```

   **if this `f.write()`call throws an exception, the file will never be closed**

## Professional Code

```python

def write_to_file(filename, content):
    with open(filename) as f:
        f.write(content)
```

---

# Using a bare except

## Bad Code

```python
def bare_except():
    while True:
        try:
            s = input('input a number: ')
            x = int(s)
            break
        except: # oops! can't CTRL+C to exit
            print('Not a number, try again')

```

  bare except will catch CTRL+C

## Professional Code

```python
def bare_except():
    while True:
        try:
            s = input('input a number: ')
            x = int(s)
            break
        except ValueError: 
            print('Not a number, try again')
```
  
---

# Caret and exponentiation

```python
y = x ^ p # bitwise XOR
y = x ** p # Exponentiation
```

---

# Comprehensions

## Bad Code

```python
def never_using_comprehensions():
    squares = {}
    for i in range(10):
        squares[i] = i * i 
```

## Professional Code

```python
def using_comprehensions():
    dict_comp = {i: i * i for i in range(10)}
    list_comp = [i * i for i in range(10)]
    set_comp = {i * i for i in range(10)}
    gen_comp = (i * i for i in range(10))
```

---

# Checking Type Equality

- noog code use `==`

```python
def checking_type_equality():
    chlid_obj = child_class(1, 2)

    if type(p) == parent:
        print('child')
    else: 
        print('not a child')

```

## Professional Code use `isinstance()`

```python
def checking_type_equality():
    chlid_obj = child_class(1, 2)

    if isinstance(chlid_obj, parent_class):
        print('child')
    else: 
        print('not a child')

```

---

# Checking Non, True or False

## Bad Code  use `==`

```python
if x == None:
    print('none')

if x == True:
    print('True')

if x == False:
    print('False')
```

## Professional Code use `is`

```python
if x is None:
    print('none')

if x is True:
    print('True')

if x is False:
    print('False')
```

- checks identity not equality

---

# using `if bool()` or `if len(x)`

## Bad Code  

```python
if bool(x):
    return "it's boolean"
if len(y) != 0:
    return "not empty"
```
  
## Professional Code

```python
if x:
    return "it's boolean"
 if y:
    return "not empty"
```

- the same result but using `if bool()` or `if len()` just shows that you don't know the language that well

---

# Type Hints & Annotations

```python
x: int = 1 
x: list[int] = []
x = list[int]()
```

- Multiple return

```python
def multiple_return() -> Union[str, bool]:
    return 'done', True
```

```python
from typing import Any
def write_to_file(filename: str, data: str) -> Any:
    try:
        with open(filename, 'a') as file:
            file.write(data)
            return 'done'

    except FileNotFoundError as Error:
        print(Error)
        return Error
```

---

# Iteration

## Bad Code  

```python
def range_len_pattern():
    a = [1, 2, 3]
    for i in range(len(a)):
        v = a[i]
```

## Professional Code

```python
def iterate_on_items():
    a = [1, 2, 3]
    for item in a:
        v = item
```

### if you still need the indexes to use

```python
def use_enumerate():
    a = [1, 2, 3]
    for index, value in enumerate(a):
        v = value
        i = index

```

### if you want to use `i` as a syncronizing varialbe to get corresponding items

- Noob

```python
def use_enumerate():
    a = [1, 2, 3]
    b = [4, 5, 6]
    for i in range(len(b)):
        aValue = a[i]
        bValue = b[i]
```

- Professional code use `zip(list, list)`

```python
def use_enumerate():
    a = [1, 2, 3]
    b = [4, 5, 6]
    for aValue, bValue in zip(a, b):
        pass
```

- if you still need the index use `enumerate(zip(list, list))`

```python
def use_enumerate():
    a = [1, 2, 3]
    b = [4, 5, 6]
    for index, (aValue, bValue) in enumerate(zip(a, b)):
        pass

```

# looping over the dictionary keys

## Bad Code

```python
def for_key_in_dict_keys():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d.keys(): 
        pass
```

## Professional Code

- the default iterate on the key

```python
def for_key_in_dict_keys():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        pass
```

---

# Tuple unpacking

## Bad Code

```python
mytuple = (1, 2)
x = mytuple[0]
y = mytuple[1]
```

## Professional Code

```python
mytuple = (1, 2)
x, y = mytuple
```

---

# index counter variable

## Bad Code

```python
l = [1, 2, 3]
i = 0
for i in l:
    i += 1
    pass
```

## Professional Code

```python
l = [1, 2, 3]
for index, value in enumerate(l):
    pass
```

---

# using `time.time` to time

## Bad Code

```python
def execution_time(func: Callable):
    start = time.time()
    func()
    end = time.time()
    print(end - start)
execution_time(do_something)
```

## Professional Code

```python
def real_execution_time(func: Callable):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(end - start)



real_execution_time(so_something)
```

---

# Using `shell=True` in subprocess module

## Bad Code

```python
    import subprocess
    result = subprocess.run(['ls -l'], capture_output=True, shell=True)
    print(result.stdout.decode('utf-8'))
```

- `shell=True` is a source of a lot of security problems
- people did this to add command arguments like `-l` but you can add the command and it's arguments in a list

## Professional Code

```python
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True)
print(result.stdout.decode('utf-8'))
```

---

# Using `from module import *`

## Bad Code

```python
from requests import *
```

- it litters your namespace with variables, Just import the things you actually need

## Professional Code

```python
from requests import get, post
```

# pep8

## Bad Code

```python
def not_following_pep8():
    x = (1, 2)
    y=5
    l = [1,2,3]

    def func(x = 5):
        pass
```

## Professional Code

```python
def following_pep8():
    x = 1, 2
    y = 5
    l = [1, 2, 3]

    def func(x=5):
        pass
```

# Using Python2

- use python3 instead
